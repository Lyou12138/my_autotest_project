import pytest

attempt = {"n" : 0}

@pytest.mark.flaky(reruns=2,reruns_dalay=1)
def test_flaky_demo():
    attempt["n"] += 1
    print(f"--> 这是第{attempt["n"]}次运行")

    if attempt["n"] == 1:
        raise AssertionError("第一次失败")

    assert True