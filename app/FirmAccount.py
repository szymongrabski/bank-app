from .Account import Account


class FirmAccount(Account):
    def __init__(self, firm_name, nip):
        super().__init__()
        self.firm_name = firm_name
        self.express_transfer_fee = 5
        if len(nip) != 10:
            self.nip = "Wrong NIP"
        else:
            self.nip = nip

    def take_out_loan(self, amount):
        if amount < 0:
            return False
        elif -1775 in self.transfer_history and self.saldo >= amount*2:
            self.saldo += amount
            return True
        else:
            return False
