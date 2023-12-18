import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount
from datetime import date


class TestSendHistoryByEmail(unittest.TestCase):
    name = "Szymon"
    surname = "Testowy"
    pesel = "03245678901"

    firm_name = "SG"
    nip = "8461627563"

    def test_send_history_personal_account_success(self):
        account = PersonalAccount(self.name, self.surname, self.pesel)
        account.saldo = 1000
        account.incoming_transfer(200)
        account.outgoing_transfer(500)

        smtp_connection = MagicMock()
        smtp_connection.send = MagicMock(return_value = True)

        status = account.send_transfer_history_by_mail("test@gmail.com", smtp_connection)
        self.assertTrue(status)

        smtp_connection.send.assert_called_once_with(
            f"Wyciąg z dnia {date.today().strftime("%Y-%m-%d")}",
            "Twoja historia konta to: [200, -500]",
            "test@gmail.com"
        )

    def test_send_history_personal_account_failure(self):
        account = PersonalAccount(self.name, self.surname, self.pesel)
        account.saldo = 1000
        account.incoming_transfer(200)
        account.outgoing_transfer(500)

        smtp_connection = MagicMock()
        smtp_connection.send = MagicMock(return_value = False)

        status = account.send_transfer_history_by_mail("test@gmail.com", smtp_connection)
        self.assertFalse(status)

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_send_history_firm_account_success(self, mock_check_nip):
        mock_check_nip.return_value = True
        account = FirmAccount(self.firm_name, self.nip)

        account.saldo = 1000
        account.incoming_transfer(200)
        account.outgoing_transfer(500)

        smtp_connection = MagicMock()
        smtp_connection.send = MagicMock(return_value = True)

        status = account.send_transfer_history_by_mail("test@gmail.com", smtp_connection)
        self.assertTrue(status)

        smtp_connection.send.assert_called_once_with(
            f"Wyciąg z dnia {date.today().strftime("%Y-%m-%d")}",
            "Historia konta twojej firmy to: [200, -500]",
            "test@gmail.com"
        )

    @patch('app.FirmAccount.FirmAccount.check_nip')
    def test_send_history_firm_account_failure(self, mock_check_nip):
        mock_check_nip.return_value = True
        account = FirmAccount(self.firm_name, self.nip)

        account.saldo = 1000
        account.incoming_transfer(200)
        account.outgoing_transfer(500)

        smtp_connection = MagicMock()
        smtp_connection.send = MagicMock(return_value = False)

        status = account.send_transfer_history_by_mail("test@gmail.com", smtp_connection)
        self.assertFalse(status)



