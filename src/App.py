while True:
    user_action = input("Type add, show,edi, complete or exit:")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit:"))
            number = number - 1
            new_todo = input("Enter new todo:")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of todo to complete:"))
            todos.pop(number - 1)
        case 'quit':
            break