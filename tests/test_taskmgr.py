import pytest

from src.taskmgr import TaskManager


@pytest.fixture
def taskman():
    taskman = TaskManager("test.json")
    taskman._TaskManager__delete_file()
    yield taskman
    taskman._TaskManager__delete_file()


@pytest.fixture
def manytasks():
    mt = [
        ("buy groceries", "todo"),
        ("cook dinner", "todo"),
        ("do laundry", "prog"),
        ("clean house", "prog"),
        ("study", "done"),
        ("workout", "done"),
    ]
    return mt


def test_create_task(taskman):
    task = taskman.add_task(description="Buy groceries")
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


def test_get_task(taskman):
    task = taskman.add_task(description="Buy groceries")
    assert taskman.get_task(1) == task


def test_get_task_not_found(taskman):
    assert taskman.get_task(1) is None


def test_update_task(taskman):
    task = taskman.add_task(description="Buy groceries")
    task = taskman.update_task(1, "Buy groceries and cook dinner")
    assert task.description == "Buy groceries and cook dinner"


def test_update_task_status(taskman):
    task = taskman.add_task(description="Buy groceries")
    task = taskman.mark_in_progress(1)
    assert task.status == "prog"
    task = taskman.get_task(1)
    assert task.status == "prog"

    task = taskman.mark_done(1)
    assert task.status == "done"
    task = taskman.get_task(1)
    assert task.status == "done"

    new_task = taskman.add_task(description="other task")
    assert new_task.status == "todo"

    assert len(taskman) == 2


def test_iter_tasks(taskman, manytasks):
    for desc, status in manytasks:
        taskman.add_task(description=desc)
    assert len(taskman) == len(manytasks)
    for i, task in enumerate(taskman):
        assert task.description == manytasks[i][0]


def test_read_file(taskman, manytasks):
    import json
    import os

    for desc, status in manytasks:
        taskman.add_task(description=desc)
        assert os.path.exists("test.json")
        with open("test.json") as f:
            data = json.load(f)
        assert len(taskman) == len(data)


def test_list_tasks(taskman, manytasks):
    for desc, status in manytasks:
        nt = taskman.add_task(description=desc)
        nt_id = nt.id
        if status == "prog":
            taskman.mark_in_progress(nt_id)
        elif status == "done":
            taskman.mark_done(nt_id)
        tt = taskman.get_task(nt_id)
        assert tt.description == desc
        assert tt.status == status

    tasks_total = taskman.list_tasks()
    assert len(tasks_total) == len(manytasks)

    tasks_todo = taskman.list_tasks(status="todo")
    assert len(tasks_todo) == len([t for t in manytasks if t[1] == "todo"])

    tasks_in_progress = taskman.list_tasks(status="prog")
    assert len(tasks_in_progress) == len([t for t in manytasks if t[1] == "prog"])


def test_delete_task(taskman):
    nt = taskman.add_task(description="Buy groceries")
    assert len(taskman) == 1
    taskman.delete_task(22)
    assert len(taskman) == 1
    taskman.delete_task(1)
    assert len(taskman) == 0
