from DataStructures.Tree import rbt_node

def new_map():
    return {"root": None, "type": "RBT"}

def is_empty(my_rbt):
    return my_rbt["root"] is None

def size(my_rbt):
    return size_node(my_rbt["root"])

def size_node(node):
    if node is None:
        return 0
    return 1 + size_node(node["left"]) + size_node(node["right"])

def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    my_rbt["root"]["color"] = rbt_node.BLACK

def get(my_rbt, key):
    return get_node(my_rbt["root"], key)

def contains(my_rbt, key):
    return get(my_rbt, key) is not None

def remove(my_rbt, key):
    if contains(my_rbt, key):
        if not rbt_node.is_red(my_rbt["root"]["left"]) and not rbt_node.is_red(my_rbt["root"]["right"]):
            rbt_node.change_color(my_rbt["root"], rbt_node.RED)
        my_rbt["root"] = remove_key(my_rbt["root"], key)
        if my_rbt["root"] is not None:
            my_rbt["root"]["color"] = rbt_node.BLACK

def key_set(my_rbt):
    keys = []
    in_order_keys(my_rbt["root"], keys)
    return keys

def in_order_keys(node, keys):
    if node:
        in_order_keys(node["left"], keys)
        keys.append(node["key"])
        in_order_keys(node["right"], keys)

def value_set(my_rbt):
    values = []
    in_order_values(my_rbt["root"], values)
    return values

def in_order_values(node, values):
    if node:
        in_order_values(node["left"], values)
        values.append(node["value"])
        in_order_values(node["right"], values)

def height(my_rbt):
    return height_node(my_rbt["root"])

def height_node(node):
    if node is None:
        return -1
    return 1 + max(height_node(node["left"]), height_node(node["right"]))

def rotate_left(node):
    right_node = node["right"]
    node["right"] = right_node["left"]
    right_node["left"] = node
    right_node["color"] = node["color"]
    node["color"] = rbt_node.RED
    return right_node

def rotate_right(node):
    left_node = node["left"]
    node["left"] = left_node["right"]
    left_node["right"] = node
    left_node["color"] = node["color"]
    node["color"] = rbt_node.RED
    return left_node

def flip_colors(node):
    node["color"] = rbt_node.RED if node["color"] == rbt_node.BLACK else rbt_node.BLACK
    if node["left"]:
        node["left"]["color"] = rbt_node.BLACK if node["left"]["color"] == rbt_node.RED else rbt_node.RED
    if node["right"]:
        node["right"]["color"] = rbt_node.BLACK if node["right"]["color"] == rbt_node.RED else rbt_node.RED

def insert_node(node, key, value):
    if node is None:
        return rbt_node.new_node(key, value, rbt_node.RED)
    if key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)
    elif key > node["key"]:
        node["right"] = insert_node(node["right"], key, value)
    else:
        node["value"] = value

    if rbt_node.is_red(node["right"]) and not rbt_node.is_red(node["left"]):
        node = rotate_left(node)
    if rbt_node.is_red(node["left"]) and rbt_node.is_red(node["left"]["left"]):
        node = rotate_right(node)
    if rbt_node.is_red(node["left"]) and rbt_node.is_red(node["right"]):
        flip_colors(node)

    return node

def get_node(node, key):
    while node is not None:
        if key < node["key"]:
            node = node["left"]
        elif key > node["key"]:
            node = node["right"]
        else:
            return node["value"]
    return None
