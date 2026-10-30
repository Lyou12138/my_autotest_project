"""
帖子相关接口封装
"""
from .client import BaseClient


class PostAPI(BaseClient):
    """帖子接口"""

    def list_posts(self, userId: int = None):
        params = {"userId": userId} if userId else None
        return self.get("posts", params=params)

    def get_post(self, post_id: int):
        return self.get(f"posts/{post_id}")

    def create_post(self, data: dict):
        return self.post("posts", json=data)

    def update_post(self, post_id: int, data: dict):
        return self.put(f"posts/{post_id}", json=data)

    def delete_post(self, post_id: int):
        return self.delete(f"posts/{post_id}")
