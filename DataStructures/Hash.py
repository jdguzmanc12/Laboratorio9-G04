def new_map(capacity=1000):
    """Crea una nueva tabla hash con capacidad inicial dada."""
    return {'keys': [None] * capacity, 'values': [None] * capacity, 'size': 0, 'capacity': capacity}

def hash_function(key, capacity):
    """Función hash simple que convierte la clave en un índice."""
    return hash(key) % capacity

def put(hash_map, key, value):
    """Inserta un par clave-valor en la tabla hash."""
    index = hash_function(key, hash_map['capacity'])
    
    while hash_map['keys'][index] is not None:
        if hash_map['keys'][index] == key:
            hash_map['values'][index] = value
            return
        index = (index + 1) % hash_map['capacity']

    hash_map['keys'][index] = key
    hash_map['values'][index] = value
    hash_map['size'] += 1

def get(hash_map, key):
    index = hash_function(key, hash_map['capacity'])
    
    while hash_map['keys'][index] is not None:
        if hash_map['keys'][index] == key:
            return hash_map['values'][index]
        index = (index + 1) % hash_map['capacity']
    
    return None

def contains(hash_map, key):
    index = hash_function(key, hash_map['capacity'])
    
    while hash_map['keys'][index] is not None:
        if hash_map['keys'][index] == key:
            return True
        index = (index + 1) % hash_map['capacity']
    
    return False