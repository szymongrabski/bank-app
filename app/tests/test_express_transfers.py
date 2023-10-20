import unittest
from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount


class TestExpressTransfers(unittest.TestCase):
    def test_express_transfer_from_personal_account(self):
        account = PersonalAccount("Janusz", "Testowy", "01260100000")
        account.saldo = 100
        account.express_transfer(50)
        self.assertEqual(account.saldo, 49, "Wrong saldo in express transfer made by PersonalAccount")

    def test_express_transfer_from_personal_account_with_wrong_amount(self):
        account = PersonalAccount("Janusz", "Testowy", "01260100000")
        account.saldo = 100
        account.express_transfer(-50)
        self.assertEqual(account.saldo, 100, "Wrong saldo in express transfer made by PersonalAccount with wrong amount")

    def test_express_transfer_from_personal_account_with_discount_code(self):
        account = PersonalAccount("Janusz", "Testowy", "03260100000", "PROM_123")
        account.express_transfer(50)
        self.assertEqual(account.saldo, -1, "Wrong saldo in express transfer made by PersonalAccount with discount code")

    def test_express_transfer_from_firm_account(self):
        account = FirmAccount("SGF", "1234567890")
        account.saldo = 100
        account.express_transfer(50)
        self.assertEqual(account.saldo, 45, "Wrong saldo in express transfer made by FirmAccount")

    def test_express_transfer_from_firm_account_with_amount_bigger_than_saldo(self):
        account = FirmAccount("SGF", "1234567890")
        account.saldo = 10
        account.express_transfer(50)
        self.assertEqual(account.saldo, 10, "Amount bigger than saldo in express transfer in FirmAccount passed")