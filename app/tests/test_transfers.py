import unittest

from ..PersonalAccount import PersonalAccount


class TestTransfer(unittest.TestCase):
    personal_data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "03245678901"
    }

    def test_incoming_transfer(self):
        account = PersonalAccount(self.personal_data["name"], self.personal_data["surname"],
                                  self.personal_data["pesel"])
        account.incoming_transfer(50)
        self.assertEqual(account.saldo, 50, "Incoming transfer is not working")

    def test_incoming_transfer_with_incorrect_amount(self):
        account = PersonalAccount(self.personal_data["name"], self.personal_data["surname"],
                                  self.personal_data["pesel"])
        account.incoming_transfer(-50)
        self.assertEqual(account.saldo, 0, "Incoming transfer with incorrect amount passed")

    def test_outgoing_transfer(self):
        account = PersonalAccount(self.personal_data["name"], self.personal_data["surname"],
                                  self.personal_data["pesel"])
        account.saldo = 100
        account.outgoing_transfer(50)
        self.assertEqual(account.saldo, 50, "Outgoing transfer is not working")

    def test_outgoing_transfer_with_amount_greater_than_saldo(self):
        account = PersonalAccount(self.personal_data["name"], self.personal_data["surname"],
                                  self.personal_data["pesel"])
        account.saldo = 100
        account.outgoing_transfer(120)
        self.assertEqual(account.saldo, 100, "Outgoing transfer with amount greater than saldo passed")

    def test_outgoing_transfer_with_promo_code(self):
        account = PersonalAccount(self.personal_data["name"], self.personal_data["surname"],
                                  self.personal_data["pesel"], "PROM_123")
        account.outgoing_transfer(20)
        self.assertEqual(account.saldo, 30, "Outgoing transfer with promo code is not working")

    def test_series_of_transfers(self):
        account = PersonalAccount(self.personal_data["name"], self.personal_data["surname"],
                                  self.personal_data["pesel"])
        account.saldo = 100
        account.outgoing_transfer(50)
        account.incoming_transfer(20)
        account.outgoing_transfer(30)
        self.assertEqual(account.saldo, 40, "Multiple transfers are not working")

