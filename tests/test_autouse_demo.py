"""autouse fixture 演示：一个没被任何用例"请求"的 fixture，却会自动对每个用例生效"""
import pytest


@pytest.fixture(autouse=True)          # ← 关键：autouse=True，自动生效
def auto_timer():
    """每个用例自动执行：测试前打印、测试后打印（不用用例参数里写它）"""
    print("\n[前置] 每个用例开始前，自动跑到这里")
    yield                              # 暂停，让用例跑
    print("\n[后置] 每个用例结束后，自动跑到这里")


def test_one(auto_timer):
    print("  执行用例 test_one")
    assert 1 == 1


def test_two():
    print("  执行用例 test_two")
    assert 2 == 2
