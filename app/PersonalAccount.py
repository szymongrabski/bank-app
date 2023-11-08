from .Account import Account



class PersonalAccount(Account):

    def __init__(self, name, surname, pesel, discount_code=None):

        super().__init__()

        self.name = name

        self.surname = surname

        if len(pesel) != 11:

            self.pesel = "Wrong pesel"
        else:

            self.pesel = pesel


        if self.is_discount_code_correct(discount_code) and self.is_born_after_1960(pesel):

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


    def is_born_after_1960(self, pesel):

        year = int(pesel[0:2])

        month = int(pesel[2:4])


        if year > 60:

            return True

        elif month > 20:

            return True
        else:

            return False


