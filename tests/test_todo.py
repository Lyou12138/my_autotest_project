"""
待办事项接口测试
覆盖：列表、详情（参数化）、创建
"""
import pytest
from utils.validator import assert_status_code, assert_json_field


class TestTodo:
    """待办接口测试"""

    @pytest.mark.smoke
    def test_list_todos(self, todo_api):
        """查询待办列表"""
        r = todo_api.list_todos()
        assert_status_code(r, 200)
        assert isinstance(r.json(), list), "返回应为列表"

    @pytest.mark.parametrize("todo_id", [1, 50, 100])
    def test_get_todo(self, todo_api, todo_id):
        """查询待办详情（参数化）"""
        r = todo_api.get_todo(todo_id)
        assert_status_code(r, 200)
        assert_json_field(r, "id", todo_id)

    def test_create_todo(self, todo_api):
        """创建待办"""
        data = {"userId": 1, "title": "学习自动化测试", "completed": False}
        r = todo_api.create_todo(data)
        # POST 创建资源，REST 规范返回 201 Created
        assert_status_code(r, 201)
        assert_json_field(r, "title", "学习自动化测试")
