# Valets - simple cryptocurrency wallets generator
Written in Python 3. Made with love inside the [Revain](https://revain.org) company.

## What is it?
Imagine that you have an application, with allows users to work with cryptocurrencies. For example, you are using them for the payment receipt (ICO, invest fund, etc). It mean, that every user should have it's own address for Bitcoin, Ethereum, Zcash, Dash, Monero and much much more.

So, you'll need a lot of wallets.

Valets allows you to generate them automatically, so all you need is to use this addresses in your application.

## ⚠️ Warning ⚠️
### It's highly recommended not to use Valets on production machine.

## Features:
- Generate thousands of wallets for:
  - [Bitcoin](https://bitcoin.org/en/)
  - [Ethereum](https://www.ethereum.org/)
  - [Zcash](https://z.cash/) (Soon)
  - [Monero](https://getmonero.org/home) (Soon)
  - [Dash](https://www.dash.org/) (Soon)
- After generating wallets for some coin you'll get CSV file with life-critical information
  - Bitcoin - `Private key, address`
  - Ethereum - `Passphrase, address` (Private key will be added soon!)
- Standart wallet formats
  - Bitcoin - `.bitcoin/wallet.dat`
  - Ethereum - `.ethereum/keystore/`

## Usage
### Install and launch third party apps
Valets use original cryptocurrency's clients, so you won't be able to use this app without installing bitcoind for Bitcoin, geth for Ethereum and so on.

#### Bitcoin
Installation guide - [here](https://askubuntu.com/questions/41001/how-do-i-install-bitcoin-in-ubuntu).

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt update
sudo apt install bitcoind
```

Run bitcoin server:

```
bitcoind -daemon
```

#### Ethereum
Installation guide - [here](https://github.com/ethereum/go-ethereum/wiki/Installing-Geth)

```
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

## To Do
- Zcash support
- Dash support
- Monero support
- Automatically encrypt `_valets_....` folder (private keys, passphrases, etc)
