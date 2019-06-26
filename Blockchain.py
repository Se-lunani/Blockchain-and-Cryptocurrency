# initializing the blockchain list
genesis_block = {
        'previous_hash':'',
        'index': 0,
        'transaction': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Evan'


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction (recepient, sender=owner,amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recepient,
        'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transaction': open_transactions
             }
    blockchain.append(block)




def get_transaction_value():
    # gets user input, transforms it from a string to a float and stores it
    tx_recipient = input('Enter the recipient of the Transaction:')
    tx_amount = float(input('Enter your Transaction Amount PLease:'))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('your choice :')
    return user_input


def print_block_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('*' * 20)


def verify_chain():
    for (index,block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash']!=hash_block(blockchain[index-1]):
            return False
    return True




waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: Add a new transaction value')
    print('2:Mine a New Block')
    print('3:Output Blocks')
    print('h:Manipulate the chain')
    print('q:Exit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recepient, amount = tx_data
        add_transaction(recepient, amount=amount)
        print(open_transactions)
        # Adding the transaction amount to the block chain
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_block_elements()
    elif user_choice == 'h':
        # securing the block chain
        if len(blockchain) >= 1:
            blockchain[0] ={
                'previous_hash':'',
                'index':0,
                'transactions':[{'sender':'chris','recipient':'Mwami','amount':500}]
            }

    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Your input is invalid')
    if not verify_chain():
        print_block_elements()
        print ('invalid blockchain!')
        break
else:
        print('User left!')

print('Done!')
