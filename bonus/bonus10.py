try:
    width = float(input("Enter a rectangle width: "))
    length = float(input("Enter a rectangle length: "))
    if width == length:
        exit("That looks like a square.")
    area = width * length
    print(f"Rectangle area is: {area}")
except ValueError:
    print("Please enter a number.")
