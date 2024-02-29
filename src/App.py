todos = []

while True:
    user_action = input("Type add, show,edit or exit:")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)