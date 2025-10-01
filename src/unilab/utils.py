from __future__ import annotations
from typing import Iterable

def hello(name: str) -> str:
    return f"Hello, {name}! Wellcome to master class project: Jupyter + Python."

def mean(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("Empty list.")
    return sum(values) / len(values)