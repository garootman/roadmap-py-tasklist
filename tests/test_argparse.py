import sys

import pytest

from src.args import arg_parser


def test_add_command():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "add", "some task"]
    # Проверяем, что вывод соответствует ожиданиям
    arg_namespace = arg_parser()
    assert arg_namespace.command == "add"
    assert arg_namespace.description == "some task"


def test_update_command():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "update", "1", "some task"]
    # Проверяем, что вывод соответствует ожиданиям
    arg_namespace = arg_parser()
    assert arg_namespace.command == "update"
    assert arg_namespace.task_id == 1
    assert arg_namespace.description == "some task"


def test_delete_command():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "delete", "1"]
    # Проверяем, что вывод соответствует ожиданиям
    arg_namespace = arg_parser()
    assert arg_namespace.command == "delete"
    assert arg_namespace.task_id == 1


def test_mark_in_progress_command():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "prog", "1"]
    # Проверяем, что вывод соответствует ожиданиям
    arg_namespace = arg_parser()
    assert arg_namespace.command == "prog"
    assert arg_namespace.task_id == 1


def test_mark_done_command():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "done", "1"]
    # Проверяем, что вывод соответствует ожиданиям
    arg_namespace = arg_parser()
    assert arg_namespace.command == "done"
    assert arg_namespace.task_id == 1


def test_list_command_with_status():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "list", "done"]
    # Проверяем, что вывод соответствует ожиданиям
    arg_namespace = arg_parser()
    assert arg_namespace.command == "list"
    assert arg_namespace.status == "done"


def test_list_command_without_status():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "list"]
    # Проверяем, что вывод соответствует ожиданиям
    arg_namespace = arg_parser()
    assert arg_namespace.command == "list"
    assert arg_namespace.status == None


def test_list_command_with_wrong_status():
    # Подаем аргументы в sys.argv
    sys.argv = ["my_script.py", "list", "wrong_status"]
    # Проверяем, что вывод соответствует ожиданиям
    with pytest.raises(SystemExit):
        arg_namespace = arg_parser()
