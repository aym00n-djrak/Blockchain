from cryptography.hazmat.primitives import hashes

class Block :

    def __init__(self, previous_hash, transaction_list):
        self.previous_hash = previous_hash
        self.transaction_list = transaction_list

        if type(self.previous_hash) != str :
            self.previous_hash = str(self.previous_hash)

        self.block_data= "-".join(transaction_list)+ "-" + self.previous_hash
        self.block_hash= hash(self.block_data.encode())
        self.block_hash = str(self.block_hash)
        self.previous_block = None
        self.next_block = None


    def hash(block_data):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(block_data.encode())
        return digest.finalize()
    
    def transaction(self, transaction):
        self.transaction_list.append(transaction)
        self.block_data= "-".join(self.transaction_list)+ "-" + self.previous_hash
        self.block_hash= hash(self.block_data.encode())

    def get_block_data(self):
        return self.block_data
    
    def get_block_hash(self):
        return self.block_hash
    
    def get_transaction_list(self):
        return self.transaction_list
    
    def get_previous_hash(self):
        return self.previous_hash
    
    def get_hash(self):
        return self.block_hash

    def generate_genesis_block():
        return Block("0", ["Genesis Block"])
    
    def generate_next_block(self, previous_hash, transaction_list):
        return Block(previous_hash, transaction_list)
    

    def get_previous_block(self):
        return self.previous_block
    
    def get_next_block(self):
        return self.next_block
    
    def __str__(self):
        return "Block hash: " + self.block_hash + "\nPrevious hash: " + self.previous_hash + "\nTransaction list: " + str(self.transaction_list) + "\nBlock data: " + self.block_data + "\n"
