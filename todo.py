todo = []
while True:
    print("Enter add, show or exit")
    user_input = input()
    user_input = user_input.strip()
    match user_input:
        case "add":
            add_input = input()
            todo.append(add_input)
        case "show":
            for item in todo:
                print(item)
        case "exit":
            break;
        case _:
            break;
print("Bye!")
