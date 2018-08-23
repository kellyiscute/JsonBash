import json
import copy

json_path = ''


def remove_empty(lst: list) -> list:
    result = []
    for j in range(0, lst.__len__()):
        if lst[j].__len__() != 0:
            result.append(lst[j])

    return result


def check_path(path: str, obj: dict) -> bool:
    levels = path.split('/')
    levels = remove_empty(levels)
    local_json = copy.deepcopy(obj)
    result = True
    for j in range(0, levels.__len__()):
        if levels[j] in local_json.keys():
            local_json = local_json[levels[j]]
        else:
            result = False
            break

    return result


def get_content(path: str, obj: dict):
    levels = path.split('/')
    levels = remove_empty(levels)
    local_json = copy.deepcopy(obj)
    for j in range(0, levels.__len__()):
        local_json = local_json[levels[j]]

    return local_json


def get_keys(path: str, obj: dict):
    if str(type(dict)) != 'dict':
        return ''
    levels = path.split('/')
    levels = remove_empty(levels)
    local_json = copy.deepcopy(obj)
    for j in range(0, levels.__len__()):
        print(levels[j])
        local_json = local_json[levels[j]]

    return list(local_json.keys())


if __name__ == '__main__':
    f = open('json-load.json', 'r')
    json_content = f.read()
    json_parsed = json.loads(json_content)

    while True:
        instruction = input(json_path + ' >>> ')
        command = instruction.split(' ')[0]
        if command == 'goto':
            if instruction.split(' ').__len__() > 1 and instruction.split(' ')[1] == '..':
                if json_path != '':
                    old_path = json_path
                    json_path = ''
                    for i in range(0, old_path.split('/').__len__()-1):
                        json_path += str(old_path.split('/')[i]) + '/'
            elif instruction.split(' ').__len__() > 1:
                if check_path(json_path + '/' + instruction.split(' ')[1], json_parsed):
                    json_path += '/' + instruction.split(' ')[1]
                else:
                    print('key does not exist')
            else:
                print('Where is your freaking parameter!')
        if command == 'get':
            if instruction.split(' ').__len__() > 1:
                print(get_content(json_path + str(instruction.split(' ')[1]), json_parsed))
            else:
                print(get_content(json_path, json_parsed))
        if command == 'ls':
            k = (get_keys(json_path, json_parsed))
            for j in range(0, k.__len__()):
                print(k[j])
