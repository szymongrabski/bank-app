import unittest
from unittest.mock import patch
from ..AccountRegister import AccountRegister
from ..PersonalAccount import PersonalAccount

class TestAccountRegister(unittest.TestCase):
    @patch('app.AccountRegister.AccountRegister.collection')
    def test_load_accounts_from_database(self, mock_collection):
        mock_collection.find.return_value = [
            {"name": "Jan", "surname": "Kowalski", "pesel": "89092909875", "saldo": 1000, "transfer_history": []}
        ]
        AccountRegister.load()
        self.assertEqual(len(AccountRegister.account_list), 1)
        self.assertEqual(AccountRegister.account_list[0].name, 'Jan')

    @patch("app.AccountRegister.AccountRegister.collection")
    def test_save_accounts_to_database(self, mock_collection):
        mock_collection.find.return_value = [{
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "12345678900",
            "saldo": 0,
            "transfer_history": []
        },
        {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "12345678901",
            "saldo": 0,
            "transfer_history": []
        }]
        AccountRegister.load()
        self.assertEqual(AccountRegister.count_how_much_accounts_in_register(), 2)
        AccountRegister.add_to_account_register(PersonalAccount("Jan", "Kowalski", "12345678902"))
        self.assertEqual(AccountRegister.count_how_much_accounts_in_register(), 3)
        mock_collection.find.return_value.append({
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "pesel": "12345678902",
            "saldo": 0,
            "transfer_history": []
        })
        AccountRegister.save()
        AccountRegister.delete_account("12345678902")
        mock_collection.find.return_value.pop()
        AccountRegister.load()
        self.assertEqual(AccountRegister.count_how_much_accounts_in_register(), 2)