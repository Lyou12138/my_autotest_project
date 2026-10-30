from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. 打开必应
    page.goto("https://www.bing.com")

    # 2. 等搜索框真正可见（吸取上次教训：等元素可见再操作，最稳）
    page.locator("#sb_form_q").wait_for()

    # 3. 定位搜索框、填关键词、点搜索按钮
    #    选择器来自刚才探查到的真实 id：sb_form_q / sb_form_go
    page.locator("#sb_form_q").fill("软件测试")
    page.keyboard.press("Enter")

    # 4. 断言：结果页【标题】包含"软件测试"
    #    为什么不断言结果区文本？必应中文版会对部分结果做法律合规过滤，
    #    结果区可见文本不稳定；但标题一定包含搜索词，更可靠。
    #    re.compile(...) 是"正则"，这里表示"包含"匹配
    expect(page).to_have_title(re.compile("软件测试"))

    # 5. 打印结果页标题，双重确认
    print("断言通过！搜索结果页标题:", page.title())

    browser.close()
