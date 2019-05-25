n = int(input())
with open('file.txt', 'r+') as f:
    lines = f.readlines()
print('\n'.join(line for line in lines[-n:]))
