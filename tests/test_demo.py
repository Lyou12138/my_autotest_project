import requests

def test_get_user_status():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert r.status_code == 200

def test_get_post_status():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert r.status_code == 200

def test_user_post_status():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = r.json()
    assert "name" in data