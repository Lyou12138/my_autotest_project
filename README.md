# my-autotest-project

自动化测试入门练手项目（基于 Python + pytest + requests）

## 目录结构

```
my_autotest_project/
├── tests/                # 测试用例
│   ├── conftest.py      # pytest 全局配置（fixture 定义在这里）
│   ├── test_user.py     # 用户相关接口测试
│   └── test_post.py     # 帖子相关接口测试（CRUD 全覆盖）
├── api/                  # 接口封装层
│   ├── client.py        # HTTP 客户端基类（支持 base_url、重试、Session）
│   ├── user_api.py      # 用户接口封装
│   └── post_api.py      # 帖子接口封装
├── utils/                # 工具层
│   └── validator.py     # 通用断言工具（比 assert 更清晰）
├── requirements.txt      # 依赖列表
├── pytest.ini            # pytest 配置
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试

在项目根目录执行：

```bash
# 运行所有用例
pytest

# 只看用例列表，不执行
pytest --collect-only

# 只跑冒烟用例
pytest -m smoke

# 只跑某个文件
pytest tests/test_user.py

# 只跑某个用例
pytest tests/test_user.py::TestUserDetail::test_get_user_success

# 关键字筛选
pytest -k "list"

# 详细输出
pytest -vv
```

### 3. 生成 Allure 报告（可选）

```bash
# 生成 allure 原始数据
pytest --allure-features-dir=features

# 生成 HTML 报告（需要先安装 allure 命令行）
allure generate allure-results -o allure-report --clean

# 打开报告
allure open allure-report
```

## 项目学习路径

- **Day 1-2**：读懂 `api/client.py`，理解 HTTP 请求是怎么被封装的
- **Day 3-5**：读懂 `tests/conftest.py`，理解 fixture 的分层与作用域
- **Day 6-8**：读 `test_user.py` 和 `test_post.py`，学习断言的写法
- **Day 9-10**：给项目新增一个业务模块的测试用例
- **Day 11-15**：把项目改造成一个真实的接口自动化框架

## 拓展练习

1. **添加新业务模块**：给 `todos` 接口写完整 CRUD 用例
2. **多环境切换**：把 `BASE_URL` 抽到 `config.yaml`，通过环境变量切换
3. **数据库校验**：创建帖子后查询数据库验证
4. **性能监控**：记录每个用例耗时，输出到报告
5. **接入 CI**：用 GitHub Actions 每天定时跑一次

## 常见问题

| 报错 | 原因 | 解决 |
|---|---|---|
| `ModuleNotFoundError: No module named 'api'` | 项目根目录没在 sys.path | 在项目根目录执行 pytest，或在 `conftest.py` 加 `sys.path.append(os.getcwd())` |
| `ConnectionError` | 网络问题 | 检查网络或换 base_url |
| `AssertionError: 期望 200, 实际 500` | 接口挂了 | 先看具体响应，改断言 |
