from brownie import accounts, config, MyFirstContract

def main():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    my_first_contract = MyFirstContract[-1]
    tx = my_first_contract.setNumber(12345, {'from': account})
    tx.wait(1)
    print("number is", my_first_contract.getNumber())