import json

def error():
    print("Error! Invalid input. Try again...")

def pull_data(file_name:str) -> list:
    with open(file_name, 'r') as data:
        return json.load(data)

def save_data(list_to_save: list , file_name: str):
    with open(file_name, 'w') as data:
        json.dump(list_to_save, data, indent=4)


