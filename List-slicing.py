numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[2:5])
print(numbers[:4])
print(numbers[4:])
print(numbers[-3:])
print(numbers[::2])
print(numbers[1:7:2])
print(numbers[::-1])

copy = numbers[:]
copy[0] = 0
print(copy)
print(numbers)
