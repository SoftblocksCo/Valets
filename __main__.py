from argparse import ArgumentParser
from Crypto.Cipher import AES
from getpass import getpass
from sys import exit
from smtplib import SMTP
from random import randint
from os import makedirs
from os import urandom
from termcolor import colored
from csv import writer
from utils import write_same_line
from signal import signal
from signal import SIGINT
from importlib import import_module

import logging

def _exit(msg):
    logger.error(msg)
    exit(1)

def handler(signum, frame):
    print("")
    _exit("Ctrl+C pressed, exit")
signal(SIGINT, handler=handler)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

parser = ArgumentParser(description='Revain wallets generator')

parser.add_argument('-save', default='', type = str,
    help="Enable save mode for wallets generation. Argument - strong password for private keys encription")

parser.add_argument('-btc', help="Generate BTC (Bitcoin) wallets", default=0, type=int)
parser.add_argument('-eth', help="Generate ETH (Ethereum) wallets", default=0, type=int)
parser.add_argument('-etc', help="Generate ETC (Ethereum classic) wallets", default=0, type=int)
parser.add_argument('-ltc', help="Generate LTC (Litecoin) wallets", default=0, type=int)
parser.add_argument('-dash', help="Generate DASH (Dash) wallets", default=0, type=int)
parser.add_argument('-xmr', help="Generate XMR (Monero) wallets", default=0, type=int)
parser.add_argument('-zcash', help="Generate ZEC (ZCash) wallets", default=0, type=int)

parser.add_argument('-d', '--dir', help="Directory to store wallets", default="_valets_{}".format(urandom(8).hex()))
parser.add_argument('-c', '--coins', help="Specify coins for wallets generation", required=True, type=str, nargs='+', action='append')

if __name__ == "__main__":
    options = parser.parse_args()
    try: # Trying to init NEW directory for storing wallets
        makedirs(options.dir)
        logger.info("Wallets folder: {}/".format(options.dir))
    except Exception as e:
        _exit(e)

    for coin, wallets_amount in options.coins: # Iterate on every coin
        wallets_amount = int(wallets_amount)

        logger.info("Generating {} {} wallets".format(wallets_amount, coin))

        try: # Trying to init wallet class
            wallet_module = import_module("coins.{}".format(coin)) # Import API module for specific wallet
            w = getattr(wallet_module, "{}_wallet".format(coin))()
        except Exception as e:
            _exit(e)

        with open("{}/{}.csv".format(options.dir, coin), "a") as wallet_file:
            wallet_writer = writer(wallet_file)

            if coin in ['ETH', 'ETC']:
                wallet_writer.writerow(('Passphase', 'Address', 'Keystore'))
            else:
                wallet_writer.writerow(('Private_key', 'Address'))

            # Generate adresses & private keys
            for i in range(1, wallets_amount+1):
                if coin in ['ETH', 'ETC']: # Ethereum like coins have a special wallet structure
                    passphase = urandom(16).hex()
                    address = w.get_address(passphase)
                    keystore = w.get_keystore_file(address)
                    wallet_writer.writerow((passphase, address, keystore))

                    wallet_writer.writerow((passphase, address, keystore)) # Store wallet info
                else:
                    address = w.get_address()
                    private_key = w.get_private_key(address)
                    wallet_writer.writerow((private_key, address))

                    wallet_writer.writerow((private_key, address)) # Store wallet info

                write_same_line("New {} address ({}): {}".format(coin, i, address))
            print ("")


            logger.info("{} {} addresses generated successfully".format(wallets_amount, coin))
