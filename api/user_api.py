"""
用户相关接口封装
"""
from .client import BaseClient


class UserAPI(BaseClient):
    """用户接口"""

    def list_users(self, **params):
        return self.get("users", params=params)

    def get_user(self, user_id: int):
        return self.get(f"users/{user_id}")

    def create_user(self, data: dict):
        return self.post("users", json=data)

    def update_user(self, user_id: int, data: dict):
        return self.put(f"users/{user_id}", json=data)

    def delete_user(self, user_id: int):
        return self.delete(f"users/{user_id}")
