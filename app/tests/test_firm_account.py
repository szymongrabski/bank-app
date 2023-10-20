import unittest

from ..FirmAccount import FirmAccount


class TestCreateBankAccount(unittest.TestCase):
    name = "SGF"
    nip = "1234567890"

    def test_create_firm_account(self):
        account = FirmAccount(self.name, self.nip)
        self.assertEqual(account.firm_name, self.name, "Wrong firm name passed")
        self.assertEqual(account.nip, self.nip, "Wrong nip passed")
        self.assertEqual(account.saldo, 0, "Wrong saldo passed")

    def test_create_firm_account_with_incorrect_nip(self):
        account = FirmAccount(self.name, "0123")
        self.assertEqual(account.nip, "Wrong NIP", "Wrong nip passed")

    def test_incoming_transfer(self):
        account = FirmAccount(self.name, self.nip)
        account.incoming_transfer(100)
        self.assertEqual(account.saldo, 100, "Wrong saldo in incoming transfer in FirmAccount class")

    def test_outgoing_transfer(self):
        account = FirmAccount(self.name, self.nip)
        account.saldo = 120
        account.outgoing_transfer(20)
        self.assertEqual(account.saldo, 100, "Wrong saldo in outgoing transfer in FirmAccount class")
