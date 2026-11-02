"""
性能测试入门脚本（locust）
用 locust 模拟多个用户并发访问 jsonplaceholder 的 /users 接口，
统计响应时间、吞吐量、失败率。
"""
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    # wait_time：每个用户【两次请求之间】等多久（这里是随机 1~3 秒）
    # 作用：模拟真实用户"不是每毫秒都在狂点"，更接近现实
    wait_time = between(1, 3)

    @task
    def get_users(self):
        # 一个"任务"：用户做的一件事。这里就是 GET /users
        self.client.get("/users")
