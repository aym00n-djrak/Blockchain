from blockchain_class import *


t1 = "John sends 2 BTC to Mike"
t2 = "Mike sends 1 BTC to John"
t3 = "John sends 2 BTC to Mike"
t4 = "Mike sends 1 BTC to John"


def create_chain():
    chain = Block.generate_genesis_block()
    print("Genesis Block : \n")
    print(chain)
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
        chain = chain.generate_next_block(chain.get_hash(), list)
        print("Block " + str(i+1) + " : \n")
        print(chain)
    print("Blockchain \n", chain)
    return chain


blockchain= create_chain()



