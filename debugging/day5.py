menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)
# error was in the user_choice where we passed in a index of str instead of int.
# solution fixed with a int() method around input()

