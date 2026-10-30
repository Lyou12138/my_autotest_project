"""
待办事项接口封装
"""
from .client import BaseClient


class TodoAPI(BaseClient):
    """待办接口"""

    def list_todos(self, userId=None):
        params = {"userId": userId} if userId else None
        return self.get("todos", params=params)

    def get_todo(self, todo_id):
        return self.get(f"todos/{todo_id}")

    def create_todo(self, data):
        return self.post("todos", json=data)

    def update_todo(self, todo_id, data):
        return self.put(f"todos/{todo_id}", json=data)

    def delete_todo(self, todo_id):
        return self.delete(f"todos/{todo_id}")
