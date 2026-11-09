values = input().split()
numbers = []

for value in values:
    numbers.append(int(value))

largest = 0
for number in numbers:
    if number > largest:
        largest = number

print(largest)
