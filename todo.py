todo = []
while True:
    print("Enter add, show, edit or exit")
    user_input = input()
    user_input = user_input.strip()
    match user_input:
        case "add":
            add_input = input()
            todo.append(add_input)
        case "show":
            for index, item in enumerate(todo):
                row = f"{index}. {item}"
                print(row)
        case "edit":
            index_to_edit = int(input("Enter the index of the to do you want to edit: ")) -1
            edited_to_do = input("Enter what you want to write in place of that: ")
            todo[index_to_edit] = edited_to_do
        case "exit":
            break;
print("Bye!")
