#initializing the blockchain list
blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=None):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    #gets user input, transforms it from a string to a float and stores it
    user_input =  float(input('Enter your Transaction Amount PLease:'))
    return user_input

def get_user_choice():
    user_input = input('your choice :')
    return user_input

def print_block_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print('outputting block')
        print(block)


#getting the first transaction input and adding the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('please choose')
    print('1 add a new transaction value')
    print('2 print the blockchain')
    print('q:Exit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_transaction_value())
    elif user_choice =='2':
        print_block_elements()
    elif user_choice=='q':
        break
    else:
        print('Your input is invalid')
    print('choice registered!')

print('done')

