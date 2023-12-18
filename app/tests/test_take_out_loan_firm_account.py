import unittest
from ..FirmAccount import FirmAccount
from parameterized import parameterized
from unittest.mock import patch

class TestTakeOutLoanByFirmAccount(unittest.TestCase):
    firm_name = "TestFirm"
    nip = "1234567890"

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def setUp(self, mock_check_nip):
        mock_check_nip.return_value = True
        self.account = FirmAccount(self.firm_name, self.nip)
    @parameterized.expand([
        ([-1775], 500, 100, True, 600, "Loan taken by firm account with two right conditions is not working"),
        ([100, 200], 500, 100, False, 500, "Loan taken by firm account without outcoming transfer from ZUS passed"),
        ([-1775], 200, 400, False, 200, "Loan taken by firm account with saldo smaller than expected loan amount passed"),
        ([-1775], 500, -100, False, 500, "Loan taken by firm account with negative amount passed")

    ])
    def test_taking_out_loan_by_firm_account(self, transfer_history, saldo, expected_loan_amount, expected_loan_ability, expected_saldo, msg):
        self.account.transfer_history = transfer_history
        self.account.saldo = saldo
        loan_abillity = self.account.take_out_loan(expected_loan_amount)
        self.assertEqual(loan_abillity, expected_loan_ability, f"{msg} - Loan ability mismatch")
        self.assertEqual(self.account.saldo, expected_saldo, f"{msg} - Saldo mismatch")