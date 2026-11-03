import pytest
from playwright.sync_api import expect

PRACTICE_URL = "file:///C:/Users/myages2026/WorkBuddy/2026-10-17-14-39-35/outputs/my_autotest_project/tests/practice_page.html"

@pytest.mark.smoke
@pytest.mark.parametrize("key",[("性能测试"),("回归测试")])
def test_key_ui(page,key):
    page.goto(PRACTICE_URL)
    page.locator("#search_box").wait_for()
    page.locator("#search_box").fill(key)
    page.locator("#search_btn").click()
    expect(page.locator("#result")).to_contain_text(key)