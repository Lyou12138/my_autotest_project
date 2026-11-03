import pytest
from playwright.sync_api import expect

def test_open_page(page , practice_url):
    page.goto(practice_url)
    expect(page.locator("#result")).to_have_text("等待输入")
    expect(page).to_have_title("自动化练习页")

def test_search_shows_result(page,practice_url):
    page.goto(practice_url)
    page.locator("#search_box").fill("性能测试")
    page.locator("#search_btn").click()
    expect(page.locator("#result")).to_contain_text("性能测试")

@pytest.mark.parametrize("key",["冒烟测试","性能测试","接口测试"])
def test_search_param(page,practice_url,key):
    page.goto(practice_url)
    page.locator("#search_box").fill(key)
    page.locator("#search_btn").click()
    expect(page.locator("#result")).to_contain_text(key)

def test_search_semantic(page,practice_url):
    page.goto(practice_url)
    page.get_by_placeholder("输入关键词").fill("语义化定位")
    page.get_by_role("button",name="搜索").click()
    expect(page.locator("#result")).to_contain_text("语义化定位")

def test_ui_assertions(page,practice_url):
    page.goto(practice_url)
    expect(page.locator("#search_btn")).to_be_visible()
    expect(page.get_by_role("button")).to_have_count(1)
    