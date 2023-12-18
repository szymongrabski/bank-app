import requests
import unittest
from ..AccountRegister import AccountRegister


class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/api/accounts"
        requests.post(self.url, json={"name": "Szymon", "surname": "Głównytestowy", "pesel": "11111111111"})

    def test_create_account(self):
        response = requests.post(self.url, json={"name": "Dariusz", "surname": "Testowy", "pesel": "03245678901"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "Created account"})

    def test_create_account_with_not_unique_pesel(self):
        response = requests.post(self.url, json={"name": "Dariusz", "surname": "Podtestowy", "pesel": "11111111111"})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), {"message": "Pesel is not unique"})

    def test_count_accounts(self):
        response = requests.get(self.url + "/count")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"active_accounts": 1})

    def test_get_account_by_pesel(self):
        response = requests.get(self.url + "/11111111111")
        self.assertEqual(response.status_code, 200)
        self.assertIn("account", response.json())

    def test_get_account_by_wrong_pesel(self):
        response = requests.get(self.url + "/03245678902")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "Account not found"})

    def test_patch_account_with_all_values(self):
        response = requests.patch(
            self.url + "/update/11111111111",
            json={"name": "Tomasz", "surname": "Testow", "pesel": "11111111111", "saldo": 100}
        )
        self.assertEqual(response.status_code, 202)
        self.assertIn("updatedAccount", response.json())

    def test_patch_account_with_one_value(self):
        response = requests.patch(
            self.url + "/update/11111111111",
            json={"name": "Tomasz"}
        )
        self.assertEqual(response.status_code, 202)
        self.assertIn("updatedAccount", response.json())

    def test_patch_account_with_wrong_value(self):
        response = requests.patch(
            self.url + "/update/11111111111",
            json={"abc": "Tomasz"}
        )
        self.assertEqual(response.status_code, 400)

    def test_patch_account_with_wrong_pesel(self):
        response = requests.patch(
            self.url + "/update/12345678904",
            json={"name": "Tomasz", "surname": "Testow", "pesel": "12345678901", "saldo": 100}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "Account not found"})

    def test_delete_account(self):
        response = requests.delete(self.url + "/delete/11111111111")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Account deleted"})

    def test_delete_account_with_wrong_pesel(self):
        response = requests.delete(self.url + "/delete/12345678965")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "Account not found"})

    def tearDown(self):
        requests.delete("http://localhost:5000/api/accounts/delete/11111111111")

    @classmethod
    def tearDownClass(cls):
        requests.delete("http://localhost:5000/api/accounts/delete/03245678901")
