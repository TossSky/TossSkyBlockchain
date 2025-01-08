import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = f"{self.index}{self.previous_hash}{self.data}".encode()
        return hashlib.sha256(block_content).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")
    
    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)

# Пример
First_Blockchain = Blockchain()

First_Blockchain.add_block("Hello")
First_Blockchain.add_block("world!")

for block in First_Blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}")
