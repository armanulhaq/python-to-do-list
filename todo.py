while True:
    user_input = input("Enter add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    match user_input:
        case "add":
            added_input = input("Enter a todo: ") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(added_input)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todo = file.readlines()

            for index, item in enumerate(todo):
                item = item.strip('\n')
                row = f"{index + 1}. {item}"
                print(row)

        case "edit":
            index_to_edit = int(input("Enter the index of the to do you want to edit: ")) - 1
            with open('todos.txt', 'r') as file:
                todo = file.readlines()
            edited_to_do = input("Enter what you want to write in place of that: ")
            todo[index_to_edit] = edited_to_do + '\n'

            # Write the updated todos list back to the file
            with open('todos.txt', 'w') as file:
                file.writelines(todo)

        case "complete":
            index_to_complete = int(input("Enter the index that you want to complete: "))
            with open('todos.txt', 'r') as file:
                todo = file.readlines()

            todo_to_remove = todo.pop(index_to_complete - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todo)

            print(f"{todo_to_remove.strip('\n')} has been removed.")
        case "exit":
            break;
print("Bye!")
