from BlockChain import CBlock
from Signature import generate_keys, sign, verify
import pickle
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import time

from Transaction import *

from TxBlock import *

MIN_MINING_TIME = 30
MAX_MINING_TIME = 60

if __name__ == "__main__":

    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

# Valid Blocks

    # Valid Transactions
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 5)
    Tx1.add_output(rose_pbc, 5)
    Tx1.sign(alex_prv)

    Tx2 = Tx()
    Tx2.add_input(mike_pbc,1)
    Tx2.add_output(rose_pbc,0.9)
    Tx2.sign(mike_prv)

    # Block "root": Valid
    root = TxBlock(None)
    root.addTx(Tx1)
    root.addTx(Tx2)

    # Valid Transactions
    Tx3 = Tx()
    Tx3.add_input(rose_pbc,3.1)
    Tx3.add_output(alex_pbc, 3)
    Tx3.sign(rose_prv)
    
    Tx4 = Tx()
    Tx4.add_input(mike_pbc,2.1)
    Tx4.add_output(mara_pbc, 2)
    Tx4.add_reqd(rose_pbc)
    Tx4.sign(mike_prv)
    Tx4.sign(rose_prv)

    # Block "B1": Valid
    B1 = TxBlock(root)
    B1.addTx(Tx3)
    B1.addTx(Tx4)

# -------------------------------------------------
    start = time.time()
    nonce = B1.find_nonce()
    elapsed = time.time() - start

    if B1.good_nonce():
        print("Success! Nonce is good!")
        print(f'Accepted Nonce = {str(nonce)}')

        print("elapsed time: " + str(elapsed) + " s.")
        if elapsed < MIN_MINING_TIME:
            print("Alarm! Mining is too fast")
        elif elapsed > MAX_MINING_TIME:
            print("Alarm! Mining is too Slow")
    
    else:
        print("ERROR! Bad nonce")

# -------------------------------------------------


    savefile = open("block.dat", "wb")
    pickle.dump(B1, savefile)
    savefile.close()

    loadfile = open("block.dat" ,"rb")
    load_B1 = pickle.load(loadfile)
    loadfile.close()

    for b in [root, B1, load_B1, load_B1.previousBlock]:
        if b.is_valid():
            print ("Success! Valid block is verified.")
        else:
            print ("Error! Valid block is not verified.")

# ----------------------------------------------------------------------
    if load_B1.good_nonce():                                    # ------
        print("Success! Nonce is good after save and load!")    # ------
    else:                                                       # ------
        print("ERROR! Bad nonce after load")                    # ------
# ----------------------------------------------------------------------


    Tx5 = Tx()
    Tx5.add_input(rose_pbc, 1)
    Tx5.add_output(mike_pbc, 10)
    Tx5.sign(rose_prv)

    B2 = TxBlock(B1)
    B2.addTx(Tx5)

    load_B1.previousBlock.addTx(Tx4)

    for b in [B2, load_B1]:
        if b.is_valid():
            print ("Error! Invalid block is verified.")
        else:
            print ("Success! Invalid blocks is detected.")


    # Test mining rewards and tx fees
    B3 = TxBlock(B2)
    B3.addTx(Tx2)
    B3.addTx(Tx3)
    B3.addTx(Tx4)

    # reward transaction
    Tx6 = Tx(type=REWARD)
    Tx6.add_output(mara_pbc, REWARD_VALUE)
    B3.addTx(Tx6)
    
    # validation of valid block, containing tx for mining reward + 3 other valid txs
    if B3.is_valid():
        print("Success! Block reward succeeded.")
    else:
        print("Error! Block reward failed.")

    # validation of valid block, containing tx for mining reward and tx fees + 3 other valid txs
    B4 = TxBlock(B3)
    B4.addTx(Tx2)
    B4.addTx(Tx3)
    B4.addTx(Tx4)

    Tx7 = Tx(type=REWARD)
    Tx7.add_output(mara_pbc, 25.3)
    B4.addTx(Tx7)

    if B4.is_valid():
        print("Success! Transaction fees succeeded.")
    else:
        print("Error! Transaction fees failed.")


    #Greedy miner
    B5 = TxBlock(B4)
    B5.addTx(Tx2)
    B5.addTx(Tx3)
    B5.addTx(Tx4)

    Tx8 = Tx()
    Tx8.add_output(mara_pbc, REWARD_VALUE + 1 + 0.3)

    # validation of invalid block, containing tx for (invalid) mining reward (26 coins for reward)
    B5.addTx(Tx8)
    if not B5.is_valid():
        print("Success! Greedy miner is detected.")
    else:
        print("Error! Greedy miner is not detected")