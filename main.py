# App1 is a Todo list App

TodoList = []
def doTodo():
    print("add, show, edit, or quit")
    
    runTodo = True   
    while runTodo != False:
        #ask for user action
        userAction = input("\nchoose a action: ")
        
        match userAction:
            
            case "add":
                todo = input("enter a task: ")
                TodoList.append(todo)
                print("added successfully")
            
            case "show":
                print("showing your Todo List:")
                i = 0
                for todo_at in TodoList:
                    print(TodoList[i])
                    i+= 1
                
            
            case "edit":
                validIndex = False
                while validIndex == False:
                    index = int(input("which todo would you like to change? "))
                    if index > len(TodoList) or index < len(TodoList) or index == 0:
                        validIndex = True
                        new_todo = input("enter replacement task: ")
                        TodoList[index - 1] = new_todo
                        print("edited sucessfully")
                    else:
                        print("index supplied not in range, try again.")
            
            case "quit":
                print("program exiting..")
                runTodo = False
                quit()
                
            case _ :
                print("invalid input try again.")
                
            

    
    
    
# def giveRegisterCount(userRegistry):
    
#     count = userRegistry.len()
#     return count
    
    
# def registerUser(userRegistry):
#     prompt_userName = input("what would you like your username to be? ")
#     userRegistry = userRegistry.append(prompt_userName)
#     print("Successfully Registered")
#     return userRegistry
    

# def todoAuth():
#     #creation during auth
#     userRegistry = []
#     username = ''
#     numtrys = 3
#     userAuth = False;
#     passAuth = False;
#     passKey = "bobanova"
    
#     while userAuth == False:
        
#         username = input("Enter username:")

#         if username in userRegistry:
#             userAuth = True
            
#             while passAuth == False: 
                
#                 password = input("PassKey:")
#                 if password == passKey: 
#                     print("access granted..")
#                     doTodo()
#                     passAuth = True
#                 elif password != passKey: 
                    
#                     if numtrys == 0:
#                         print("maximum attempts reached. access locked")
#                         quit()
                        
#                     print(f"access denied.\n you have {numtrys} left.")
#                     numtrys -= 1
                    
                    
        # else:
        #     print("user has not been registered.")
        #     reg_choice = input("would you like to add a user to the registry?(y/n) ")
        #     if reg_choice == 'y':
        #         registerUser(userRegistry)
            
            
#call auth for todo app start
print("Starting App..\n")
doTodo()
#todoAuth()



