import pytest

from issue2pr_sandbox.parse import parse_duration, parse_size


def test_parse_duration_units() -> None:
    assert parse_duration("30s") == 30
    assert parse_duration("5m") == 300
    assert parse_duration("2h") == 7200
    assert parse_duration("1.5d") == 129600


def test_parse_duration_is_case_insensitive_and_tolerates_spaces() -> None:
    assert parse_duration(" 5M ") == 300
    assert parse_duration("2H") == 7200


def test_parse_duration_rejects_garbage() -> None:
    with pytest.raises(ValueError):
        parse_duration("soon")
    with pytest.raises(ValueError):
        parse_duration("5 weeks")


def test_parse_size_uses_binary_units() -> None:
    assert parse_size("512b") == 512
    assert parse_size("10kb") == 10240
    assert parse_size("1.5mb") == 1572864
    assert parse_size("2gb") == 2147483648


def test_parse_size_rejects_garbage() -> None:
    with pytest.raises(ValueError):
        parse_size("a lot")
