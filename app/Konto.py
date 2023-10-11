class Konto:
    def __init__(self, imie, nazwisko, pesel, discount_code = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Wrong pesel"
        else :
            self.pesel = pesel
        
        if self.is_discount_code_correct(discount_code):
            self.saldo = 50
        else:
            self.saldo = 0
    
    def is_discount_code_correct(self, discount_code):
        if discount_code is None:
            return False
        if discount_code.startswith("PROM_") and len(discount_code) == 8:
            return True
        else:
            return False

