from playwright.sync_api import expect
import re

def test_bing_search_software_testing(page):
    """UI 用例1：在必应搜索"软件测试"，断言结果页标题包含关键词"""
    # ---- Arrange（准备）：启动浏览器，打开必应 ----
    page.goto("https://www.bing.com")

        # ---- Act（执行）：定位搜索框、输入、回车搜索 ----
    page.locator("#sb_form_q").wait_for()     # 等搜索框可见
    page.locator("#sb_form_q").fill("软件测试")  # 填关键词
    page.keyboard.press("Enter")              # 回车提交

        # ---- Assert（断言）：结果页标题包含关键词 ----
    expect(page).to_have_title(re.compile("软件测试"))

def test_bing_Search_playwright(page):
    page.goto("http://www.bing.com")

    page.locator("#sb_form_q").wait_for()
    page.locator("#sb_form_q").fill("playwright教程")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("playwright教程"))