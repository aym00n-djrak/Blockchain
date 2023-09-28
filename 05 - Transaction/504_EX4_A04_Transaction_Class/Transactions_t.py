"""
This test case will verify if the provided exercise solution by a student for the Transaction.py is correct.
"""

from Signature import *

from Transaction import *


def print_transaction(tx_name, tx):
    print("---------------")
    print(f"-- {tx_name}")

    for index, input_item in enumerate(tx.inputs):
        payer = None
        for key_name, prv_key, pbc_key in keys_list:
            if pbc_key == input_item[0]:
                payer = key_name
        if payer != None:
            print(f"In[{index+1}]:  {payer} sends {input_item[1]} coin")
        else:
            print("There is no known Public key for sender")

    for index, output_item in enumerate(tx.outputs):
        receiver = None
        for key_name, prv_key, pbc_key in keys_list:
            if pbc_key == output_item[0]:
                receiver = key_name
        if receiver != None:
            print(f"Out[{index+1}]: {receiver} receives {output_item[1]} coin")
        else:
            print("There is no known Public key for receiver")

    tx_data = []
    tx_data.append(tx.inputs)
    tx_data.append(tx.outputs)
    tx_data.append(tx.reqd)
    signed = False
    for s in tx.sigs:
        for key_name, _, pbc_key in keys_list:
            if verify(tx_data, s, pbc_key):
                signed = True
                print(f"\n{tx_name} is signed by {key_name}.", end="\n")
                # print(s, end='\n')
    if not signed:
        print("There is no signature on this Transaction")

    print()


if __name__ == "__main__":
    keys_list = []

    alex_prv, alex_pbc = generate_keys()
    keys_list.append(("alex", alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(("mike", mike_prv, mike_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(("rose", rose_prv, rose_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(("mara", mara_prv, mara_pbc))

    # --------------------------------------
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(mike_pbc, 1)
    Tx1.sign(alex_prv)

    # --------------------------------------
    Tx2 = Tx()
    Tx2.add_input(alex_pbc, 2)
    Tx2.add_output(mike_pbc, 1)
    Tx2.add_output(rose_pbc, 1)
    Tx2.sign(alex_prv)

    # --------------------------------------
    Tx3 = Tx()
    Tx3.add_input(rose_pbc, 1.2)
    Tx3.add_output(alex_pbc, 1.1)
    Tx3.sign(rose_prv)
    Tx3.sign(mara_prv)

    # --------------------------------------
    print([k for k, v in locals().items()])
    for tx in [Tx1, Tx2, Tx3]:
        tx_name = [k for k, v in locals().items() if v == tx][0]
        print(tx, tx_name)
        print_transaction(tx_name, tx)
