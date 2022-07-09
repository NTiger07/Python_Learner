person = {
    "name": "Favour",
    "age": 20,
    "address": "NGR"
}

person["name"] = "Olaleru"
print(person.get("name"))
# print(person.keys())
# print(person.values())

#for loop
for key, value in person.items():
    print(f"{key}: {value}")