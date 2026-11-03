"""数据文件驱动示例：测试数据放在 CSV 文件里，代码从文件读，改数据不用改代码"""
import csv
import os
from pathlib import Path
import pytest
from playwright.sync_api import expect

# 本地练习页地址（动态：本机/CI 通用）
PRACTICE_URL = (Path(__file__).resolve().parent / "practice_page.html").as_uri()

# 数据文件路径：__file__ 是当前文件，../data/search_data.csv 相对它定位（不管在哪运行都对）
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "search_data.csv")


def load_keywords():
    """从 CSV 读取所有 keyword 列，返回一个列表"""
    with open(DATA_FILE, encoding="utf-8-sig") as f:   # utf-8-sig 自动剥掉开头的 BOM 隐藏字符
        reader = csv.DictReader(f)          # 按第一行当表头，读成字典
        return [row["keyword"] for row in reader]   # 取出每一行的 keyword


@pytest.mark.parametrize("keyword", load_keywords())
def test_search_from_file(page, keyword):
    """用数据文件里的关键词搜索，断言结果区包含该词"""
    page.goto(PRACTICE_URL)
    page.locator("#search_box").wait_for()
    page.locator("#search_box").fill(keyword)
    page.locator("#search_btn").click()
    expect(page.locator("#result")).to_contain_text(keyword)
