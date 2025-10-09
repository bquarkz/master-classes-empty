from __future__ import annotations

import ast
import operator
import random

import unicodedata as udata
import networkx as nx
import matplotlib.pyplot as plt
from typing import Iterable, Tuple, Any

def hello(name: str) -> str:
    return f"Hello, {name}! Wellcome to master class project: Jupyter + Python."

def mean(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("Empty list.")
    return sum(values) / len(values)

def median(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("Empty list.")
    values = sorted(values)
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]

def variance(values: Iterable[float], sample: bool = False) -> float:
    values = list(values)
    if not values:
        raise ValueError("Empty list.")
    n = len(values)
    m = mean(values)
    ss = [(x - m) ** 2 for x in values]
    if n == 1:
        return 0.0
    if sample:
        return sum(ss) / (n - 1)
    else:
        return sum(ss) / n

def count_words(text: str) -> int:
    return text.strip().count(" ") + 1

def _strip_accents(s: str) -> str:
    nkfd = udata.normalize("NFKD", s)
    return "".join(ch for ch in nkfd if not udata.combining(ch))

def count_vowels_consonants(text: str) -> Tuple[int, int]:
    t = _strip_accents(text).lower()
    vowels = 0
    consonants = 0
    for ch in t:
        if ch.isalpha(): # discard numbers and punctuation
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

def evaluate_expression(expr: str) -> Any:
    expr = expr.strip()
    tree = ast.parse(expr, mode="eval")
    return _eval_node(tree.body)

_ALLOWED_BINARY_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def _eval_node(node: ast.expr) -> Any:
    if isinstance(node, ast.BinOp):
        l = _eval_node(node.left) # evaluate left
        r = _eval_node(node.right) # evaluate right
        op_type = type(node.op)
        if op_type in _ALLOWED_BINARY_OPS:
            try:
                return _ALLOWED_BINARY_OPS[op_type](l, r)
            except ZeroDivisionError as e:
                raise ZeroDivisionError("Division by zero") from e
        raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
    elif isinstance(node, ast.UnaryOp): # refuses unary operators
        raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
    elif isinstance(node, ast.Constant): # int and float constants are allowed, they are the leaves of the expression tree
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only int and float constants are allowed")
    elif isinstance(node, ast.Expr): # everything that is not a binary operator (l @ r) should be computed as an expression
        return _eval_node(node.value)
    raise ValueError(f"Unsupported expression element: {type(node).__name__}")

def labefy(node: ast.AST) -> str:
    opType = type(node.op)
    if opType == ast.Add:
        return "+"
    elif opType == ast.Sub:
        return "-"
    elif opType == ast.Mult:
        return "*"
    elif opType == ast.Div:
        return "/"
    else:
        return "?"

def ast_to_graph(node: ast.expr, g: nx.DiGraph, parent: str = None, counter: list = None) -> str:
    if counter is None:
        counter = [0]
    node_id = f"n{counter[0]}"
    counter[0] += 1

    # label nodes with useful info
    if isinstance(node, ast.BinOp):
        label = labefy(node)
    elif isinstance(node, ast.UnaryOp):
        label = type(node.op).__name__ # not sure exactly what to do here...
    elif isinstance(node, ast.Constant):
        label = repr(node.value)
    elif isinstance(node, ast.Expr):
        label = "Expr"
    else:
        label = type(node).__name__

    g.add_node(node_id, label=label)

    if parent is not None:
        g.add_edge(parent, node_id)

    if isinstance(node, ast.BinOp):
        ast_to_graph(node.left, g, node_id, counter)
        ast_to_graph(node.right, g, node_id, counter)
    elif isinstance(node, ast.UnaryOp):
        ast_to_graph(node.operand, g, node_id, counter)
    elif isinstance(node, ast.Expr):
        ast_to_graph(node.value, g, node_id, counter)
    # Constants are leaves

    return node_id

def draw_expression(expr_src: str, figsize: Tuple[int,int]=(8,6)):
    tree = ast.parse(expr_src, mode="eval") if not expr_src.strip().startswith(" ") else ast.parse(expr_src, mode="eval")
    g = nx.DiGraph()
    ast_to_graph(tree.body if isinstance(tree, ast.Expression) else tree, g)
    labels = nx.get_node_attributes(g, "label")
    plt.figure(figsize=figsize)
    pos = nx.spring_layout(g) # graphiviz is much better, but let's keep it simple for now
    nx.draw(g, pos, with_labels=False, arrows=True, node_size=2000, node_color="lightblue")
    nx.draw_networkx_labels(g, pos, labels, font_size=10)
    plt.axis("off")
    plt.show()

def random_numbers_unique(size: int = 30, min_val: int = 0, max_val: int = 100) -> list:
    s = set(random_numbers(size, min_val, max_val))
    while len(s) < size:
        s.add(random.randint(min_val, max_val))
    return list(s)

def random_numbers(size: int = 30, min_val: int = 0, max_val: int = 100) -> list:
    return [random.randint(min_val, max_val) for _ in range(size)]
