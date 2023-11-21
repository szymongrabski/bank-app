from .PersonalAccount import PersonalAccount


class AccountRegister:
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
                return True
        return False

