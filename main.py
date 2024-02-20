# App1 is a Todo list App
#

import time
curr_time = time.strftime("%H:%M:%S", time.localtime())
print("Current Time is :", curr_time)

userRegistry = []
TodoList = []
passKey = "novaboba"
username = ";lkadjf;akdfj;akfj"
password = "0-aifa;dfjadfja;lfj"
numtrys = 3


def Todo():
    print("1.\"add\": add a task to your list")
    print("2.\"show\": display all tasks")
    print("3.\"edit\": edit a task in your list")
    
    
    userAction = input("choose a action: ")
    match userAction:
        
        case "add":
            print("added successfully:")
        
        case "show":
            print("showing your Todo List:")
        
        case "edit":
            print("editted sucessfully")

    
    
    
def giveRegisterCount(userRegistry):
    
    count = userRegistry.len()
    return count
    
    
def registerUser(userRegistry):
    prompt_userName = input("what would you like your username to be? ")
    userRegistry = userRegistry.append(prompt_userName)
    print("Successfully Registered")
    return userRegistry
    

while username not in userRegistry:
    #check username is in registry
    username = input("Enter username:")

    if username in userRegistry:
        #go onto password    
        while password != passKey: 
            
            password = input("Enter password:")
            if password == passKey: 
                print("access granted..")
                Todo()
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
            
            
        



