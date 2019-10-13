# dPoW-API

## How to run

    pip3 install -r requirements.txt
    export FLASK_APP=api.py
    python3 api.py

## How to run (Windows)

    pip3 install -r requirements.txt
    set FLASK_APP=hello.py
    python3 api.py

## How it works

You can call the endpoint (/request_block_mine) sending a json data like the following one:

      {
        "miner_transaction": {
            "block_type": "state",
            "account": "xrb_3rridbdhm8jkjyzaig6xqkfcg7oob47rk9zm5moeiququmg3t8toq66nyrs7",
            "representative": "xrb_3rridbdhm8jkjyzaig6xqkfcg7oob47rk9zm5moeiququmg3t8toq66nyrs7",
            "previous": "B0BE8ECADF6FF1182D49C578E3EFED66AC43095CBF9D55EC1C84DFAB1EE0B64F",
            "balance": 000000000000000000000000000001,
            "signature": "asdadjadja"
        },
        "user_transaction": {
            "block_type": "state",
            "account": "xrb_3rridbdhm8jkjyzaig6xqkfcg7oob47rk9zm5moeiququmg3t8toq66nyrs7",
            "representative": "xrb_3rridbdhm8jkjyzaig6xqkfcg7oob47rk9zm5moeiququmg3t8toq66nyrs7",
            "link_as_account": "xrb_3rridbdhm8jkjyzaig6xqkfcg7oob47rk9zm5moeiququmg3t8toq66nyrs7",
            "balance": 500000000000000000000000000000,
            "signature": "asdadjadja"
        }
    }	
    
   The first transaction is responsible for the payment of the miner and the second one is your real transaction. The miner mines his transaction before the user one to guarantee his payment.
    
