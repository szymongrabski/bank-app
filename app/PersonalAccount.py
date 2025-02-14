from .Account import Account
from datetime import date

class PersonalAccount(Account):

    def __init__(self, name, surname, pesel, discount_code=None):
        super().__init__()
        self.name = name
        self.surname = surname
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Wrong pesel"
        else:
            self.pesel = pesel

        if self.is_discount_code_correct(discount_code) and self.is_born_after_1960(pesel):
            self.saldo = 50
        else:
            self.saldo = 0

    def take_out_loan(self, amount):
        if self.are_n_latest_transfers_incoming(3) or self.count_sum_of_n_latest_transfers(5) >= amount:
            self.saldo += amount
            return True
        return False

    def are_n_latest_transfers_incoming(self, n):
        if len(self.transfer_history) < n:
            return False
        for transfer in self.transfer_history[-n:]:
            if transfer < 0:
                return False
        return True

    def count_sum_of_n_latest_transfers(self, n):
        if len(self.transfer_history) < n:
            return False
        return sum(self.transfer_history[-n:])

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

    def send_transfer_history_by_mail(self, adresat, smtp_connection):
        today_date = date.today().strftime("%Y-%m-%d")
        subject = f"Wyciąg z dnia {today_date}"
        content = f"Twoja historia konta to: {self.transfer_history}"

        return smtp_connection.send(subject, content, adresat)