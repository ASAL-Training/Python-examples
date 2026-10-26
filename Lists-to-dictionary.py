keys = ["name", "city", "age"]
values = ["Zahi", "Nablus", 22]

print(dict(zip(keys, values)))

person = {}
for index in range(len(keys)):
    person[keys[index]] = values[index]

print(person)
