import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "03245678901"
    discount_code = "PROMO_123"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel)

    #tutaj proszę dodawać nowe testy

    def test_pesel_with_len_10(self):
        account = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(account.pesel, "Wrong pesel", "Za krótki pesel został przyjęty za prawidłowy")

    def test_pesel_with_len_12(self):
        account = Konto(self.imie, self.nazwisko, "123456789000")
        self.assertEqual(account.pesel, "Wrong pesel", "Za długi pesel został przyjęty za prawidłowy")

    def test_empty_pesel(self):
        account = Konto(self.imie, self.nazwisko, "")
        self.assertEqual(account.pesel, "Wrong pesel", "Pusty pesel został przyjęty za prawidłowy")
    
    # Feature 4 - discount code

    def test_discount_with_wrong_prefix(self):
        account = Konto(self.imie, self.nazwisko, self.pesel, "PRIMO_123")
        self.assertEqual(account.saldo, 0, "Wrong prefix in discount code passed")

    def test_discount_with_wrong_suffix(self):
        account = Konto(self.imie, self.nazwisko, self.pesel, "PROMO_1234")
        self.assertEqual(account.saldo, 0, "Wrong suffix in discount code passed")

    def test_discount_with_wrong_length(self):
        account = Konto(self.imie, self.nazwisko, self.pesel, "PROMOU_12345")
        self.assertEqual(account.saldo, 0, "Wrong length in discount code passed")

    def test_discount_promo(self):
        account = Konto(self.imie, self.nazwisko, self.pesel, "")
        self.assertEqual(account.saldo, 0, "Empty discount code passed")

    # Feature 5 - born after 1960

    def test_discount_year_59(self):
        account = Konto(self.imie, self.nazwisko, "59010100000", self.discount_code)
        self.assertEqual(account.saldo, 0, "Born in 1959 passed")

    def test_discount_year_61(self):
        account = Konto(self.imie, self.nazwisko, "61010100000", self.discount_code)
        self.assertEqual(account.saldo, 0, "Born in 1961 passed")

    def test_discount_year_60(self):
        account = Konto(self.imie, self.nazwisko, "60010100000", self.discount_code)
        self.assertEqual(account.saldo, 0, "Born in 1960 passed")
    
    def test_discount_year_2001(self):
        account = Konto(self.imie, self.nazwisko, "01260100000", self.discount_code)
        self.assertEqual(account.saldo, 0, "Born in 2001 passed")
    
    def test_discount_year_2001_wrong_discount_code(self):
        account = Konto(self.imie, self.nazwisko, "01260100000", "PROMOU_12")
        self.assertEqual(account.saldo, 0, "Born in 2001 and with wrong discount code passed")

    