from __future__ import annotations

import ast
import operator
import unicodedata as udata
from typing import Iterable, Tuple, Any

def hello(name: str) -> str:
    return f"Hello, {name}! Wellcome to master class project: Jupyter + Python."

def mean(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("Empty list.")
    return sum(values) / len(values)

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
        l = _eval_node(node.left)
        r = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in _ALLOWED_BINARY_OPS:
            try:
                return _ALLOWED_BINARY_OPS[op_type](l, r)
            except ZeroDivisionError as e:
                raise ZeroDivisionError("Division by zero") from e
        raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
    elif isinstance(node, ast.UnaryOp):
        raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only int and float constants are allowed")
    elif isinstance(node, ast.Expr):
        return _eval_node(node.value)
    raise ValueError(f"Unsupported expression element: {type(node).__name__}")