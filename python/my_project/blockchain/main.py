from blockchain_class import *


t1 = "John sends 2 BTC to Mike"
t2 = "Mike sends 1 BTC to John"
t3 = "John sends 2 BTC to Mike"
t4 = "Mike sends 1 BTC to John"


def create_chain():
    blockchain = [Block.generate_genesis_block()]
    print("Genesis Block : \n")
    print(blockchain[-1])
    print("How many blocks do you want to add?")
    n = int(input())
    for i in range(n):
        list = []
        print("How many transactions do you want to add?")
        m = int(input())
        for j in range(m):
            print("Enter transaction")
            t = input()
            list.append(t)
        new_block = blockchain[-1].generate_next_block(blockchain[-1].get_hash(), list)
        blockchain.append(new_block)
        print("Block " + str(i+1) + " : \n")
        print(blockchain[-1])

    return blockchain


blockchain= create_chain()


for i in range(len(blockchain)):
    print("Block " + str(i) + " : \n")
    print(blockchain[i])
    print("\n")

