from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. 打开必应（Bing 对自动化脚本友好，国内可访问）
    page.goto("https://www.bing.com")
    page.wait_for_load_state("networkidle")   # 等页面加载完

    # 2. 探查页面上所有输入框：打印它们的 id、name、type
    #    locator("input, textarea")：找出所有 <input> 和 <textarea> 标签
    #    .count()：有几个；.nth(i)：取第 i 个；.get_attribute("xx")：读某个属性
    boxes = page.locator("input, textarea")
    print("页面上共有", boxes.count(), "个输入框：")
    for i in range(boxes.count()):
        el = boxes.nth(i)
        print(
            i,
            "| id =", el.get_attribute("id"),
            "| name =", el.get_attribute("name"),
            "| type =", el.get_attribute("type"),
        )

    # 3. 顺便打印页面标题，确认必应真的加载成功了
    print("页面标题:", page.title())

    browser.close()
