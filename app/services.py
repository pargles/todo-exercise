from app.models import Todo, AllTodos

# todo, add a lock to prevent race condition with async calls
# replicates a database
# key is the priority, assuming that priorities are unique
# but in a real application would probably be better to have an uuid
# and add the creation date to sort todos with the same priority
DATABASE: dict = {}


def add_todo(todo: Todo) -> Todo:
    if todo.priority not in DATABASE:
        DATABASE[todo.priority] = todo
        return todo
    else:
        raise Exception("Todo already exists")


def list_all_todos(include_missing_todos: bool) -> AllTodos:
    all_todos = AllTodos(current=[])
    all_todos.current = list(DATABASE.values())
    if include_missing_todos:
        existing_priorities = DATABASE.keys()
        if len(existing_priorities) > 0:
            highest_priority: int = max(existing_priorities)
            # assuming that priorities always start from 1
            range_of_priorities = range(1, highest_priority)
            # calculating the difference in both sets to find the missing ones
            missing_priorities = set(range_of_priorities) - set(existing_priorities)
            all_todos.missing = missing_priorities
    return all_todos


def delete_todo(priority: int) -> Todo:
    todo_to_be_deleted = DATABASE[priority]
    if todo_to_be_deleted is None:
        raise Exception("Todo doesn't exist")
    else:
        del DATABASE[priority]
        return todo_to_be_deleted
