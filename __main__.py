from argparse import ArgumentParser
from Crypto.Cipher import AES
from getpass import getpass
from sys import exit
from smtplib import SMTP
from random import randint

import csv
import logging

from passphase import Passphase

def _exit(msg):
    logger.error(msg)
    exit(1)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

parser = ArgumentParser(description='Revain wallets generator')

parser.add_argument('-btc', help="Generate BTC (Bitcoin) wallets", default=0, type=int)
parser.add_argument('-eth', help="Generate ETH (Ethereum) wallets", default=0, type=int)
parser.add_argument('-dash', help="Generate DASH (Dash) wallets", default=0, type=int)
parser.add_argument('-xmr', help="Generate XMR (Monero) wallets", default=0, type=int)
parser.add_argument('-zcash', help="Generate ZEC (ZCash) wallets", default=0, type=int)

parser.add_argument('-k', '--keys', help="Number of keys", default=0, type=int)
parser.add_argument('-g', '--generate', help="Generate keys", default=0, type=int)
parser.add_argument('-w', '--wordlist', help="Path to wordlist file", default="wallets/wordlist.txt")
parser.add_argument('-d', '--dir', help="Directory to store wallets", default="valets_{}".format(randint(200, 900)))

if __name__ == "__main__":
    options = parser.parse_args()

    if options.generate > 0: # Generate new keys for private keys encryption
        logger.info("Generating {} new keys".format(options.generate))

        try: # Loading wordlist
            p = Passphase(options.wordlist)
        except Exception as e:
            _exit("Can't open wordlist file, current path: {}".format(options.wordlist))

        try: # Checking SMTP service
            smtp = SMTP('localhost')
        except Exception as e:
            _exit("Can't connect to the SMTP provider ({})".format(e))

        # Getting email addresses from users
        emails = []
        for i in range(1, options.generate + 1):
            new_email = input("{}. Enter your email: ".format(i))
            emails.append(new_email)

        # Generating passphrases
        passphrases = {}
        for email in emails:
            passphrases[email] = p.get_phrase(12)

        # Sending passphrases
        for email in passphrases.keys():
            msg = """
            ============ ALERT ALERT ALERT ============
            Your passphrase is: {}
            You need {} more passphrases to unlock the funds.

            Best wishes,
            Valets
            """.format(' '.join(passphrases[email]), options.generate - 1)
            try:
                smtp.sendmail("bot@revain.org", [email], msg)
                logger.info("Successfully sent email to {}".format(email))
            except Exception as e:
                _exit("Can't send email to {}: {}".format(email, e))

    if options.btc > 0: # Generate BTC wallets
        from coins.BTC import BitcoinWallet
        w = BitcoinWallet()

        for i in range(options.btc):
            pk = w.get_private_key()
            address = w.get_address(pk)
            print (pk, address)
