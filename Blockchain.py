# initializing the blockchain list
blockchain = []
open_transactions = []
owner = 'Evan'


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
    pass


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
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: add a new transaction value')
    print('2 print the blockchain blocks')
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
        print_block_elements()
    elif user_choice == 'h':
        # securing the block chain
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Your input is invalid')
    if not verify_chain():
        print('invalid blockchain')
        break
    else:
        print('User left!')

print('Done!')
