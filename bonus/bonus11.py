def get_average_temp():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]
        print(values)
        average = sum(values) / len(values)
        return average


average_local = get_average_temp()
print(average_local)
