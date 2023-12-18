import unittest

from ..PersonalAccount import PersonalAccount

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "03245678901"
    discount_code = "PROM_123"
    def test_tworzenie_konta(self):
        pierwsze_konto = PersonalAccount(self.name, self.surname, self.pesel)
        self.assertEqual(pierwsze_konto.name, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.surname, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel)

    def test_pesel_with_len_10(self):
        account = PersonalAccount(self.name, self.surname, "1234567890")
        self.assertEqual(account.pesel, "Wrong pesel", "Za krótki pesel został przyjęty za prawidłowy")

    def test_pesel_with_len_12(self):
        account = PersonalAccount(self.name, self.surname, "123456789000")
        self.assertEqual(account.pesel, "Wrong pesel", "Za długi pesel został przyjęty za prawidłowy")

    def test_empty_pesel(self):
        account = PersonalAccount(self.name, self.surname, "")
        self.assertEqual(account.pesel, "Wrong pesel", "Pusty pesel został przyjęty za prawidłowy")

    # Feature 4 - discount code

    def test_discount_code(self):
        account = PersonalAccount(self.name, self.surname, self.pesel, "PROM_123")
        self.assertEqual(account.saldo, 50, "Correct discount code is not working")

    def test_discount_with_wrong_prefix(self):
        account = PersonalAccount(self.name, self.surname, self.pesel, "PRIMO_123")
        self.assertEqual(account.saldo, 0, "Wrong prefix in discount code passed")

    def test_discount_with_wrong_suffix(self):
        account = PersonalAccount(self.name, self.surname, self.pesel, "PROMO_1234")
        self.assertEqual(account.saldo, 0, "Wrong suffix in discount code passed")

    def test_discount_with_wrong_length(self):
        account = PersonalAccount(self.name, self.surname, self.pesel, "PROMOU_12345")
        self.assertEqual(account.saldo, 0, "Wrong length in discount code passed")

    def test_discount_promo(self):
        account = PersonalAccount(self.name, self.surname, self.pesel, "")
        self.assertEqual(account.saldo, 0, "Empty discount code passed")

    # Feature 5 - born after 1960

    def test_discount_year_59(self):
        account = PersonalAccount(self.name, self.surname, "59010100000", self.discount_code)
        self.assertEqual(account.saldo, 0, "Born in 1959 passed")

    def test_discount_year_61(self):
        account = PersonalAccount(self.name, self.surname, "61010100000", self.discount_code)
        self.assertEqual(account.saldo, 50, "Born in 1961 is not working")

    def test_discount_year_60(self):
        account = PersonalAccount(self.name, self.surname, "60010100000", self.discount_code)
        self.assertEqual(account.saldo, 0, "Born in 1960 passed")

    def test_discount_year_2001(self):
        account = PersonalAccount(self.name, self.surname, "01260100000", self.discount_code)
        self.assertEqual(account.saldo, 50, "Born in 2001 is not working")

    def test_discount_year_2001_wrong_discount_code(self):
        account = PersonalAccount(self.name, self.surname, "01260100000", "PROMOU_12")
        self.assertEqual(account.saldo, 0, "Born in 2001 and with wrong discount code passed")

