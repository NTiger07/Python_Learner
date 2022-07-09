def greet(name):
    print(f"Hello {name}")

greet("Favour")


def is_adult(age):
    return age >= 18

print(is_adult(20))
print(is_adult(15))


def convert_gender(gender = "unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"

print(convert_gender("m"))
print(convert_gender("f"))
