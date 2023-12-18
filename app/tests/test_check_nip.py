import unittest
from unittest.mock import patch
from ..FirmAccount import FirmAccount


class TestCheckNip(unittest.TestCase):
    name = "SGF"
    nip = "8461627563"

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_check_nip(self, mock_check_nip):
        mock_check_nip.return_value = True
        account = FirmAccount(self.name, self.nip)
        self.assertEqual(account.check_nip(account.nip), True, "Check NIP not working")

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_check_nip_with_short_nip(self, mock_check_nip):
        mock_check_nip.return_value = False
        account = FirmAccount(self.name, "111")
        self.assertEqual(account.nip, 'Wrong NIP')
        self.assertEqual(account.check_nip(account.nip), False, "Wrong NIP passed")

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_create_firm_account_with_wrong_nip(self, mock_check_nip):
        mock_check_nip.return_value = False
        with self.assertRaises(Exception) as context:
            account = FirmAccount(self.name, "1100111111")
        self.assertTrue("NIP not in GOV database" in str(context.exception))

    @patch('app.FirmAccount.requests.get')
    def test_create_account_with_get_200(self, mock_get):
        mock_get.return_value.status_code = 200
        account = FirmAccount(self.name, '8461627563')
        self.assertEqual(account.nip, '8461627563')

    @patch('app.FirmAccount.requests.get')
    def test_create_account_with_get_False(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception) as context:
            account = FirmAccount(self.name, '1234567897')
        self.assertTrue("NIP not in GOV database" in str(context.exception))
