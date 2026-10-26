numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]

print(list(set(numbers)))

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
