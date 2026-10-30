# import requests
# def test_user_1():
#     r = requests.get("https://jsonplaceholder.typicode.com/users/1")
#     assert r.status_code == 200

# def test_user_2():
#     r = requests.get("https://jsonplaceholder.typicode.com/users/2")
#     assert r.status_code == 200

# def test_user_3():
#     r = requests.get("https://jsonplaceholder.typicode.com/users/3")
#     assert r.status_code == 200

# import pytest
# import requests

# @pytest.mark.parametrize("user_id",[1,2,3,4,5])
# def test_get_user(user_id):
#     r = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
#     assert r.status_code == 200

import pytest
import requests

@pytest.mark.parametrize("user_id,expected_name",[ (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
    ])
def test_get_user_name(user_id,expected_name):
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    data = r.json()
    assert data["name"] == expected_name