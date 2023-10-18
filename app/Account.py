class Account:
    def __init__(self):
        self.saldo = 0    

    def incoming_transfer(self, amount):
        if amount > 0:
            self.saldo += amount
    
    def outgoing_transfer(self, amount):
        if amount > 0 and amount <= self.saldo:
            self.saldo -= amount