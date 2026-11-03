"""
tests/ui/conftest.py —— 【局部】fixture
重要：这个 conftest 只对【tests/ui 目录】下的用例生效，
它对 tests 根目录（比如 tests/test_ui_my_own.py）是【不可见】的。

这跟 tests/conftest.py 不同：那个是全局（对整个 tests 及子目录生效）。
"""
import pytest


@pytest.fixture
def practice_url():
    """
    本地练习页地址（只给 UI 子目录的用例用）
    之所以放这里不放全局：这个地址只跟 UI 测试有关，跟接口测试无关。
    接口测试不需要"页面地址"，放全局会让所有用例都背着一个用不上的东西。
    """
    return "file:///C:/Users/myages2026/WorkBuddy/2026-10-17-14-39-35/outputs/my_autotest_project/tests/practice_page.html"
