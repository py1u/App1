# day 5 debugging problems

# 1
# menu = ["pasta", "pizza", "salad"]
# user_choice = int(input("Enter the index of the item: "))
# message = f"You chose {menu[user_choice]}."
# print(message)
# error was in the user_choice where we passed in a index of str instead of int.
# solution fixed with a int() method around input()

# 2
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print(f"{i}.{j}")
# error was that enumerate is a method () but had [] instead

# 3
menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")
# error was that f string 'f' was inside the quotes when it should be placed outside and before " "

