class Account:
    def __init__(self):
        self.saldo = 0
        self.express_transfer_fee = 1
        self.transfer_history = []

    def incoming_transfer(self, amount):
        if amount > 0:
            self.saldo += amount
            self.transfer_history.append(amount)

    def outgoing_transfer(self, amount):
        if 0 < amount <= self.saldo:
            self.saldo -= amount
            self.transfer_history.append(-amount)

    def express_transfer(self, amount):
        if 0 < amount <= self.saldo:
            self.saldo -= (amount + self.express_transfer_fee)
            self.transfer_history.extend([-amount, -self.express_transfer_fee])
    

    