import unittest
from ..PersonalAccount import PersonalAccount
from parameterized import parameterized


class TestTakeOutLoan(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "03245678901"

    def setUp(self):
        self.account = PersonalAccount(self.name, self.surname, self.pesel)

    @parameterized.expand([
        ([100, 100, 100], 500, True, 500, "Three incoming transfers are not working"),
        ([100, -50, 300, -100, 100], 100, True, 100, "Sum of five transfers is not working"),
        ([200, 200], 100, False, 0, "Too short transfer history passed"),
        ([100, 200, -300, 20, 10], 1000, False, 0, "Wrong sum of five transfers passed")
    ])
    def test_taking_out_loan(self, transfer_history, expected_loan_amount, expected_loan_ability, expected_saldo, msg):
        self.account.transfer_history = transfer_history
        loan_ability = self.account.take_out_loan(expected_loan_amount)
        self.assertEqual(loan_ability, expected_loan_ability, f"{msg} - Loan ability mismatch")
        self.assertEqual(self.account.saldo, expected_saldo, f"{msg} - Saldo mismatch")
