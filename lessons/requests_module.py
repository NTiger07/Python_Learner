import json
import requests

response = requests.get("http://localhost:5000/")
jsonData = json.loads(response.text)

class Joke:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self) -> str:
        return f"My name is {name}, I am {age} years and I am a {gender}"
    
for item in jsonData:
    name = item["name"]
    age = item["age"]
    gender = item["gender"]
    print(Joke(name, age, gender))
