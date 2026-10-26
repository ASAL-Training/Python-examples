numbers = [10, 20, 30, 40, 50]
del numbers[1]
print(numbers)

numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

numbers = [10, 20, 30, 40, 50]
last = numbers.pop()
first = numbers.pop(0)
print(numbers)
print(last)
print(first)

numbers = [10, 20, 30]
del numbers[:]
print(numbers)
