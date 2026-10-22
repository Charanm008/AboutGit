import json

date = {
    "employee":[
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Anna", "age": 22, "city": "London"},
        {"name": "Peter", "age": 34, "city": "Berlin"}
    ]
}

with open('data.json', 'w', newline='') as f:
    json.dump(date, f)

with open('data.json', 'r', newline='') as f:
    data = json.load(f)
    print(data)