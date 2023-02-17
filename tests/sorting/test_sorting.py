from datetime import datetime
from src.pre_built.sorting import sort_by
from src.insights.jobs import read

PATH = "tests/mocks/sorting.csv"


def test_sort_by_criteria():
    sorted_min = read(PATH)
    sort_by(sorted_min, "min_salary")
    sorted_max = read(PATH)
    sort_by(sorted_max, "max_salary")
    sorted_date = read(PATH)
    sort_by(sorted_date, "date_posted")
    first_date = datetime.strptime(sorted_date[0]["date_posted"], "%Y-%m-%d")
    last_date = datetime.strptime(
        sorted_date[len(sorted_date) - 1]["date_posted"], "%Y-%m-%d"
    )

    assert (
        sorted_min[0]["min_salary"]
        >= sorted_min[len(sorted_min) - 1]["min_salary"]
    )
    assert (
        sorted_max[0]["max_salary"]
        <= sorted_max[len(sorted_max) - 1]["max_salary"]
    )
    assert first_date >= last_date
