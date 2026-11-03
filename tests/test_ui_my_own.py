import pytest
from pathlib import Path
from playwright.sync_api import expect

PRACTICE_URL = (Path(__file__).resolve().parent / "practice_page.html").as_uri()

@pytest.mark.smoke
@pytest.mark.parametrize("key",[("性能测试"),("回归测试")])
def test_key_ui(page,key):
    page.goto(PRACTICE_URL)
    page.locator("#search_box").wait_for()
    page.locator("#search_box").fill(key)
    page.locator("#search_btn").click()
    expect(page.locator("#result")).to_contain_text(key)