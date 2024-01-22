import requests
import unittest

class TestCreateAndDeleteAccount(unittest.TestCase):
    def test_create_and_delete_account(self):
        url = 'http://localhost:5000/api/accounts'
        for i in range(100):
            pesel = str(i).zfill(11)
            create_response = requests.post(url, json={
                "name": "Jan",
                "surname": "Kowalski",
                "pesel": pesel
            }, timeout=2)
            self.assertEqual(create_response.status_code, 201)
            delete_response = requests.delete(f"{url}/delete/{pesel}", timeout=2)
            self.assertEqual(delete_response.status_code, 200)