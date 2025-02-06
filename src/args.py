import argparse


def arg_parser(*arguments):
    parser = argparse.ArgumentParser(
        prog="\nCLI Task Manager",
        description="A simple CLI task manager application",
        epilog="Enjoy the program! :)",
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # 'add' command
    parser_add = subparsers.add_parser('add', help='Create a new task')
    parser_add.add_argument('description', type=str, help='Task description')

    # 'update' command
    parser_update = subparsers.add_parser('update', help='Update an existing task')
    parser_update.add_argument('task_id', type=int, help='ID of the task to update')
    parser_update.add_argument('description', type=str, help='New description of the task')

    # 'delete' command
    parser_delete = subparsers.add_parser('delete',  help='Delete a task')
    parser_delete.add_argument('task_id', type=int, help='ID of the task to delete')

    # 'prog' command
    parser_mark_in_progress = subparsers.add_parser('prog', help='Mark a task as in-progress')
    parser_mark_in_progress.add_argument('task_id', type=int, help='ID of the task to mark as in-progress')

    # 'done' command
    parser_mark_done = subparsers.add_parser('done', help='Mark a task as done')
    parser_mark_done.add_argument('task_id', type=int, help='ID of the task to mark as done')

    # 'list' command
    parser_list = subparsers.add_parser('list', help='List tasks')
    parser_list.add_argument('status', type=str, nargs='?', choices=['done', 'todo', 'prog'], help='Filter tasks by status')

    parsed = parser.parse_args(*arguments)
    return parsed