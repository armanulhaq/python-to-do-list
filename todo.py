def get_todos(filename):
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        return todos

def write_todos(filename, todos):
    with open('todos.txt', 'w') as file:
            file.writelines(todos)

while True:
    user_input = input("Enter add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        added_input = user_input[4:]

        todo = get_todos('todos.txt')
        todo.append(added_input + '\n')

        write_todos('todos.txt', todo)

    elif user_input.startswith('show'):

        todo = get_todos('todos.txt')

        for index, item in enumerate(todo):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            index_to_edit = int(user_input[5:]) - 1

            todo = get_todos('todos.txt')

            edited_to_do = input("Enter what you want to write in place of that: ")
            todo[index_to_edit] = edited_to_do + '\n'

            # Write the updated todos list back to the file
            write_todos('todos.txt',todo)

        except ValueError:
            print("Invalid Command")
            continue

    elif user_input.startswith('complete'):
        try:
            index_to_complete = int(user_input[9:])
            todo = get_todos('todos.txt')
            todo_to_remove = todo.pop(index_to_complete - 1)

            write_todos('todos.txt', todo)

            print(f"{todo_to_remove.strip('\n')} has been removed.")
        except IndexError:
            print("Invalid index")
            continue

    elif user_input.startswith('exit'):
        break;

    else:
        print("Invalid response")
print("Bye!")
