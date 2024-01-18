from .PersonalAccount import PersonalAccount
from pymongo import MongoClient

class AccountRegister:
    client = MongoClient('localhost', 27017)
    db = client['bankApp']
    collection = db['account_register']
    account_list = []


    @classmethod
    def add_to_account_register(cls, account):
        if isinstance(account, PersonalAccount):
            cls.account_list.append(account)

    @classmethod
    def count_how_much_accounts_in_register(cls):
        return len(cls.account_list)

    @classmethod
    def find_account_in_register_by_pesel(cls, pesel):
        for account in cls.account_list:
            if account.pesel == pesel:
                return account
        return None

    @classmethod
    def delete_account(cls, pesel):
        for account in cls.account_list:
            if account.pesel == pesel:
                cls.account_list.remove(account)

    @classmethod
    def save(cls):
        cls.collection.delete_many({})
        for account in cls.account_list:
            cls.collection.insert_one(
                {
                    "name": account.name,
                    "surname": account.surname,
                    "pesel": account.pesel,
                    "saldo": account.saldo,
                    "transfer_history": account.transfer_history,
                }
            )

    @classmethod
    def load(cls):
        cls.account_list = []
        for account in cls.collection.find():
            acc = PersonalAccount(account["name"], account["surname"], account["pesel"])
            acc.saldo = account["saldo"]
            acc.transfer_history = account["transfer_history"]
            cls.account_list.append(acc)

