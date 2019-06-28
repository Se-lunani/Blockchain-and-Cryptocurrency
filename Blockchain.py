import functools

# initializing the blockchain list
MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transaction': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Evan'
participants = {'Evan'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transaction'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0, tx_sender, 0)
    tx_recipient = [[tx['amount'] for tx in block['transaction'] if tx['recipient'] == participant] for block in
                    blockchain]
    amount_received = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0, tx_recipient, 0)
    return amount_received - amount_sent


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recepient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transaction': copied_transactions
             }
    blockchain.append(block)
    return True


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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: Add a new transaction value')
    print('2:Mine a New Block')
    print('3:Output Blocks')
    print('4:Output Participants')
    print('5:check transaction validity')
    print('h:Manipulate the chain')
    print('q:Exit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recepient, amount = tx_data
        if add_transaction(recepient, amount=amount):
            print('Transaction Added')
        else:
            print('Transaction Failed')
        print(open_transactions)
        # Adding the transaction amount to the block chain
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_block_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('all transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        # securing the block chain
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'chris', 'recipient': 'Mwami', 'amount': 500}]
            }

    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Your input is invalid')
    if not verify_chain():
        print_block_elements()
        print('invalid blockchain!')
        break
    print('Balance of {}: {:6.2f}'.format('Evan', get_balance('Evan')))
else:
    print('User left!')

print('Done!')
