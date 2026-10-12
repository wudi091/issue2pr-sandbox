"""一个给 Issue2PR 练手用的小工具库。"""

from .parse import parse_duration, parse_size
from .stats import mean, median, percentile
from .text import slugify, truncate, word_count

__all__ = [
    "mean",
    "median",
    "parse_duration",
    "parse_size",
    "percentile",
    "slugify",
    "truncate",
    "word_count",
]
