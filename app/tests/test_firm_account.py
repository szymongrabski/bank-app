import unittest
from unittest.mock import patch
from ..FirmAccount import FirmAccount


class TestFirmAccount(unittest.TestCase):
    name = "SGF"
    nip = "8461627563"

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_create_firm_account(self, mock_check_nip):
        mock_check_nip.return_value = True
        account = FirmAccount(self.name, self.nip)
        self.assertEqual(account.firm_name, self.name, "Wrong firm name passed")
        self.assertEqual(account.nip, self.nip, "Wrong nip passed")
        self.assertEqual(account.saldo, 0, "Wrong saldo passed")
    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_create_firm_account_with_incorrect_nip(self, mock_check_nip):
        mock_check_nip.return_value = True
        account = FirmAccount(self.name, "0123")
        self.assertEqual(account.nip, "Wrong NIP", "Wrong nip passed")

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_incoming_transfer(self, mock_check_nip):
        mock_check_nip.return_value = True
        account = FirmAccount(self.name, self.nip)
        account.incoming_transfer(100)
        self.assertEqual(account.saldo, 100, "Wrong saldo in incoming transfer in FirmAccount class")

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_outgoing_transfer(self, mock_check_nip):
        mock_check_nip.return_value = True
        account = FirmAccount(self.name, self.nip)
        account.saldo = 120
        account.outgoing_transfer(20)
        self.assertEqual(account.saldo, 100, "Wrong saldo in outgoing transfer in FirmAccount class")
