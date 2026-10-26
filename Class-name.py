class Task:
    def __init__(self, title):
        self.title = title


task = Task("Read a book")
numbers = [1, 2, 3]
title = "Hello"

print(type(task).__name__)
print(task.__class__.__name__)
print(type(numbers).__name__)
print(title.__class__.__name__)
