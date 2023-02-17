from datetime import datetime
from src.pre_built.sorting import sort_by
from src.insights.jobs import read

PATH = "tests/mocks/sorting.csv"

DATA = [
    {
        "title": "Web developer",
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2020-06-07",
    },
    {
        "title": "Front end developer",
        "min_salary": 2000,
        "max_salary": 2000,
        "date_posted": "2021-06-01",
    },
    {
        "title": "Back end developer",
        "min_salary": 3000,
        "max_salary": 3000,
        "date_posted": "2020-10-09",
    },
    {
        "title": "Full stack end developer",
        "min_salary": 4000,
        "max_salary": 8000,
        "date_posted": "2021-01-01",
    },
]


def test_sort_by_criteria():
    sorted_min = DATA
    sort_by(sorted_min, "min_salary")
    sorted_max = DATA
    sort_by(sorted_max, "max_salary")
    sorted_date = DATA
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
