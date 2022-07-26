from urllib import request
import json


req = request.urlopen("http://localhost:5000/")
content = req.read()
data = json.loads(content)


class Joke:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self) -> str:
        return f"My name is {name}, I am {age} years and I am a {gender}"
    
    
for item in data:
    name = item["name"]
    age = item["age"]
    gender = item["gender"]
    print(Joke(name, age, gender))
