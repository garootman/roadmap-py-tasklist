from datetime import datetime

import pytest

from src.task import Task


def test_create_task_nodate():
    task = Task(id=1, description="Buy groceries", status="todo")
    assert task.id == 1
    assert task.description == "Buy groceries"
    assert task.status == "todo"
    # test dict
    assert task.to_dict() == {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": task.createdAt,
        "updatedAt": task.updatedAt,
    }


def test_create_task_withdate():
    now = datetime.now()
    task = Task(
        id=1,
        description="Buy groceries",
        status="todo",
        createdAt=now,
        updatedAt=now,
    )
    assert task.id == 1
    assert task.description == "Buy groceries"
    assert task.status == "todo"
    assert task.createdAt == now
    assert task.updatedAt == now


def test_create_task_invalid_status():
    with pytest.raises(ValueError):
        Task(id=1, description="Buy groceries", status="invalid")


def test_create_task_correct_statuses():
    Task(id=1, description="Buy groceries", status="todo")
    Task(id=1, description="Buy groceries", status="prog")
    Task(id=1, description="Buy groceries", status="done")


def test_task_str():
    task = Task(id=1, description="Buy groceries", status="todo")
    assert str(task) == "Task 1: Buy groceries (todo)"
