filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f'../files/{filename}'append, 'w')
    file.write('Hello')
    file.close()
