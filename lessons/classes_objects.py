class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self) -> str:
        return f"Brand: {self.brand}  price:{self.price}"

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")


infinix = Phone("Hot 8 Lite", 40000)
samsung = Phone("S20", 400000)

print(infinix.brand)
print(infinix.price)
infinix.call(9000923)

print(infinix)