"""字符串工具。"""

from __future__ import annotations

import re

_NON_ALNUM_RUN = re.compile(r"[^a-z0-9]+")


def word_count(text: str) -> int:
    """按空白切词。"""
    return len(text.split())


def slugify(text: str) -> str:
    """转成 URL 友好的形式：小写、非字母数字的连续段折成一个短横线、首尾不留短横线。"""
    return _NON_ALNUM_RUN.sub("-", text.lower()).strip("-")


def truncate(text: str, limit: int, ellipsis: str = "…") -> str:
    """超长就截断并加省略号。limit 是**结果**的总长度上限，省略号也算在里面。"""
    if len(text) <= limit:
        return text
    return text[:limit] + ellipsis
