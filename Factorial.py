def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"The factorial of {number} is {factorial(number)}")
