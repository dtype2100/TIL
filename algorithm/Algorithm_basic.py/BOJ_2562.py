numbers = [int(input()) for i in range(9)]
max_number = max(numbers)
print(max_number, numbers.index(max_number) + 1, sep="\n")