# initializing the blockchain list
blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=None):
    if last_transaction is None:
        last_transaction = [1]
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    # gets user input, transforms it from a string to a float and stores it
    user_input = float(input('Enter your Transaction Amount PLease:'))
    return user_input


def get_user_choice():
    user_input = input('your choice :')
    return user_input


def print_block_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0]== blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid





while True:
    print('please choose')
    print('1: add a new transaction value')
    print('2 print the blockchain blocks')
    print('h:Manipulate the chain')
    print('q:Exit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_block_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
         blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Your input is invalid')
    if not verify_chain():
        print('invalid blockchain')
        break

print('Done!')

