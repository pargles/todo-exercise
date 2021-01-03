from app.models import Todo
from app.services import DATABASE, add_todo, list_all_todos, delete_todo
# todo, mock DATABASE and reinitialize it on every test


def test_add_todos():
    new_todo1 = Todo(name="test1", priority=1)
    new_todo2 = Todo(name="test2", priority=2)
    new_todo3 = Todo(name="test3", priority=5)
    add_todo(new_todo1)
    add_todo(new_todo2)
    add_todo(new_todo3)
    assert len(DATABASE) == 3
    assert DATABASE[1].name == "test1"


def test_add_duplicated_todo():
    new_todo1 = Todo(name="test1", priority=1)
    try:
        add_todo(new_todo1)
        assert False
    except Exception:
        assert True


def test_delete_todo():
    previous_database_size = len(DATABASE)
    deleted_todo = delete_todo(2)
    new_database_size = len(DATABASE)
    assert deleted_todo
    assert new_database_size == previous_database_size - 1


def test_delete_invalid_todo():
    try:
        delete_todo(4)
        assert False
    except Exception:
        assert True


def test_list_current_todos():
    all_todos = list_all_todos(False)
    assert len(all_todos.current) > 0
    assert not all_todos.missing


def test_list_all_todos():
    all_todos = list_all_todos(True)
    expected_missing_todos = [2, 3, 4]
    assert len(all_todos.missing) > 0
    for missing_todo in expected_missing_todos:
        assert missing_todo in all_todos.missing
    assert len(all_todos.current) > 0


def test_add_invalid_priority():
    new_todo = Todo(name="test", priority=-1)
    add_todo(new_todo)
    assert DATABASE[new_todo.priority]
