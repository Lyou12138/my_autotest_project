"""接口版数据文件驱动：从 CSV 读 user_id 和期望名字，驱动 /users/{id} 接口测试"""
import csv
import os
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "users.csv")


def load_users():
    """从 CSV 读出所有 (user_id, expected_name)，返回列表"""
    with open(DATA_FILE, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return [(row["user_id"], row["expected_name"]) for row in reader]


@pytest.mark.parametrize("user_id, expected_name", load_users())
def test_get_user_from_file(user_id, expected_name):
    """按 id 查用户，断言返回的名字 == 文件里期望的名字"""
    r = requests.get(f"{BASE_URL}/users/{user_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == expected_name
