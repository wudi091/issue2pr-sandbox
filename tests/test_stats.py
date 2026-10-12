import pytest

from issue2pr_sandbox.stats import mean, median, percentile


def test_mean() -> None:
    assert mean([1, 2, 3]) == 2.0
    assert mean([2.5, 3.5]) == 3.0


def test_median_of_odd_length_is_the_middle_element() -> None:
    assert median([3, 1, 2]) == 2
    assert median([5]) == 5


def test_median_of_even_length_averages_the_two_middle_values() -> None:
    assert median([1, 2, 3, 4]) == 2.5
    assert median([10, 2, 8, 4]) == 6.0


def test_percentile_interpolates_between_neighbours() -> None:
    assert percentile([1, 2, 3, 4], 50) == 2.5
    assert percentile([1, 2, 3, 4], 0) == 1.0
    assert percentile([1, 2, 3, 4], 100) == 4.0


def test_empty_input_is_rejected() -> None:
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        percentile([], 50)


def test_percentile_rejects_out_of_range_p() -> None:
    with pytest.raises(ValueError):
        percentile([1, 2], 101)
