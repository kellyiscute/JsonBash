import json
import copy

JSON_PATH = ''


def remove_empty(lst: list) -> list:
    # result = []
    # for item in lst:
    #     if len(item) != 0:
    #         result.append(item)
    result = [item for item in lst if len(item) != 0]
    return result


def check_path(path: str, obj: dict) -> bool:
    """
    Check if each level of path is in the names of obj.

    Args:
        path: This is the first param.
        obj: This is a second param.

    Returns:
        The Boolean of the checkage.
    """
    levels = path.split('/')
    levels = remove_empty(levels)
    result = True
    for level in levels:
        if not level in obj.keys():
            result = False
            break
    return result


def get_content(path: str, obj: dict):
    levels = path.split('/')
    levels = remove_empty(levels)
    local_json = copy.deepcopy(obj)
    for j in range(0, levels.__len__()):
        local_json = local_json[levels[j]]  # TODO: explanation required

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
        instruction = input(JSON_PATH + ' >>> ')
        command = instruction.split(' ')[0]
        if command == 'goto':
            if instruction.split(' ').__len__() > 1 and instruction.split(' ')[1] == '..':
                if JSON_PATH != '':
                    old_path = JSON_PATH
                    JSON_PATH = ''
                    for i in range(0, old_path.split('/').__len__()-1):
                        JSON_PATH += str(old_path.split('/')[i]) + '/'
            elif instruction.split(' ').__len__() > 1:
                if check_path(JSON_PATH + '/' + instruction.split(' ')[1], json_parsed):
                    JSON_PATH += '/' + instruction.split(' ')[1]
                else:
                    print('key does not exist')
            else:
                print('Where is your freaking parameter!')
        if command == 'get':
            if instruction.split(' ').__len__() > 1:
                print(get_content(JSON_PATH + str(instruction.split(' ')[1]), json_parsed))
            else:
                print(get_content(JSON_PATH, json_parsed))
        if command == 'ls':
            k = (get_keys(JSON_PATH, json_parsed))
            for j in range(0, k.__len__()):
                print(k[j])
