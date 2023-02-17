from src.pre_built.counter import count_ocurrences

PATH = "data/jobs.csv"


def test_counter():
    assert count_ocurrences(PATH, r"javascript") == 122
    assert count_ocurrences(PATH, r"python") == 1639
