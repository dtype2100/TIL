n = int(input())
numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

for number in sorted(numbers):
    print(number)
