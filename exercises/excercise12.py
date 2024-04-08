# 1. function that converts liters to cubic meters
def liters_to_m3(liters):
    cubic = liters / 1000
    return cubic


# 2. password checker from bonus 9

def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["uppercase"] = uppercase

    print(result.values())
    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"

# 3 calculates list of integers average

def average(list):
    sum_value = float(sum(list))

    num_values = float(len(list))

    avg = sum_value / num_values
    return avg

# 4 basic greet function

def greeting(person):
    greeting = f"Hi {person}"
    return greeting

# 5 basic string concatenate function

def concatenate(left_string, right_string):
    return left_string + right_string

# 6 proper grammer greeting

def greeting(person):
    person = person.title()
    greeting = f"Hi {person}"
    return greeting
