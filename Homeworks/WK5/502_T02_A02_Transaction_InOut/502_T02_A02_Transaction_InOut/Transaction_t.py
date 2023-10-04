"""
This test case will verify if the provided exercise solution by a student for the Transaction.py is correct.
"""

from Signature import *
from Transaction import *

def print_transaction(tx_name, tx):
    print('---------------')
    print(f'-- {tx_name}')

    for (index, input_item) in enumerate(tx.inputs):
        for key_name, prv_key, pbc_key in keys_list:
            if pbc_key == input_item[0]:
                payer = key_name
        print(f'In[{index+1}]:  {payer} sends {input_item[1]} coin')

    for (index, output_item) in enumerate(tx.outputs):
        for key_name, prv_key, pbc_key in keys_list:
            if pbc_key == output_item[0]:
                receiver = key_name
        print(f'Out[{index+1}]: {receiver} receives {output_item[1]} coin') 
    print()

if __name__ == '__main__':
    
    keys_list =[]

    alex_prv, alex_pbc = generate_keys()
    keys_list.append(('alex', alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(('mike', mike_prv, mike_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(('rose', rose_prv, rose_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(('mara', mara_prv, mara_pbc))

    print(keys_list)

    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 0.9)
    Tx1.add_output(mike_pbc, 0.8)
    print_transaction('Tx1', Tx1)

    Tx2 = Tx()
    Tx2.add_input(alex_pbc, 2.1)
    Tx2.add_output(mike_pbc, 0.9)
    Tx2.add_output(rose_pbc, 1.0)
    print_transaction('Tx2', Tx2)

    Tx2.add_input(mara_pbc, 0.7)
    Tx2.add_input(mara_pbc, 1.1)
    Tx2.add_input(mara_pbc, 1.5)
    Tx2.add_output(mike_pbc, 1.9)
    Tx2.add_output(rose_pbc, 0.2)
    print_transaction('Tx2', Tx2)