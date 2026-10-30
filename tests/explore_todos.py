import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("状态码:",r.status_code)
print("返回内容：",r.json())