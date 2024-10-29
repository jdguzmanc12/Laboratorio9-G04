from DataStructures.Tree import rbt_node as rbt_node

RED = 0
BLACK = 1

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
    my_rbt["root"]["color"] = BLACK

def get(my_rbt, key):
    return get_node(my_rbt["root"], key)

def contains(my_rbt, key):
    return get(my_rbt, key) is not None

def remove(my_rbt, key):
    if contains(my_rbt, key):
        if not rbt_node.is_red(my_rbt["root"]["left"]) and not rbt_node.is_red(my_rbt["root"]["right"]):
            rbt_node.change_color(my_rbt["root"], RED)
        my_rbt["root"] = remove_key(my_rbt["root"], key)
        if my_rbt["root"] is not None:
            my_rbt["root"]["color"] = BLACK

def key_set(my_rbt):
    keys = []
    in_order_keys(my_rbt["root"], keys)
    return {"size": len(keys), "elements": keys}

def in_order_keys(node, keys):
    if node:
        in_order_keys(node["left"], keys)
        keys.append(node["key"])
        in_order_keys(node["right"], keys)

def value_set(my_rbt):
    values = []
    in_order_values(my_rbt["root"], values)
    return {"size": len(values), "elements": values}

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
    node["color"] = RED
    return right_node

def rotate_right(node):
    left_node = node["left"]
    node["left"] = left_node["right"]
    left_node["right"] = node
    left_node["color"] = node["color"]
    node["color"] = RED
    return left_node

def flip_colors(node):
    node["color"] = RED if node["color"] == BLACK else BLACK
    if node["left"]:
        node["left"]["color"] = BLACK if node["left"]["color"] == RED else RED
    if node["right"]:
        node["right"]["color"] = BLACK if node["right"]["color"] == RED else RED

def insert_node(node, key, value):
    if node is None:
        return rbt_node.new_node(key, value)
    
    if key == node["key"]:
        node["value"] = value
    elif key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)
    else:
        node["right"] = insert_node(node["right"], key, value)
    if node["right"] is not None and rbt_node.is_red(node["right"]) and (node["left"] is None or not rbt_node.is_red(node["left"])):
        node = rotate_left(node)
    if node["left"] is not None and rbt_node.is_red(node["left"]) and node["left"]["left"] is not None and rbt_node.is_red(node["left"]["left"]):
        node = rotate_right(node)
    if node["left"] is not None and rbt_node.is_red(node["left"]) and node["right"] is not None and rbt_node.is_red(node["right"]):
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

def floor(my_rbt, key):
    return floor_node(my_rbt["root"], key)

def floor_node(node, key):
    if node is None:
        return None
    if key == node["key"]:
        return node["key"]
    if key < node["key"]:
        return floor_node(node["left"], key)
    t = floor_node(node["right"], key)
    return t if t is not None else node["key"]

def ceiling(my_rbt, key):
    return ceiling_node(my_rbt["root"], key)

def ceiling_node(node, key):
    if node is None:
        return None
    if key == node["key"]:
        return node["key"]
    if key > node["key"]:
        return ceiling_node(node["right"], key)
    t = ceiling_node(node["left"], key)
    return t if t is not None else node["key"]

def select(my_rbt, k):
    return select_node(my_rbt["root"], k)

def select_node(node, k):
    if node is None:
        return None
    t = size_node(node["left"])
    if t > k:
        return select_node(node["left"], k)
    elif t < k:
        return select_node(node["right"], k - t - 1)
    else:
        return node["key"]

def rank(my_rbt, key):
    return rank_node(my_rbt["root"], key)

def rank_node(node, key):
    if node is None:
        return 0
    if key < node["key"]:
        return rank_node(node["left"], key)
    elif key > node["key"]:
        return 1 + size_node(node["left"]) + rank_node(node["right"], key)
    else:
        return size_node(node["left"])

def keys(my_rbt, low, high):
    result = []
    collect_keys(my_rbt["root"], result, low, high)
    return {"size": len(result), "elements": result}

def collect_keys(node, result, low, high):
    if node is None:
        return
    if low < node["key"]:
        collect_keys(node["left"], result, low, high)
    if low <= node["key"] <= high:
        result.append(node["key"])
    if high > node["key"]:
        collect_keys(node["right"], result, low, high)

def min_key(my_rbt):
    return min_key_node(my_rbt["root"])

def min_key_node(node):
    if node is None or node["left"] is None:
        return node["key"] if node else None
    return min_key_node(node["left"])

def max_key(my_rbt):
    return max_key_node(my_rbt["root"])

def max_key_node(node):
    if node is None or node["right"] is None:
        return node["key"] if node else None
    return max_key_node(node["right"])

def values(my_rbt, low, high):
    result = []
    collect_values(my_rbt["root"], result, low, high)
    return {"size": len(result), "elements": result}

def collect_values(node, result, low, high):
    if node is None:
        return
    if low < node["key"]:
        collect_values(node["left"], result, low, high)
    if low <= node["key"] <= high:
        result.append(node["value"])
    if high > node["key"]:
        collect_values(node["right"], result, low, high)
