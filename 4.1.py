# TODO решите задачу
import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    value = sum([i["score"] * i["weight"] for i in data])
    return round(value, 3)


print(task())
