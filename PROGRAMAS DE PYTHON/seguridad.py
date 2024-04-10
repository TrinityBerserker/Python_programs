import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    # Datos iniciales del bloque génesis
    return Block(0, "0", datetime.datetime.now(), "Datos iniciales", calculate_hash(0, "0", datetime.datetime.now(), "Datos iniciales"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = datetime.datetime.now()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Crear la cadena de bloques
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Añadir bloques a la cadena de bloques
blocks_to_add = 5
for i in range(1, blocks_to_add + 1):
    new_data = f'Datos del bloque {i}'
    new_block = create_new_block(previous_block, new_data)
    blockchain.append(new_block)
    previous_block = new_block

# Imprimir la cadena de bloques
for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print("\n")
