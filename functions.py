def get_todos(filename):
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        return todos

def write_todos(filename, todos):
    with open('todos.txt', 'w') as file:
            file.writelines(todos)
