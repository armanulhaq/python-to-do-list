while True:
    user_input = input("Enter add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    match user_input:
        case "add":
            added_input = input("Enter a todo: ") + '\n'
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(added_input)

            file= open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            for index, item in enumerate(todo):
                row = f"{index + 1}. {item}"
                print(row)
        case "edit":
            index_to_edit = int(input("Enter the index of the to do you want to edit: ")) - 1
            edited_to_do = input("Enter what you want to write in place of that: ")
            todo[index_to_edit] = edited_to_do
        case "complete":
            index_to_complete = int(input("Enter the index that you want to complete: "))
            todo.pop(index_to_complete - 1)
        case "exit":
            break;
print("Bye!")
