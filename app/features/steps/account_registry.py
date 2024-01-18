from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"


@when('I create an account using name: "{name}", last name: "{surname}", pesel: "{pesel}"')
def create_account(context, name, surname, pesel):
    json_body = {"name": f"{name}",
                 "surname": f"{surname}",
                 "pesel": f"{pesel}"
    }
    create_resp = requests.post(URL + "/api/accounts", json=json_body)
    assert_equal(create_resp.status_code, 201)


@step('Number of accounts in registry equals: "{count}"')
def count_accounts_number_in_account_register(context, count):
    how_many_accounts = requests.get(URL + f"/api/accounts/count")
    assert_equal(how_many_accounts.json()["active_accounts"], int(count))


@step('Account with pesel "{pesel}" exists in registry')
def check_if_account_with_pesel_exists(context, pesel):
    account = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(account.status_code, 200)
    assert_equal(account.json()["account"]["pesel"], pesel)


@step('Account with pesel "{pesel}" does not exists in registry')
def check_if_account_with_pesel_does_not_exists(context, pesel):
    account = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(account.status_code, 404)


@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    resp = requests.delete(URL + f"/api/accounts/delete/{pesel}")
    assert_equal(resp.status_code, 200)
    assert_equal(resp.json()["message"], "Account deleted")


@when('I save the account registry')
def save_account(context):
    resp = requests.patch(URL + f"/api/accounts/save")
    assert_equal(resp.status_code, 200)


@when('I load the account registry')
def load_account_register(context):
    resp = requests.patch(URL + f"/api/accounts/load")
    assert_equal(resp.status_code, 200)


@when('I update last name in account with pesel "{pesel}" to "{surname}"')
def update_surname(context, pesel, surname):
    json_body = {"surname": f"{surname}"}
    resp = requests.patch(URL + f"/api/accounts/update/{pesel}", json=json_body)
    assert_equal(resp.status_code, 202)


@then('Last name in account with pesel "{pesel}" is "{surname}"')
def check_surname(context, pesel, surname):
    account = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(account.status_code, 200)
    assert_equal(account.json()["account"]["surname"], surname)
