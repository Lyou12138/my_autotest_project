"""
tests/ui/conftest.py —— 【局部 conftest，当前为空】
说明：原来这里的 practice_url 局部 fixture 已经【上提到全局 tests/conftest.py】了。

为什么上提？因为现在不只 ui 子目录的用例要用练习页地址，
tests 根目录的 test_ui_my_own.py / test_ui_datafile.py / test_ui_assert_more.py 也要用。
"用的人变多了" → 它就不再是"只属于 ui 子目录"的东西 → 放全局更合理。

这跟之前学的规则完全一致：谁用得到、用的人多，就放到哪个层级。
本文件保留，作为"局部 conftest 可以存在"的结构占位（以后 ui 专属的 fixture 放这）。
"""
