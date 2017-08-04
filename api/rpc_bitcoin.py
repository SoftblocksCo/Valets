import requests
import json

class Bitcoin_like_wallet():
    def __init__(self, name, parser):
        self.NAME = name

        self.USERNAME = parser.get(name, 'rpcuser')
        self.PASSWORD = parser.get(name, 'rpcpassword')
        self.PORT = parser.get(name, 'rpcport')
        self.HOST = parser.get(name, 'rpcbind')

        self.ACCOUNT = parser.get(name, 'account')

        self.URL = "http://{}:{}@{}:{}".format(self.USERNAME, self.PASSWORD, self.HOST, self.PORT)
        self.HEADERS = {'content-type' : 'application/json'}

    def get_private_key(self, address):
        """Get private key for address with currency-cli RPC query"""
        payload = json.dumps({'method':'dumpprivkey', 'params' : [address], "jsonrpc": "2.0"})

        r = requests.post(self.URL, headers=self.HEADERS, data=payload)
        private_key = json.loads(r.text).get('result')

        return private_key

    def get_address(self):
        """Generate new address with currency-cli RPC query"""
        if self.NAME == 'ZEC': # Accounts are unsupported in Zcass
            payload = json.dumps({'method':'getnewaddress', 'params' : [], "jsonrpc": "2.0"})
        else:
            payload = json.dumps({'method':'getnewaddress', 'params' : [self.ACCOUNT], "jsonrpc": "2.0"})

        r = requests.post(self.URL, headers=self.HEADERS, data=payload)
        address = json.loads(r.text).get('result')

        return address
