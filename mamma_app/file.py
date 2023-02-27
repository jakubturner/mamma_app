import json


def file_print():
    with open("tests/resources/data.json") as f:
        print(json.load(f))


file_print()
