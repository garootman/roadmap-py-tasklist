# Task manager module class

import json
import os

from .task import Task


class TaskManager:
    """
    A class to manage tasks, that are stored in a json file.
    - Add, Update, and Delete tasks
    - Mark a task as in progress or done
    - List all tasks
    - List all tasks that are done
    - List all tasks that are not done
    - List all tasks that are in progress

    """

    def __init__(self, filename):
        self.__filename = filename
        self.tasks = self.load_tasks()
        
    def __len__(self):
        return len(self.tasks)
    
    def __iter__(self):
        return iter(self.tasks)

    def __save_tasks(self, tasks):
        with open(self.__filename, "w") as f:
            tasks = [task.to_dict() for task in tasks]
            json.dump(tasks, f, indent=4, ensure_ascii=False, default=str)

    def __delete_file(self):
        if os.path.exists(self.__filename):
            os.remove(self.__filename)

    def add_task(self, description):
        # Add a new task
        task = Task(id=len(self.tasks) + 1, description=description, status="todo")
        self.tasks.append(task)
        self.__save_tasks(self.tasks)
        return task

    def update_task(self, task_id, description):
        # Update an existing task
        task = self.get_task(task_id)
        if task:
            task.description = description
            self.__save_tasks(self.tasks)
            return task
        return None

    def delete_task(self, task_id):
        # Delete a task
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.__save_tasks(self.tasks)
            return task
        return None

    def mark_in_progress(self, task_id):
        # Mark a task as in progress
        task = self.get_task(task_id)
        if task:
            task.status = "prog"
            self.__save_tasks(self.tasks)
            return task
        return None

    def mark_done(self, task_id):
        # Mark a task as done
        task = self.get_task(task_id)
        if task:
            task.status = "done"
            self.__save_tasks(self.tasks)
            return task
        return None

    def list_tasks(self, status=None):
        # List all tasks
        if status:
            tasks = [task for task in self.tasks if task.status == status]
        else:
            tasks = self.tasks
        return tasks

    def get_task(self, task_id):
        # Get a task by id
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def dump_tasks(self):
        self.__save_tasks(self.tasks)

    def load_tasks(self):
        # Load tasks from the json file
        if not os.path.exists(self.__filename):
            print("File does not exist, creating new file")
            self.__save_tasks([])

        with open(self.__filename, "r") as f:
            tasks = json.load(f)
            tasks = [Task.from_dict(task) for task in tasks]
        return tasks
