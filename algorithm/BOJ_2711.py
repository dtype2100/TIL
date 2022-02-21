t = int(input())

for i in range(t):
    index, word = input().split()
    index = int(index)
    changed_word = word[0:index-1] + word[index:]
    print(changed_word)