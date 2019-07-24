from collections import  OrderedDict
class Transaction:
    def __init__(self, sender, recepient, amount):
        self.sender = sender
        self.recipient = recepient
        self.amount = amount
def to_ordered_dict(self):
    return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
