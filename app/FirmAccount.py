from .Account import Account
import requests
from datetime import date


class FirmAccount(Account):
    def __init__(self, firm_name, nip):
        super().__init__()
        if len(nip) != 10:
            self.nip = "Wrong NIP"
        else:
            if self.check_nip(nip):
                self.nip = nip
            else:
                raise Exception("NIP not in GOV database")
        self.firm_name = firm_name
        self.express_transfer_fee = 5

    def take_out_loan(self, amount):
        if amount < 0:
            return False
        elif -1775 in self.transfer_history and self.saldo >= amount * 2:
            self.saldo += amount
            return True
        else:
            return False

    def check_nip(self, nip):
        today_date = date.today().strftime("%Y-%m-%d")
        response = requests.get(f"https://wl-test.mf.gov.pl/api/search/nip/{nip}?date={today_date}")

        if response.status_code == 200:
            print("True")
            return True
        else:
            print("False")
            return False

    def send_transfer_history_by_mail(self, adresat, smtp_connection):
        today_date = date.today().strftime("%Y-%m-%d")
        subject = f"Wyciąg z dnia {today_date}"
        content = f"Historia konta twojej firmy to: {self.transfer_history}"

        return smtp_connection.send(subject, content, adresat)
