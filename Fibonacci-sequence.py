def fibonacci(count):
    sequence = []
    current, following = 0, 1
    for _ in range(count):
        sequence.append(current)
        current, following = following, current + following
    return sequence


count = int(input("How many terms? "))

if count <= 0:
    print("Please enter a positive number")
else:
    print(fibonacci(count))
