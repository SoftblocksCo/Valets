import requests
import json

class LTC_wallet():
    def __init__(self, options):
        self.USERNAME = options.ltc_rpc_user
        self.PASSWORD = options.ltc_rpc_pass
        self.PORT = options.ltc_rpc_port
        self.HOST = options.ltc_rpc_host

        self.ACCOUNT = options.ltc_rpc_account

        self.URL = "http://{}:{}@{}:{}".format(self.USERNAME, self.PASSWORD, self.HOST, self.PORT)
        self.HEADERS = {'content-type' : 'application/json'}

    def get_private_key(self, address):
        """Get private key for address with litecoin-cli RPC query"""
        payload = json.dumps({'method':'dumpprivkey', 'params' : [address], "jsonrpc": "2.0"})

        r = requests.post(self.URL, headers=self.HEADERS, data=payload)
        private_key = json.loads(r.text).get('result')

        return private_key

    def get_address(self):
        """Generate new address with litecoin-cli RPC query"""
        payload = json.dumps({'method':'getnewaddress', 'params' : [self.ACCOUNT], "jsonrpc": "2.0"})

        r = requests.post(self.URL, headers=self.HEADERS, data=payload)
        address = json.loads(r.text).get('result')

        return address
