import unittest
from ..AccountRegister import AccountRegister
from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount


class TestTakeOutLoanByFirmAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Testowy"
    pesel = "03245678901"

    @classmethod
    def setUpClass(cls):
        cls.account = PersonalAccount(cls.name, cls.surname, cls.pesel)
        AccountRegister.add_to_account_register(cls.account)

    def test_add_to_account_register(self):
        testAccount = PersonalAccount(self.name, self.surname, "03245678902")
        AccountRegister.add_to_account_register(testAccount)
        self.assertEqual(AccountRegister.count_how_much_accounts_in_register(), 2,
                         "Adding to account register is not working")

    def test_add_firm_account_to_register(self):
        testFirmAccount = FirmAccount("TestEX", "1234567890")
        AccountRegister.add_to_account_register(testFirmAccount)
        self.assertEqual(AccountRegister.count_how_much_accounts_in_register(), 1,
"Firm account was added to account register")

    def test_find_account_by_pesel(self):
        result = AccountRegister.find_account_in_register_by_pesel("03245678901")
        self.assertEqual(result, self.account, "Cannot find account by pesel")

    def test_find_account_by_pesel_wrong(self):
        result = AccountRegister.find_account_in_register_by_pesel("03245678904")
        self.assertIsNone(result, "Should not find account by pesel")

    @classmethod
    def tearDownClass(cls):
        AccountRegister.account_list = []