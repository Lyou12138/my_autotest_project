# my-autotest-project

Python + pytest 自动化测试项目，覆盖 **接口自动化（requests）+ UI 自动化（Playwright）+ 测试报告（pytest-html）+ CI 持续集成（GitHub Actions）**。

适合作为测试入门练手 / 作品集项目。

## 技术栈

| 模块 | 技术 | 说明 |
|---|---|---|
| 测试框架 | pytest | 用例收集、fixture、参数化、marker |
| 接口测试 | requests | 基于 jsonplaceholder 免费 API |
| UI 测试 | Playwright | 真实浏览器，必应搜索场景 |
| 测试报告 | pytest-html | 跑完自动生成 report.html |
| CI | GitHub Actions | push 后自动跑全部测试 |

## 目录结构

```
my_autotest_project/
├── .github/workflows/ci.yml   # CI 配置：push 后自动装环境、跑测试、传报告
├── api/                       # 接口封装层
│   ├── client.py              # HTTP 客户端基类（base_url、Session、get/post/put/delete）
│   ├── user_api.py            # 用户接口封装
│   ├── post_api.py            # 帖子接口封装
│   └── todo_api.py            # 待办接口封装
├── utils/
│   └── validator.py           # 通用断言工具（会"说人话"的断言）
├── tests/                     # 测试用例
│   ├── conftest.py            # 全局 fixture（API 客户端 + Playwright browser/page）
│   ├── test_user.py           # 用户接口测试
│   ├── test_post.py           # 帖子接口测试（CRUD 全覆盖）
│   ├── test_todo.py           # 待办接口测试（含参数化）
│   ├── test_ui_search.py      # UI 自动化用例（Playwright 必应搜索）
│   └── ...                    # 其余为学习过程的演示/练习脚本
├── requirements.txt           # 依赖
├── pytest.ini                 # pytest 配置（含报告参数）
└── README.md
```

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 安装 Playwright 的 Chromium 浏览器（UI 用例需要）
playwright install chromium

# 3. 运行全部测试（自动生成 report.html）
pytest

# 4. 只跑某个文件
pytest tests/test_user.py
pytest tests/test_ui_search.py -v

# 只跑冒烟用例
pytest -m smoke

# 只看用例列表
pytest --collect-only
```

## 测试报告

运行 `pytest` 后，项目根目录生成 `report.html`，双击即可打开，查看：

- 整体通过/失败统计
- 每个用例的耗时与结果
- 失败用例的完整报错

## CI（持续集成）

`.github/workflows/ci.yml` 配置：**每次 push 到 main 分支**，GitHub 自动：

1. 拉取代码（`actions/checkout`）
2. 安装 Python 3.12（`setup-python`）
3. 安装依赖（`pip install -r requirements.txt`）
4. 安装 Playwright 浏览器（`playwright install --with-deps chromium`）
5. 运行全部测试（`pytest`）
6. 上传测试报告（`actions/upload-artifact`）

在 GitHub 仓库 **Actions** 标签页可查看运行结果，绿色对勾即全部通过。

## 常见问题

| 报错 | 原因 | 解决 |
|---|---|---|
| `ModuleNotFoundError: No module named 'api'` | 项目根目录没在 sys.path | 在项目根目录执行 pytest |
| `playwright` 未找到 | 没装依赖 | `pip install -r requirements.txt` |
| 浏览器启动失败 | 没装 Playwright 浏览器 | `playwright install chromium` |
| UI 用例超时 | 页面加载慢 / 元素未出现 | 检查网络，或改用更稳定的断言点（如标题） |
