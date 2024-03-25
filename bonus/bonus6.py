goals = ["LeetCode easy 1 a day",
         "Network 5 people, and apply 10 jobs",
         "Work on Artr Login page"]

filenames = ["LeetCode.txt", "Network.txt", "Login.txt"]

for content, filename in zip(goals, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)