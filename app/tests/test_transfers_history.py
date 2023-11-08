import unittest

from ..FirmAccount import FirmAccount
from ..PersonalAccount import PersonalAccount


class TestTransferHistory(unittest.TestCase):  
    testFirmAccount = FirmAccount("SGF", "1234567890")
    testPersonalAccount = PersonalAccount("Krzysztof", "Testowy", "01260100000")

    def test_transfer_history_by_firm_account(self):
        account = FirmAccount(self.testFirmAccount.firm_name, self.testFirmAccount.nip)
        account.incoming_transfer(100)
        account.outgoing_transfer(50)
        account.incoming_transfer(20)
        account.express_transfer(40)
        self.assertEqual(account.transfer_history, [100, -50, 20, -40, -5], "Wrong transfer history in firm account passed")

    def test_transfer_history_by_personal_account(self):
        account = PersonalAccount(self.testPersonalAccount.name, self.testPersonalAccount.surname, self.testPersonalAccount.pesel)
        account.incoming_transfer(100)
        account.outgoing_transfer(50)
        account.incoming_transfer(20)
        account.express_transfer(40)
        self.assertEqual(account.transfer_history, [100, -50, 20, -40, -1], "Wrong transfer history in firm personal passed")
    
    def test_transfer_history_with_wrong_saldo(self):
        account = FirmAccount(self.testFirmAccount.firm_name, self.testFirmAccount.nip)
        account.outgoing_transfer(50)
        self.assertEqual(account.transfer_history, [], "Account history added wrong transfer")

