from pathlib import Path
import pytest
from playwright.sync_api import expect

PRACTICE_URL = (Path(__file__).resolve().parent / "practice_page.html").as_uri()


def test_page_loads_correctly(page):
    """UI 断言进阶：验证页面加载后的各种状态"""
    page.goto(PRACTICE_URL)

    # 1. 页面标题（你已经会 to_have_title）
    expect(page).to_have_title("自动化练习页")

    # 2. 页面 URL 对不对（to_have_url：地址栏等于这个地址）
    expect(page).to_have_url(PRACTICE_URL)

    # 3. 搜索框是"可见"的（to_be_visible：元素在页面上显示出来）
    expect(page.locator("#search_box")).to_be_visible()

    # 4. 搜索按钮可见且可点
    expect(page.locator("#search_btn")).to_be_visible()

    # 5. 大标题文字正好是"自动化练习页"（to_have_text：精确相等）
    expect(page.locator("h1")).to_have_text("自动化练习页")

    # 6. 页面上 input 标签正好 1 个（to_have_count：数量断言）
    expect(page.locator("input")).to_have_count(1)

    expect(page.locator("#result")).to_have_text("等待输入")
