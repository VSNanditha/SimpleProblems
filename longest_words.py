with open('file.txt', 'r') as f:
    words = f.read().split()

max_length = len(max(words, key=len))
print('max length words: ', [word for word in words if len(word) == max_length])
