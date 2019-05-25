with open('file_write.txt', 'w+') as f:
    f.write('Hello\n')
    f.write('This is test')
f.close()
f = open('file_write.txt', 'r')
print(f.read())

