from datetime import datetime


class Task:
    """
    A class to represent a task from tasklist

    id: A unique identifier for the task
    description: A short description of the task
    status: The status of the task (todo, in-progress, done)
    createdAt: The date and time when the task was created
    updatedAt: The date and time when the task was last updated

    """

    def __init__(self, id, description, status, createdAt=None, updatedAt=None):
        self.id = id
        self.description = description
        self.status = status
        if createdAt is None:
            createdAt = datetime.now()
        if updatedAt is None:
            updatedAt = datetime.now()
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ["todo", "in-progress", "done"]:
            raise ValueError("Invalid status")
        self._status = value
        self.updatedAt = datetime.now()

    def __str__(self):
        return f"Task {self.id}: {self.description} ({self.status})"

    def __repr__(self):
        return f"Task {self.id}: {self.description} ({self.status})"

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            description=data["description"],
            status=data["status"],
            createdAt=data["createdAt"],
            updatedAt=data["updatedAt"],
        )
