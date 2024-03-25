new_member = input("Add a new member: ")
file = open('../files/members.txt', 'w')
file.write(new_member)