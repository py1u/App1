new_member = input("Add a new member: ")

file = open('../files/members.txt', 'r')
content = file.readlines()
file.close()

content.append(new_member + '\n')


file = open('../files/members.txt', 'w')
content = file.writelines(content)
file.close()
