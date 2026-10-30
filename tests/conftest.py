"""
pytest 全局配置
所有 fixture 定义在这里，同目录及子目录下的用例自动可见
"""
import pytest
from api.client import BaseClient
from api.user_api import UserAPI
from api.post_api import PostAPI
from api.todo_api import TodoAPI
from playwright.sync_api import sync_playwright


# 环境配置
BASE_URL = "https://jsonplaceholder.typicode.com"


# ---------- Session 级别 fixture（整个测试会话只创建一次） ----------
@pytest.fixture(scope="session")
def base_url():
    """基础 URL"""
    return BASE_URL


@pytest.fixture(scope="session")
def http():
    """
    通用 HTTP 客户端
    返回一个 BaseClient 实例，测试中直接用 http.get/post 即可
    """
    client = BaseClient(
        base_url=BASE_URL,
        headers={"Content-Type": "application/json"},
    )
    yield client
    client.close()


@pytest.fixture(scope="session")
def user_api(http):
    """用户接口封装"""
    return UserAPI(base_url=http.base_url, headers=http.session.headers)


@pytest.fixture(scope="session")
def post_api(http):
    """帖子接口封装"""
    return PostAPI(base_url=http.base_url, headers=http.session.headers)


@pytest.fixture(scope="session")
def todo_api(http):
    """待办接口封装"""
    return TodoAPI(base_url=http.base_url, headers=http.session.headers)


# ---------- Function 级别 fixture（每个用例独立） ----------
@pytest.fixture
def sample_user():
    """
    样本用户数据
    实际项目中从数据库或配置文件读取
    """
    return {
        "name": "张三",
        "email": "zhangsan@example.com",
        "phone": "13800138000",
        "address": {
            "city": "北京",
            "street": "长安街 1 号",
        },
    }


@pytest.fixture
def sample_post():
    """样本帖子数据"""
    return {
        "userId": 1,
        "title": "测试帖子",
        "body": "这是一个自动化测试创建的帖子",
    }


# ---------- UI 自动化 fixture（Playwright） ----------
@pytest.fixture(scope="session")
def browser():
    """
    启动一个无头浏览器，整个测试会话【只启动一次】，所有用例共用
    yield：先把浏览器交给用例用；所有用例跑完后，回到这里关浏览器
    """
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        yield b
        b.close()


@pytest.fixture
def page(browser):
    """
    每个用例【各自开一个新页面】（默认 function 级别），用例之间互不干扰
    用例函数参数里写 page，pytest 会自动注入；用例跑完自动关页面
    """
    pg = browser.new_page()
    yield pg
    pg.close()
