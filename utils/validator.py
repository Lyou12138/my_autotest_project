"""
通用断言工具
比 assert 更强大：能生成清晰的错误信息
"""


def assert_status_code(response, expected: int):
    """断言 HTTP 状态码"""
    assert response.status_code == expected, (
        f"期望状态码 {expected}, 实际 {response.status_code}, "
        f"URL: {response.url}, 响应: {response.text[:200]}"
    )


def assert_json_field(response, path: str, expected=None):
    """
    断言 JSON 响应中的某个字段
    path 用点分隔：'user.name' 表示 data.user.name
    """
    data = response.json()
    current = data
    for key in path.split("."):
        if isinstance(current, list):
            current = current[int(key)]
        else:
            assert key in current, f"响应中缺少字段: {path} (实际字段: {list(current.keys())})"
            current = current[key]

    if expected is not None:
        assert current == expected, f"字段 {path} 期望 {expected}, 实际 {current}"


def assert_not_empty(response, field: str = None):
    """断言响应体非空，或指定字段非空"""
    data = response.json()
    if field:
        assert data.get(field), f"字段 {field} 为空"
    else:
        assert data, "响应体为空"


def assert_contains(response, substring: str):
    """断言响应体包含某个字符串"""
    assert substring in response.text, f"响应不包含: {substring}"

def assert_status_in_range(response, min_code: int, max_code: int):
    """断言状态码落在 [min_code, max_code] 闭区间内"""
    code = response.status_code
    assert min_code <= code <= max_code, (
        f"状态码 {code} 不在 [{min_code}, {max_code}] 区间内"
    )

