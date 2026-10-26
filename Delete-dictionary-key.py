person = {"name": "Zahi", "city": "Nablus", "age": 22}

key = input("Which key do you want to delete? ")

if key in person:
    del person[key]
    print(f"'{key}' was deleted")
else:
    print(f"'{key}' does not exist")

print(person)

removed = person.pop("age", None)
print(removed)
print(person)
