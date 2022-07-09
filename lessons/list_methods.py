cars = ["Audi", "Ferrari", "Buga'i", "Lamborghini", "Tesla", "Toyota"]

cars.append("BMW")
print(len(cars))
print(cars)

cars.sort()
print(cars)

cars.reverse()
print(cars)
print("Audi" in cars)

cars.remove("Toyota")
print(cars)

cars.pop()
print(cars)

del cars[-2]
print(cars)

del cars[0:3]
print(cars)

cars.clear()
print(len(cars))
print(cars)
