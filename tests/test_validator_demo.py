import requests
from utils.validator import assert_status_in_range

def test_status_in_range():
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert_status_in_range(r,200,299)