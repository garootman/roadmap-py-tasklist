import argparse

from src.taskmgr import TaskManager

parser = argparse.ArgumentParser(
    prog="\nCLI Task Manager",
    description="A simple CLI task manager application",
    epilog="Enjoy the program! :)",
)


parser.add_argument("command", help="Command to execute")
parser.add_argument("task_num", help="Task to add, update, or delete")
parser.add_argument("description", help="Description of the task", nargs="?")


args = parser.parse_args()

print(args)


exit()

"""
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

"""


tm = TaskManager("tasks.json")
