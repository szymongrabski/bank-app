import unittest
from ..AccountRegister import AccountRegister
from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount
from parameterized import parameterized


class TestTakeOutLoanByFirmAccount(unittest.TestCase):
    def setUp(self):
        AccountRegister.account_list = []

    def test_add_to_account_register(self):
        testAccount = PersonalAccount("Dariusz", "Test", "03245678901")
        AccountRegister.add_to_account_register(testAccount)
        self.assertEqual(AccountRegister.count_how_much_accounts_in_register(), 1, "Adding to account register is not working")

    def test_add_firm_account_to_register(self):
        testFirmAccount = FirmAccount("TestEX", "1234567890")
        AccountRegister.add_to_account_register(testFirmAccount)
        self.assertEqual(AccountRegister.count_how_much_accounts_in_register(), 0, "Firm account was added to account register")

    def test_find_account_by_pesel(self):
        AccountRegister.account_list = [PersonalAccount("Dariusz", "Test", "03245678901")]
        result = AccountRegister.find_account_in_register_by_pesel("03245678901")
        print(result)
        self.assertTrue(result, "Can not find account by pesel")

    def test_find_account_by_pesel_wrong(self):
        AccountRegister.account_list = [PersonalAccount("Dariusz", "Test", "03245678901")]
        result = AccountRegister.find_account_in_register_by_pesel("03245678902")
        self.assertFalse(result, "Can not find account by pesel")


    def test_counting_accounts(self):
        AccountRegister.account_list=[PersonalAccount("Dariusz", "Test", "03245678901"), PersonalAccount("Dariusz", "Test", "03245678904")]
        self.assertEqual(len(AccountRegister.account_list), 2, "Wrong number of accounts")

