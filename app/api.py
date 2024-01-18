import requests
from flask import Flask, request, jsonify
from .AccountRegister import AccountRegister
from .PersonalAccount import PersonalAccount

app = Flask(__name__)


@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Request stworzenia konta z danymi: {data}")
    account = PersonalAccount(data["name"], data["surname"], data["pesel"])

    foundAccount = AccountRegister.find_account_in_register_by_pesel(data["pesel"])
    if foundAccount:
        return jsonify({"message": "Pesel is not unique"}), 409

    AccountRegister.add_to_account_register(account)
    return jsonify({"message": "Created account"}), 201


@app.route("/api/accounts/count", methods=['GET'])
def how_many_accounts():
    accountsNumber = AccountRegister.count_how_much_accounts_in_register()
    return jsonify({"active_accounts": accountsNumber}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def find_account_by_pesel(pesel):
    foundAccount = AccountRegister.find_account_in_register_by_pesel(pesel)

    if (foundAccount is None):
        return jsonify({"message": "Account not found"}), 404
    else:
        return jsonify({"account": foundAccount.__dict__}), 200


@app.route("/api/accounts/update/<pesel>", methods=['PATCH'])
def update_account(pesel):
    foundAccount = AccountRegister.find_account_in_register_by_pesel(pesel)
    data = request.get_json()

    if foundAccount:
        if "name" in data:
            foundAccount.name = data["name"]
        elif "surname" in data:
            foundAccount.surname = data["surname"]
        elif "pesel" in data:
            foundAccount.pesel = data["pesel"]
        elif "saldo" in data:
            foundAccount.saldo = data["saldo"]
        else:
            return jsonify({"message": f"{data} does not match"}), 400
        return jsonify({"updatedAccount": f"{foundAccount.__dict__}"}), 202
    else:
        return jsonify({"message": "Account not found"}), 404


@app.route("/api/accounts/delete/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    foundAccount = AccountRegister.find_account_in_register_by_pesel(pesel)

    if foundAccount:
        AccountRegister.delete_account(pesel)
        return jsonify({"message": "Account deleted"}), 200
    else:
        return jsonify({"message": "Account not found"}), 404


@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def make_transfer(pesel):
    data = request.get_json()
    foundAccount = AccountRegister.find_account_in_register_by_pesel(pesel)

    if not foundAccount:
        return jsonify({"message": "Account not found"}), 404

    if "amount" not in data or "type" not in data:
        return jsonify({"message": "Missing fields: amount and type"}), 400

    if data["type"] == "incoming":
        foundAccount.incoming_transfer(data["amount"])
        return jsonify({"message": "Incoming transfer accepted to realisation"}), 200
    elif data["type"] == "outgoing":
        foundAccount.outgoing_transfer(data["amount"])
        return jsonify({"message": "Outgoing transfer accepted to realisation"}), 200


@app.route("/api/accounts/save", methods=["PATCH"])
def save_to_database():
    AccountRegister.save()
    return jsonify({"message": "Saved to database"}), 200


@app.route("/api/accounts/load", methods=["PATCH"])
def load_from_database():
    AccountRegister.load()
    accounts_number = AccountRegister.count_how_much_accounts_in_register()
    return jsonify({"message": f"Loaded from database", "accounts_number": accounts_number}), 200

