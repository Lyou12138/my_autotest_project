"""
演示：practice_url 这个 fixture 只在 tests/ui 目录下能用。
这个用例在 ui 子目录里，所以能拿到 practice_url。
"""
from playwright.sync_api import expect


def test_practice_title(page, practice_url):
    """打开练习页，断言页面标题（practice_url 从本目录的 conftest 注入）"""
    page.goto(practice_url)
    expect(page).to_have_title("自动化练习页")
