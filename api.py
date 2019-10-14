from flask import Flask, jsonify, request, abort
from nano_pow import mine_block, check_balance, miner_account, url
from nanolib import Block

import requests
import json

app = Flask(__name__)


@app.route('/opening_request', methods=['GET', 'POST'])
def opening_request():
    return miner_account


@app.route('/request_block_mine', methods=['GET', 'POST'])
def request_block_mine():
    data = request.get_json()
    if data:
        miner = data.get("miner_transaction")
        user = data.get("user_transaction")
        miner_block = Block(
            block_type=miner.get('block_type'),
            account=miner.get('account'),
            representative=miner.get('representative'),
            previous=miner.get('previous'),
            link_as_account=miner_account,
            balance=miner.get('balance')
        )
        miner_block_hash = miner_block.work_block_hash
        if check_balance(miner.get('account'), miner.get('balance')):
            miner_block.solve_work()
            miner_block_json = json.loads(miner_block.json())
            miner_block_new_json = {
                "account": miner_block_json.get("account"),
                "balance": miner_block_json.get("balance"),
                "link": miner_block_json.get("link"),
                "link_as_account": miner_block_json.get("link_as_account"),
                "previous": miner_block_json.get("previous"),
                "representative": miner_block_json.get("representative"),
                "type": miner_block_json.get("type"),
                "signature": miner.get("signature")
            }
            requests.post(url, json={"action": "process", "block": miner_block_new_json})
            user_transaction = mine_block(user.get('block_type'), user.get('account'), user.get('representative'), miner_block_hash, user.get('link_as_account'), user.get('balance'))
            user_transaction_json = json.loads(user_transaction.json())
            user_transaction_new_json = {
                "account": user_transaction_json.get("account"),
                "balance": user_transaction_json.get("balance"),
                "link": user_transaction_json.get("link"),
                "link_as_account": user_transaction_json.get("link_as_account"),
                "previous": user_transaction_json.get("previous"),
                "representative": user_transaction_json.get("representative"),
                "type": user_transaction_json.get("type"),
                "signature": user.get("signature")
            }
            r = requests.post(url, json={"action": "process", "block": user_transaction_new_json})
            return jsonify(r.text)
    abort(401)
