from issue2pr_sandbox.text import slugify, truncate, word_count


def test_word_count_splits_on_whitespace() -> None:
    assert word_count("hello world") == 2
    assert word_count("  a   b\tc\n") == 3
    assert word_count("") == 0


def test_slugify_folds_runs_of_punctuation_into_one_dash() -> None:
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("  Foo   Bar  ") == "foo-bar"
    assert slugify("a---b") == "a-b"


def test_truncate_leaves_short_text_alone() -> None:
    assert truncate("hello", 10) == "hello"
    assert truncate("hello", 5) == "hello"


def test_truncate_counts_the_ellipsis_inside_the_limit() -> None:
    assert truncate("hello world", 8) == "hello w…"
    assert len(truncate("hello world", 8)) == 8
