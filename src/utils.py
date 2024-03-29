import json
import datetime


def read_json():
    with open("operation.json", 'r') as file:
        read_file = json.load(file)
        return read_file


def last_five_operation(read_file):
    read_file.reverse()
    executed_list = []
    for i in read_file:
        if 'state' in i.keys():
            if i['state'] == 'EXECUTED':
                executed_list.append(i)
            else:
                continue
        else:
            continue
    get_file = executed_list[0:5]
    get_file.reverse()
    return get_file


def give_operation(get_file):
    for get_dict in get_file:
        get_date = datetime.datetime.strptime(get_dict['date'], '%Y-%m-%dT%H:%M:%S.%f')
        print(f"{get_date.strftime('%d.%m.%Y')} {get_dict['description']}")
        print(f"{from_operation(get_dict)} -> {to_operation(get_dict)} ")
        print(f"{get_dict['operationAmount']['amount']} {get_dict['operationAmount']['currency']['name']}\n")


def from_operation(operation):
    if 'from' in operation.keys():
        split_from = operation['from'].split(' ')
        if split_from[0] == 'Счет':
            return f"{split_from[0]} **{split_from[1][-4:]}"
        elif len(split_from) > 2:
            return f"{split_from[0]} {split_from[1]} {split_from[-1][0:4]} {split_from[-1][4:6]}** **** {split_from[-1][-4:]}"
        else:
            return f"{split_from[0]} {split_from[1][0:4]} {split_from[1][4:6]}** **** {split_from[1][-4:]}"
    else:
        return ''


def to_operation(operation):
    split_to = operation['to'].split(' ')
    if split_to[0] == 'Счет':
        return f"{split_to[0]} **{split_to[1][-4:]}"
    elif len(split_to) > 2:
        return f"{split_to[0]} {split_to[1]} {split_to[-1][0:4]} {split_to[-1][4:6]}** **** {split_to[-1][-4:]}"
    else:
        return f"{split_to[0]} {split_to[1][0:4]} {split_to[1][4:6]}** **** {split_to[1][-4:]}"

# print(read_json())
# print(last_five_operation(read_json()))
# print(give_operation(last_five_operation()))
# print(to_operation(last_five_operation()))
