"""
This test case will verify if the provided exercise solution by a student for the Transaction.py is correct.
"""

from Signature import *
from Transaction import *

if __name__ == "__main__":
    
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

  # Check Valid Transactions
    # Test 1
    # --------------------------------------
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(mike_pbc, 1)
    Tx1.sign(alex_prv)

    # Test 2
    # --------------------------------------
    Tx21 = Tx()
    Tx21.add_input(alex_pbc, 2)
    Tx21.add_output(mike_pbc, 1)
    Tx21.add_output(rose_pbc, 1)
    Tx21.sign(alex_prv)

    Tx22 = Tx()
    Tx22.add_input(rose_pbc, 1.2)
    Tx22.add_output(alex_pbc, 1.1)
    Tx22.add_reqd(mara_pbc)
    Tx22.sign(rose_prv)
    Tx22.sign(mara_prv)

    for transaction in [Tx1, Tx21, Tx22]:
        if transaction.is_valid():
            print("SUCCESS! Valid transaction is verified.")
        else:
            print("ERROR! Valid transaction is not verified.")

  # Check Invalid Transactions
    # Test 3
    # --------------------------------------
    # Wrong signatures
    Tx3 = Tx()
    Tx3.add_input(alex_pbc, 1)
    Tx3.add_output(mike_pbc, 1)
    Tx3.sign(mike_prv)

    # Test 4
    # --------------------------------------
    # Escrow Tx not signed by the arbiter
    Tx4 = Tx()
    Tx4.add_input(rose_pbc, 1.2)
    Tx4.add_output(mike_pbc, 1.1)
    Tx4.add_reqd(mara_pbc)
    Tx4.sign(rose_prv)

    # Test 5
    # --------------------------------------
    # Two input addrs, signed by one
    Tx5 = Tx()
    Tx5.add_input(rose_pbc, 1)
    Tx5.add_input(mara_pbc, 0.1)
    Tx5.add_output(mike_pbc, 1.1)
    Tx5.sign(mara_prv)

    # Test 6
    # --------------------------------------
    # Outputs exceed inputs
    Tx6 = Tx()
    Tx6.add_input(mara_pbc, 1.2)
    Tx6.add_output(alex_pbc, 1)
    Tx6.add_output(alex_pbc, 2)
    Tx6.sign(mara_prv)

    # Test 7
    # --------------------------------------
    # Negative values
    Tx7 = Tx()
    Tx7.add_input(mike_pbc, -1)
    Tx7.add_output(alex_pbc, -1)
    Tx7.sign(mike_prv)

    # Test 8
    # --------------------------------------
    # Modified Tx
    Tx8 = Tx()
    Tx8.add_input(mike_pbc, 1)
    Tx8.add_output(alex_pbc, 1)
    Tx8.sign(mike_prv)
    
    # outputs = [(alex_pbc,1)] change to [(rose_pbc,1)]
    Tx8.outputs[0] = (rose_pbc, 1)

    for transaction in [Tx3, Tx4, Tx5, Tx6, Tx7, Tx8]:
        if transaction.is_valid():
            print("ERROR! Invalid transaction is not verified.")
        else:
            print("SUCCESS! Invalid transaction is not verified.")