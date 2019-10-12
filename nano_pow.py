from nanolib import Block
import json
import requests

with open('config.json') as config_file:
    data = json.load(config_file)

miner_account = data['nano_address']
url = data['nano_url']


def mine_block(block_type, account, representative, previous, link_as_account, balance):
    block = Block(
        block_type=block_type,
        account=account,
        representative=representative,
        previous=previous,
        link_as_account=link_as_account,
        balance=balance
    )
    block.solve_work()
    return block.json()


def check_balance(address, balance):
    data = {
        "action": "account_balance",
        "account": address
    }
    resp = json.loads(requests.post(url, json=data).text)
    if int(resp['balance']) >= int(balance):
        return True
    return False
