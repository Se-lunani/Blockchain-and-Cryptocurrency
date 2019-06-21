#initializing the blockchain list
blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=None):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input('Enter your Transaction Amount PLease:'))

#getting the first transaction input and adding the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_user_input())

# output the blockchain list to the console

    for block in blockchain:
        print('outputting block')
        print(block)

print('done')
