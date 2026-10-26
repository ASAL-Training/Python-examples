first = {"name": "Zahi", "city": "Nablus"}
second = {"city": "Ramallah", "age": 22}

merged = {**first, **second}
print(merged)

copied = first.copy()
copied.update(second)
print(copied)

print(first)
print(second)
