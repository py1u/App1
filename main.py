# App1 is a Todo list App
#

import time

userRegistry = []
passKey = "novaboba"
username = ";lkadjf;akdfj;akfj"
password = "0-aifa;dfjadfja;lfj"
numtrys = 3


def Todo(prompt):
    print("choose a action: 1,2,3")
    print("1.Add: add a task to your list")
    print("2.Show: display all task")
    print("3.Edit: edit a task in your list")
    
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
                break
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
            
            
        



