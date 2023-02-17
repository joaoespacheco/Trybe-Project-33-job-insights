from src.pre_built.brazilian_jobs import read_brazilian_file

PATH = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    responses = read_brazilian_file(PATH)
    for response in responses:
        assert "title" in response
        assert "salary" in response
        assert "type" in response
