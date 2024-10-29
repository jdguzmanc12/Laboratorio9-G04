def new_list():
    return []

def add_last(array_list, element):
    array_list.append(element)

def get_element(array_list, index):
    if 0 <= index < len(array_list):
        return array_list[index]
    return None

def size(array_list):
    return len(array_list)

def is_empty(array_list):
    return len(array_list) == 0