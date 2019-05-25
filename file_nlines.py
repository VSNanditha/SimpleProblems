n = int(input())
with open('file.txt', 'r+') as f:
    for i in range(n):
        print(f.readline())
