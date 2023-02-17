from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_data = read(path)
    industries_data = {
        int(industries["max_salary"])
        for industries in jobs_data
        if industries["max_salary"].isnumeric()
    }
    return max(industries_data)

    raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_data = read(path)
    industries_data = {
        int(industries["min_salary"])
        for industries in jobs_data
        if industries["min_salary"].isnumeric()
    }
    return min(industries_data)

    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary doesn't exists")
    elif (
        not str(job["min_salary"]).isnumeric()
        or not str(job["max_salary"]).isnumeric()
    ):
        raise ValueError(
            "job['min_salary'] or job['max_salary'] aren't valid integers"
        )
    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("aren't valid integers")
    elif not str(salary).replace("-", "").isnumeric():
        raise ValueError("aren't valid integers")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    jobs_list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass

    return jobs_list
    raise NotImplementedError
