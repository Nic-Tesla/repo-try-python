#1-25-00
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware

http_provider = 'https://bsc-dataseed.binance.org'
web3 = Web3(Web3.HTTPProvider(http_provider))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

a = web3.fromWei()



