import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file
    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, "r", encoding="utf8") as file:
        data_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return [row for row in data_reader]


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_data = read(path)
    jobs = {job["job_type"] for job in jobs_data}
    return jobs

    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    jobs_match = [job for job in jobs if job['job_type'] == job_type]
    return jobs_match
    raise NotImplementedError
