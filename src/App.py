while True:
    user_action = input("Type add, show, edit, complete, or quit: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)
        case 'edit':

            number = int(input("Number of todo to edit:"))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # print("here is todos existing", todos)

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            # print("Here is how it will be", todos)
        case 'complete':

            number = int(input("Number of todo to complete:"))
            todos.pop(number - 1)
        case 'quit':
            print("Bye!")
            break