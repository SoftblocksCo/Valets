from subprocess import check_output

class DASH_wallet():
    def __init__(self):
        # Dashd should already be started
        # Otherwise exception will be raised
        tmp_address = check_output(['dash-cli', 'getnewaddress'])

    def get_private_key(self, address):
        """Get private key for address with dash-cli"""
        private_key = check_output(['dash-cli', 'dumpprivkey', address])
        private_key = private_key.rstrip() # Remove end line symbol

        return private_key.decode('utf-8')

    def get_address(self):
        """Generate new address with dash-cli"""
        address = check_output(['dash-cli', 'getnewaddress'])
        address = address.rstrip() # Remove end line symbol

        return address.decode('utf-8')
