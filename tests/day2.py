# import requests

# def test_get_user():
#     url = "https://jsonplaceholder.typicode.com/users/1"
#     # 发送一个get请求
#     response = requests.get(url)

#     assert response.status_code == 200, "状态码不是 200"

#     data = response.json()
 
#     assert "name" in data, "缺少name字段"
#     assert "email" in data, "缺少email字段"

#     print("测试通过")
#     print(f"用户名:{data['name']}")
#     print(f"邮箱：{data['email']}")

# test_get_user()
