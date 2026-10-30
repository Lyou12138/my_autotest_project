from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)   # 启动无头浏览器
    page = browser.new_page()                    # 打开一个新页面

    # 1. 打开百度
    page.goto("https://www.baidu.com")

    # 2. 定位搜索框并输入内容
    #    page.locator("#kw")：找"id 为 kw 的元素"（百度搜索框，十几年没变过的稳定 ID）
    #    .fill("软件测试")：往输入框里填入文字
    search_box = page.locator("#kw")
    search_box.fill(search_box.fill("软件测试", force=True))

    # 3. 定位搜索按钮并点击
    #    page.locator("#su")：找"id 为 su 的元素"（百度"百度一下"搜索按钮）
    #    .click()：点它一下
    search_button = page.locator("#su")
    search_button.click()

    # 4. 等待页面跳转到结果页
    page.wait_for_load_state("networkidle")

    # 5. 打印结果页的标题，验证真的搜索成功了
    print("搜索后的标题:", page.title())

    browser.close()
