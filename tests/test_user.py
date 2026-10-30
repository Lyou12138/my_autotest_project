"""
用户接口测试
覆盖：查询列表、查询详情、按字段过滤
"""
import pytest
from utils.validator import assert_status_code, assert_json_field


class TestUserList:
    """用户列表相关测试"""

    @pytest.mark.smoke
    @pytest.mark.user
    def test_list_users_success(self, user_api):
        """查询用户列表成功"""
        r = user_api.list_users()
        assert_status_code(r, 200)
        assert isinstance(r.json(), list), "返回应为列表"
        assert len(r.json()) >= 10, "返回数量应至少 10 条"

    @pytest.mark.skip(reason="jsonplaceholder 不支持 name 查询参数，实测返回空列表")
    @pytest.mark.user
    def test_list_users_with_query(self, user_api):
        """按条件查询用户（该接口实际不支持 name 过滤，保留用例作为占位）"""
        r = user_api.list_users(name="Leanne")
        assert_status_code(r, 200)
        assert len(r.json()) >= 1, "查询应有结果"

    @pytest.mark.user
    def test_list_users_response_fields(self, user_api):
        """响应字段完整性校验"""
        r = user_api.list_users()
        assert_status_code(r, 200)
        user = r.json()[0]
        required_fields = ["id", "name", "email", "phone", "website", "address", "company"]
        for f in required_fields:
            assert f in user, f"缺少字段: {f}"


class TestUserDetail:
    """用户详情相关测试"""

    @pytest.mark.parametrize("user_id, expected_id", [
        (1, 1),
        (2, 2),
        (10, 10),
    ])
    @pytest.mark.user
    def test_get_user_success(self, user_api, user_id, expected_id):
        """查询用户详情成功（参数化）"""
        r = user_api.get_user(user_id)
        assert_status_code(r, 200)
        assert_json_field(r, "id", expected_id)
        assert_json_field(r, "name")
        assert_json_field(r, "email")

    @pytest.mark.user
    @pytest.mark.parametrize("user_id", [9999, 99999])
    def test_get_user_not_found(self, user_api, user_id):
        """查询不存在的用户"""
        r = user_api.get_user(user_id)
        # jsonplaceholder 对不存在的资源返回 200 空对象，实际项目中应该是 404
        # 这里做兼容处理
        assert r.status_code in (200, 404), f"状态码应为 200 或 404, 实际 {r.status_code}"
