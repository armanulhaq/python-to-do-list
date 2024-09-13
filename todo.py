while True:
    user_input = input("Enter add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        added_input = user_input[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(added_input + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_input.startswith('show'):
        with open('todos.txt', 'r') as file:
            todo = file.readlines()

        for index, item in enumerate(todo):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_input.startswith('edit'):
        index_to_edit = int(user_input[5:]) - 1
        with open('todos.txt', 'r') as file:
            todo = file.readlines()
        edited_to_do = input("Enter what you want to write in place of that: ")
        todo[index_to_edit] = edited_to_do + '\n'

        # Write the updated todos list back to the file
        with open('todos.txt', 'w') as file:
            file.writelines(todo)

    elif user_input.startswith('complete'):
        index_to_complete = int(user_input[9:])
        with open('todos.txt', 'r') as file:
            todo = file.readlines()

        todo_to_remove = todo.pop(index_to_complete - 1)

        with open('todos.txt', 'w') as file:
            file.writelines(todo)

        print(f"{todo_to_remove.strip('\n')} has been removed.")

    elif user_input.startswith('exit'):
        break;

    else:
        print("Invalid response")
print("Bye!")
