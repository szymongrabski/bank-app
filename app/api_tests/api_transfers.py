import requests
import unittest
from ..AccountRegister import AccountRegister


class TestApiTransfers(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/api/accounts"
        requests.post(self.url, json={"name": "Szymon", "surname": "Głównytestowy", "pesel": "11111111111"})

    def test_api_transfer_with_wrong_pesel(self):
        response = requests.post(self.url + "/11111111112/transfer", json={"type": "incoming", "amount": 200})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "Account not found"})

    def test_api_transfer_wrong_body(self):
        response = requests.post(self.url + "/11111111111/transfer", json={"type": "outgoing"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "Missing fields: amount and type"})

    def test_api_incoming_transfer(self):
        response = requests.post(self.url + "/11111111111/transfer", json={"type": "incoming", "amount": 200})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Incoming transfer accepted to realisation"})
        account = requests.get(self.url + "/11111111111").json()["account"]
        self.assertEqual(account["saldo"], 200)

    def test_api_outgoing_transfer_with_wrong_amount(self):
        response = requests.post(self.url + "/11111111111/transfer", json={"type": "outgoing", "amount": 200})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Outgoing transfer accepted to realisation"})
        account = requests.get(self.url + "/11111111111").json()["account"]
        self.assertEqual(account["saldo"], 0)

    def test_api_outgoing_transfer(self):
        requests.post(self.url + "/11111111111/transfer", json={"type": "incoming", "amount": 500})
        response = requests.post(self.url + "/11111111111/transfer", json={"type": "outgoing", "amount": 300})
        self.assertEqual(response.status_code, 200)
        account = requests.get(self.url + "/11111111111").json()["account"]
        self.assertEqual(account["saldo"], 200)

    def tearDown(self):
        requests.delete("http://localhost:5000/api/accounts/delete/11111111111")
