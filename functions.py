def get_todos(filename='todos.txt'):
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        return todos

def write_todos(todos, filename='todox.txt'):
    with open('todos.txt', 'w') as file:
            file.writelines(todos)
