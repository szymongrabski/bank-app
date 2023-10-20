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