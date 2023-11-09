import pytest

from main import Worker, Application

@pytest.fixture
def application():
    workers = [
        Worker("John", "Doe", "1990-01-15"),
        Worker("Jane", "Smith", "1985-04-22"),
        Worker("Alice", "Johnson", "1995-08-10"),
    ]
    app = Application(workers)
    return app

def test_getWorkers_whenMatchingCondition_shouldReturnListOfMatchingWorkers(application):
    condition = "John"

    filtered_workers = application.getWorkers(condition)

    assert len(filtered_workers) == 2
    assert any(str(worker) == "John Doe" for worker in filtered_workers)
    assert any(str(worker) == "Alice Johnson" for worker in filtered_workers)

def test_getWorkers_whenNoMatchingCondition_shouldReturnEmptyList(application):
    condition = "xy"

    filtered_workers = application.getWorkers(condition)

    assert len(filtered_workers) == 0