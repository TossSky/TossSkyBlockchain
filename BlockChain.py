import hashlib
import datetime


class Transaction:
    def __init__(self, sender, receiver, amount, nonce, contract_call=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.nonce = nonce
        self.contract_call = contract_call  # Для вызова смарт-контрактов
        self.data = f"{self.sender} -> {self.receiver}: {self.amount} (nonce: {self.nonce}, contract: {self.contract_call})".encode()

    def __str__(self):
        return f"Transaction(sender={self.sender}, receiver={self.receiver}, amount={self.amount}, nonce={self.nonce}, contract_call={self.contract_call})"


class Block:
    def __init__(self, index, previous_hash, transactions, difficulty=4):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.nonce = 0
        self.timestamp = datetime.datetime.now()
        self.hash = self.calculate_hash(difficulty)

    def calculate_hash(self, difficulty):
        while True:
            block_content = f"{self.index}{self.previous_hash}{self.transactions}{self.nonce}".encode()
            hash_result = hashlib.sha256(block_content).hexdigest()
            if hash_result.startswith('0' * difficulty):
                return hash_result
            self.nonce += 1

    def __str__(self):
        transactions_str = "\n  ".join(str(tx) for tx in self.transactions)
        return (f"Block {self.index}:\n"
                f"  Previous Hash: {self.previous_hash}\n"
                f"  Transactions:\n  {transactions_str}\n"
                f"  Hash: {self.hash}\n"
                f"  Nonce: {self.nonce}\n"
                f"  Timestamp: {self.timestamp}")


class SmartContract:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, sender, amount):
        self.balance += amount
        print(f"Contract balance updated: {self.balance} USDT (deposit from {sender})")

    def withdraw(self, sender, amount):
        if sender != self.owner:
            print("Unauthorized access: only the owner can withdraw funds.")
            return False
        if self.balance < amount:
            print("Insufficient contract balance.")
            return False
        self.balance -= amount
        print(f"Contract balance updated: {self.balance} USDT (withdraw by {sender})")
        return True

    def __str__(self):
        return f"SmartContract(owner={self.owner}, balance={self.balance})"


class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]
        self.mempool = []
        self.contracts = {}


    def create_genesis_block(self):
        return Block(0, "0", ["Genesis Block"], self.difficulty)

    def add_transaction(self, transaction):
        if transaction.contract_call:
            self.execute_contract(transaction)
        else:
            self.mempool.append(transaction)

    def execute_contract(self, transaction):
        contract_address = transaction.contract_call["address"]
        function_name = transaction.contract_call["function"]
        parameters = transaction.contract_call["parameters"]

        if contract_address not in self.contracts:
            print(f"Contract {contract_address} not found.")
            return

        contract = self.contracts[contract_address]
        if hasattr(contract, function_name):
            function = getattr(contract, function_name)
            function(transaction.sender, *parameters)
        else:
            print(f"Function {function_name} not found in contract {contract_address}.")

    def deploy_contract(self, owner):
        contract = SmartContract(owner)
        contract_address = f"contract_{len(self.contracts) + 1}"
        self.contracts[contract_address] = contract
        print(f"Contract deployed at address: {contract_address}")
        return contract_address

    def mine_block(self):
        if not self.mempool:
            print("No transactions to mine.")
            return
        transactions = self.mempool[:]
        self.mempool.clear()

        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions, self.difficulty)
        self.chain.append(new_block)
        print(f"Block {new_block.index} mined successfully!")

    def __str__(self):
        return "\n".join(str(block) for block in self.chain)


# Создание блокчейна
TossSky = Blockchain(difficulty=4)

# Деплой контракта
contract_address = TossSky.deploy_contract("Alice")

# Вызов методов контракта через транзакции
TossSky.add_transaction(Transaction("Bob", None, 20, 0, {"address": contract_address, "function": "deposit", "parameters": [20]}))
TossSky.add_transaction(Transaction("Alice", None, 0, 0, {"address": contract_address, "function": "withdraw", "parameters": [10]}))

# Майнинг блока
TossSky.mine_block()

# Вывод блокчейна и контракта
print(TossSky)
print("\nContracts:")
for address, contract in TossSky.contracts.items():
    print(f"{address}: {contract}")
