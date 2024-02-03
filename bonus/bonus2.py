import time

filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:

    # three-second delay
    time.sleep(3)
    print(filename)