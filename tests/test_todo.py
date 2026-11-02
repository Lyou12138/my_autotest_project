import pytest
from utils.validator import assert_status_code,assert_json_field

class TestTodo:
    @pytest.mark.smoke
    def test_list_todos(self, todo_api):
        r = todo_api.list_todos()
        assert_status_code(r,200)
        assert isinstance(r.json(),list)

    @pytest.mark.parametrize("todo_id",[1,50,100])
    def test_get_todo(self,todo_api,todo_id):
        r = todo_api.get_todo(todo_id)
        assert_status_code(r,200)
        assert_json_field(r,"id",todo_id)

    def test_create_todo(self,todo_api):
        data={"userId":1,"title":"自动化","completed":False}
        r = todo_api.create_todo(data)
        assert_status_code(r,201)
        assert_json_field(r,"title","自动化")