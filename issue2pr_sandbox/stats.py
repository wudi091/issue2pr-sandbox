"""数值统计。"""

from __future__ import annotations

from collections.abc import Sequence


def mean(values: Sequence[float]) -> float:
    """算术平均。"""
    if not values:
        raise ValueError("mean() 需要至少一个值")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """中位数。元素个数是偶数时，取中间两个的平均。"""
    if not values:
        raise ValueError("median() 需要至少一个值")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def percentile(values: Sequence[float], p: float) -> float:
    """线性插值分位数，p 取 0~100。"""
    if not values:
        raise ValueError("percentile() 需要至少一个值")
    if not 0 <= p <= 100:
        raise ValueError("p 必须在 0~100 之间")
    ordered = sorted(values)
    if len(ordered) == 1:
        return float(ordered[0])
    position = (len(ordered) - 1) * p / 100
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight
