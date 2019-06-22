# initializing the blockchain list
blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
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
        print('outputting block')
        print(block)


while True:
    print('please choose')
    print('1: add a new transaction value')
    print('2 print the blockchain blocks')
    print('q:Exit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_block_elements()
    elif user_choice == 'q':
        break
    else:
        print('Your input is invalid')
    print('choice registered!')

print('done')
