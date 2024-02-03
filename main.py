user_prompt = "Type, add, show, edit, or exit: "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)

        case 'edit':
            number = int(input("number of the todo to edit: "))
            number = number - 1
            existing_todo = todos[number]
            print(existing_todo)
            new_todo = input("update your todo")
            todos[number] = new_todo

        case 'exit':
            break

        case _:
            print("unknown command, try again.")

print("Bye!")

