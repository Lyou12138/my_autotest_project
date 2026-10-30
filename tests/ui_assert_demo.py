from playwright.sync_api import sync_playwright, expect   # 注意：多导入了 expect（断言工具）

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. 打开百度
    page.goto("https://www.baidu.com")
    page.locator("#kw").wait_for()

    # 2. 定位搜索框、输入、点击（你已经会了，直接照抄）
    page.locator("#kw").fill("软件测试")
    page.locator("#su").click()

    # 注意：这里我们【故意不写】 wait_for_load_state
    #       因为下面要用的 expect 会自己等元素出现（自动等待）！

    # ================= 下面 2 行留给你自己敲 =================
    # 第 1 行：断言结果区 #content_left 里出现 "百度百科"
    #   提示：expect(page.locator("#content_left")).to_contain_text("百度百科")
    #
    # 第 2 行：打印 "断言通过！"
    # =========================================================
    expect(page.locator("#content_left")).to_contain_text("百度百科")
    print("断言通过！")

    browser.close()
