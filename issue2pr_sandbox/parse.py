"""把人类写的量转换成数值。"""

from __future__ import annotations

import re

_DURATION = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*([smhd])\s*$", re.IGNORECASE)
_UNIT_SECONDS = {"s": 1, "m": 60, "h": 3600, "d": 86400}

_SIZE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*(b|kb|mb|gb)\s*$", re.IGNORECASE)
_UNIT_BYTES = {"b": 1, "kb": 1024, "mb": 1024**2, "gb": 1024**3}


def parse_duration(text: str) -> int:
    """把 `5m` / `2h` / `1.5d` 转成秒。"""
    match = _DURATION.match(text)
    if not match:
        raise ValueError(f"看不懂的时长：{text!r}")
    amount, unit = match.groups()
    return int(float(amount) * _UNIT_SECONDS[unit.lower()])


def parse_size(text: str) -> int:
    """把 `10kb` / `1.5mb` 转成字节。"""
    match = _SIZE.match(text)
    if not match:
        raise ValueError(f"看不懂的大小：{text!r}")
    amount, unit = match.groups()
    return int(float(amount) * _UNIT_BYTES[unit.lower()])
