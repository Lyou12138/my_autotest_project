"""
帖子接口测试
覆盖：查询列表、查询详情、创建、更新、删除（CRUD 全覆盖）
"""
import pytest
from utils.validator import assert_status_code, assert_json_field


class TestPostList:
    """帖子列表相关测试"""

    @pytest.mark.smoke
    @pytest.mark.post
    def test_list_posts_success(self, post_api):
        """查询帖子列表成功"""
        r = post_api.list_posts()
        assert_status_code(r, 200)
        posts = r.json()
        assert isinstance(posts, list)
        assert len(posts) == 100, f"jsonplaceholder 应返回 100 条帖子, 实际 {len(posts)}"

    @pytest.mark.post
    def test_list_posts_by_user(self, post_api):
        """按用户查询帖子"""
        r = post_api.list_posts(userId=1)
        assert_status_code(r, 200)
        posts = r.json()
        assert len(posts) == 10, "用户 1 应有 10 条帖子"
        for post in posts:
            assert post["userId"] == 1


class TestPostDetail:
    """帖子详情相关测试"""

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    @pytest.mark.post
    def test_get_post_success(self, post_api, post_id):
        """查询帖子详情成功"""
        r = post_api.get_post(post_id)
        assert_status_code(r, 200)
        assert_json_field(r, "id", post_id)
        assert_json_field(r, "title")
        assert_json_field(r, "body")
        assert_json_field(r, "userId")


class TestPostCreate:
    """帖子创建相关测试"""

    @pytest.mark.post
    def test_create_post_success(self, post_api, sample_post):
        """创建帖子成功"""
        r = post_api.create_post(sample_post)
        # POST 创建资源，REST 规范返回 201 Created（不是 200）
        assert_status_code(r, 201)
        data = r.json()
        assert "id" in data, "创建成功后应返回 id"
        assert data["title"] == sample_post["title"]
        assert data["userId"] == sample_post["userId"]

    @pytest.mark.post
    @pytest.mark.parametrize("invalid_data", [
        {},                          # 空对象
        {"title": ""},              # 缺少 body
        {"userId": 1, "title": "仅标题"},  # 缺少 body
    ])
    def test_create_post_invalid(self, post_api, invalid_data):
        """创建帖子失败场景（数据不完整）"""
        r = post_api.create_post(invalid_data)
        # jsonplaceholder 不校验字段，一律返回 201；真实业务应返回 400
        assert r.status_code in (201, 400), f"意外状态码: {r.status_code}"


class TestPostUpdate:
    """帖子更新相关测试"""

    @pytest.mark.post
    def test_update_post_success(self, post_api):
        """更新帖子成功"""
        update_data = {"id": 1, "userId": 1, "title": "更新后的标题", "body": "更新后的内容"}
        r = post_api.update_post(1, update_data)
        assert_status_code(r, 200)
        assert r.json()["title"] == "更新后的标题"


class TestPostDelete:
    """帖子删除相关测试"""

    @pytest.mark.post
    def test_delete_post_success(self, post_api):
        """删除帖子成功"""
        r = post_api.delete_post(1)
        assert_status_code(r, 200)
        # 删除后再查询，jsonplaceholder 仍返回 200 空对象
        r2 = post_api.get_post(1)
        assert r2.status_code in (200, 404)
