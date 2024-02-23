# App1 is a Todo list App

TodoList = []
def doTodo():
    print("1.\"add\": add a task to your list")
    print("2.\"show\": display all tasks")
    print("3.\"edit\": edit a task in your list")
    
    
    userAction = input("choose a action: ")
    match userAction:
        
        case "add":
            todo = input("enter a task: ")
            TodoList.append(todo)
            print("added successfully:")
        
        case "show":
            print("showing your Todo List:")
            print(TodoList)
            
        
        case "edit":
            index = int(input("what todo would you like to change?"))
            new_todo = input("what do you want to change it to?")
            TodoList[index] = new_todo
            print("editted sucessfully")

    
    
    
def giveRegisterCount(userRegistry):
    
    count = userRegistry.len()
    return count
    
    
def registerUser(userRegistry):
    prompt_userName = input("what would you like your username to be? ")
    userRegistry = userRegistry.append(prompt_userName)
    print("Successfully Registered")
    return userRegistry
    

def todoAuth():
    #creation during auth
    userRegistry = []
    username = ''
    numtrys = 3
    userAuth = False;
    passAuth = False;
    passKey = "bobanova"
    
    while userAuth == False:
        
        username = input("Enter username:")

        if username in userRegistry:
            userAuth = True
            
            while passAuth == False: 
                
                password = input("PassKey:")
                if password == passKey: 
                    print("access granted..")
                    doTodo()
                    passAuth = True
                elif password != passKey: 
                    
                    if numtrys == 0:
                        print("maximum attempts reached. access locked")
                        quit()
                        
                    print(f"access denied.\n you have {numtrys} left.")
                    numtrys -= 1
                    
                    
        else:
            print("user has not been registered.")
            reg_choice = input("would you like to add a user to the registry?(y/n) ")
            if reg_choice == 'y':
                registerUser(userRegistry)
            
            
#call auth for todo app start
print("Starting App..\n")
todoAuth()



