import json
import datetime


def last_five_operation():
    with open("operation.json", 'r') as file:
        read_file = json.load(file)
        read_file.reverse()
        get_file = read_file[0:5]
        get_file.reverse()
        return get_file


def give_operation(get_file):
    for get_dict in get_file:
        print(get_dict.get("date"))


print(give_operation(last_five_operation()))
