from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. 打开必应，等页面加载完
    page.goto("https://www.bing.com")
    page.wait_for_load_state("networkidle")

    # 2. 定位搜索框，填入关键词（必应搜索框 id 是 sb_form_q）
    search_box = page.locator("#sb_form_q")
    search_box.wait_for()            # 等搜索框真正可见（吸取上次教训）
    search_box.fill("软件测试")

    # 3. 用【回车】提交搜索（不依赖搜索按钮，最稳）
    page.keyboard.press("Enter")

    # 4. 断言：结果区 #b_results 里出现 "软件测试"
    #    expect 会自动等待，不用手动 sleep
    expect(page.locator("#b_results")).to_contain_text("软件测试")
    print("断言通过：结果区里找到了'软件测试'！")

    browser.close()
