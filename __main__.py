from configparser import ConfigParser
from argparse import ArgumentParser
from Crypto.Cipher import AES
from getpass import getpass
from sys import exit
from smtplib import SMTP
from random import randint
from os import makedirs
from os import urandom
from csv import writer
from utils import write_same_line
from signal import signal
from signal import SIGINT
from importlib import import_module

from api.rpc_bitcoin import Bitcoin_like_wallet
from api.rpc_ethereum import Ethereum_like_wallet

from multiprocessing.pool import ThreadPool as Pool
from functools import partial

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

# General Valets options
parser.add_argument('-d', '--dir', help="Directory to store wallets", default="_valets_{}".format(urandom(8).hex()))
parser.add_argument('-c', '--coins', help="Specify coins for wallets generation, e.g. '-c BTC 100'", required=True, type=str, nargs='+', action='append')
parser.add_argument('-i', '--ini', help="Path to the .ini file", default="./Valets/config.ini")
parser.add_argument('-p', '--pool', help="Size of pool for wallets generator", default=10, type=int)

def generate_new_wallet(w, coin, i):
    if coin in ['ETH', 'ETC']: # Ethereum, Ethereum classic
        passphase = urandom(16).hex()
        address = w.get_address(passphase)
        keystore = w.get_keystore_file(address)

        full_credentials = (passphase, address, keystore)
        save_credentials = ('passphase', address, 'keystore')
    else: # Bitcoin, Litecoin, Dash, Dogecoin, ....
        address = w.get_address()
        private_key = w.get_private_key(address)

        full_credentials = (private_key, address)
        save_credentials = ('private_key', address)

    write_same_line("New {} address ({}): {}".format(coin, i, address))

    return {'full' : full_credentials, 'save' : save_credentials}

if __name__ == "__main__":
    options = parser.parse_args()

    parser = ConfigParser()
    parser.read(options.ini)

    try: # Trying to init NEW directory for storing wallets
        makedirs(options.dir)
        logger.info("Wallets folder: {}/".format(options.dir))
    except Exception as e:
        _exit(e)

    for coin, wallets_amount in options.coins: # Iterate on every coin
        wallets_amount = int(wallets_amount)

        logger.info("Generating {} {} wallets".format(wallets_amount, coin))

        full_wallet_file = open("{}/full_{}.csv".format(options.dir, coin), 'a')
        full_wallet_writer = writer(full_wallet_file)

        save_wallet_file = open("{}/save_{}.csv".format(options.dir, coin), 'a')
        save_wallet_writer = writer(save_wallet_file)

        if coin in ['ETH', 'ETC']:
            full_wallet_writer.writerow(('Passphase', 'Address', 'Keystore'))
            save_wallet_writer.writerow(('Passphase', 'Address', 'Keystore'))
            w = Ethereum_like_wallet(name=coin, parser=parser)
        else:
            full_wallet_writer.writerow(('Private_key', 'Address'))
            save_wallet_writer.writerow(('Private_key', 'Address'))
            w = Bitcoin_like_wallet(name=coin, parser=parser)

        # Generate <wallets_amount> adresses & private keys in pool
        p = Pool(options.pool)

        partial_generate_new_wallets = partial(generate_new_wallet, w, coin)

        wallets_credentials = p.map(partial_generate_new_wallets, range(wallets_amount))
        p.close()
        p.join()

        print ("") # Because 'write_same_line' don't use \n

        # Save wallets credentials
        logger.info("Writing {} wallets credentials".format(coin))
        for wallet_credential in wallets_credentials:
            full_wallet_writer.writerow(wallet_credential['full'])
            save_wallet_writer.writerow(wallet_credential['save'])

        # Close files and move to the next coin
        full_wallet_file.close()
        save_wallet_file.close()

        logger.info("{} {} addresses generated successfully".format(wallets_amount, coin))
