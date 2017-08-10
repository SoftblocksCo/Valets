# Valets - simple cryptocurrency wallets generator
Written in Python 3. Made with love inside the [Revain](https://revain.org) company.

# What is it?
Данный проект позволяет автоматически создавать тысячи адресов для 12 различных криптовалют. В добавок, все адреса автоматически индексируются клиентами каждой криптовалюты и можно использовать их RPC API для выяснения баланса, списка транзакций и так далее.

![General scheme](https://image.ibb.co/fDBHPv/Payments_2.png)

# ⚠️ Warning ⚠️
**Не рекомендуется использовать Valets в реальных целях, на данный момент проект не протестирован должным образом.**

# Supported currencies
| Name (Coinmarketcap link)                | Status    | Volume (24h)    | Website                            | For developers                           |
| ---------------------------------------- | --------- | --------------- | ---------------------------------- | ---------------------------------------- |
| Bitcoin ([link](https://coinmarketcap.com/currencies/bitcoin/)) | **Ready** | 1.000.000.000 $ | https://bitcoin.org/               | [Bitcoin-cli](https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list) |
| Bitcoin cash ([link](https://coinmarketcap.com/currencies/bitcoin-cash/)) | **Ready** | 360.000.000 $   | https://www.bitcoincash.org/       | [Bitcoin-cli](https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list) |
| Ethereum ([link](https://coinmarketcap.com/currencies/ethereum/)) | **Ready** | 785.000.000 $   | https://www.ethereum.org/          | [Geth](https://github.com/ethereum/go-ethereum/wiki/Managing-your-accounts) |
| Ethereum classic ([link](https://coinmarketcap.com/currencies/ethereum-classic/)) | **Ready** | 87.000.000 $    | https://ethereumclassic.github.io/ | [Geth-classic](https://github.com/ethereumproject/go-ethereum/releases) |
| Litecoin ([link](https://coinmarketcap.com/currencies/litecoin/)) | **Ready** | 119.000.000 $   | https://litecoin.com/              | [Litecoin-cli](https://litecoin.info/Litecoin_API) |
| Dash ([link](https://coinmarketcap.com/currencies/dash/)) | **Ready** | 23.000.000 $    | https://www.dash.org/              | [Dash-cli](https://dashpay.atlassian.net/wiki/display/COMMUNITY/Dash+Command-line+arguments) |
| Zcash ([link](https://coinmarketcap.com/currencies/zcash/)) | **Ready** | 27.000.000 $    | https://z.cash/                    | [Zcash-cli](https://z.cash/download.html) |
| Reddcoin ([link](https://coinmarketcap.com/currencies/reddcoin/)) | **Ready** | 970.000 $       | http://www.reddcoin.com/           | [Reddcoin-cli](https://www.reddcoin.com/#Wallets) |
| Navcoin ([link](https://coinmarketcap.com/currencies/nav-coin/)) | **Ready** | 145.000 $       | https://navcoin.org/               | [Navcoin-cli](https://navcoin.org/downloads/) |
| Vertcoin ([link](https://coinmarketcap.com/currencies/vertcoin/)) | **Ready** | 550.000 $       | https://vertcoin.org/           | [Vertcoind](https://github.com/vertcoin/vertcoin/releases) |
| Dogecoin ([link](https://coinmarketcap.com/currencies/dogecoin/)) | **Ready** | 5.000.000 $     | http://dogecoin.com/               | [Dogecoin-cli](https://github.com/dogecoin/dogecoin/releases) |
| Emercoin ([link](https://coinmarketcap.com/currencies/emercoin/)) | **Ready** | 200.000 $       | http://emercoin.com/               | [Emercoin-cli](https://emercoin.com/EMERCOIND) |

# Install currencies clients

## Bitcoin

- Installation guide - ["Running A Full Node"](https://bitcoin.org/en/full-node)
- Block explorer - [link](https://blockchain.info/)

**Install**

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get update
sudo apt-get install bitcoind
```

**Configure**

```bash
bitcoind # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.bitcoin/bitcoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.bitcoin/bitcoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.bitcoin/bitcoin.conf
echo 'rpcport=8332' >> ~/.bitcoin/bitcoin.conf
echo 'server=1' >> ~/.bitcoin/bitcoin.conf
```

**Run & check RPC**

```bash
bitcoind -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:8332/ | python -mjson.tool
```

**Stop**

```bash
bitcoin-cli stop
```

## Bitcoin cash

- Bitcoin classic used as command line tool, official website is [here](https://bitcoinclassic.com/).
- Block explorer - [link](https://bitinfocharts.com/bitcoin%20cash/explorer/)

**Install**

```bash
wget https://github.com/bitcoinclassic/bitcoinclassic/releases/download/v1.3.3uahf/bitcoin-1.3.3-linux64.tar.gz
tar xfz bitcoin-1.3.3-linux64.tar.gz
mv bitcoin-1.3.3 Bitcoinclassic
rm bitcoin-1.3.3-linux64.tar.gz
cd Bitcoinclassic/bin
rename 's/bitcoin/bitcoinclassic/' *
sudo cp * /usr/bin
```

**Configure**

```bash
mkdir .bitcoinclassic # Run only once, before first launch

echo 'rpcuser=USERNAME' > ~/.bitcoinclassic/bitcoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.bitcoinclassic/bitcoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.bitcoinclassic/bitcoin.conf
echo 'rpcport=8432' >> ~/.bitcoinclassic/bitcoin.conf
echo 'server=1' >> ~/.bitcoinclassic/bitcoin.conf
echo 'bind=0.0.0.0:9222' >> ~/.bitcoinclassic/bitcoin.conf
```

**Run & check**

```bash
bitcoinclassicd -daemon -datadir=.bitcoinclassic/

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:8432/ | python -mjson.tool
```

**Stop**

```bash
bitcoinabc-cli stop
```

## Ethereum

Offical guide, by [ethereum.org](https://ethereum.org) - [link](https://www.ethereum.org/cli#geth)

**Install**

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

**Configure**

```bash
# No need to config anything
```

**Run**

```bash
geth --rpc --rpcaddr "127.0.0.1" --rpcport 8532 --rpcapi "admin,debug,miner,shh,txpool,personal,eth,net,web3" console
```

**Stop**

```bash
# Just type 'exit' in the Geth console
```

## Ethereum classic

**Install**

```bash
wget https://github.com/ethereumproject/go-ethereum/releases/download/v3.5.86/geth-classic-linux-v3.5.0.86-db60074.tar.gz
tar xzf geth-classic-linux-v3.5.0.86-db60074.tar.gz
rm geth-classic-linux-v3.5.0.86-db60074.tar.gz
mv geth geth-classic
sudo cp geth-classic /usr/bin # Make geth-classic systemwide available
```

**Configure**

```bash
# No need to config anything
```

**Run**

```bash
geth-classic --rpc --rpcaddr "127.0.0.1" --rpcapi "admin,debug,miner,shh,txpool,personal,eth,net,web3" --rpcport 8632 --port 30304 console # Running on non-typical ports (30304 and 8632) for the purpose of collision avoidane with geth
```

**Stop**

```bash
# Just type 'exit' in the Geth-classic console
```

## Litecoin

**Install**

```bash
wget https://download.litecoin.org/litecoin-0.14.2/linux/litecoin-0.14.2-x86_64-linux-gnu.tar.gz
tar xzf litecoin-0.14.2-x86_64-linux-gnu.tar.gz
rm litecoin-0.14.2-x86_64-linux-gnu.tar.gz
mv litecoin-0.14.2/ Litecoin
cd Litecoin/bin/
sudo cp * /usr/bin # Make binaries systemwide available
```

**Configure**

```bash
litecoind # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.litecoin/litecoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.litecoin/litecoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.litecoin/litecoin.conf
echo 'rpcport=8732' >> ~/.litecoin/litecoin.conf
echo 'server=1' >> ~/.litecoin/litecoin.conf
```

**Run & check**

```bash
litecoind -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:8732/ | python -mjson.tool
```

**Stop**

```bash
litecoin-cli stop
```

## Dogecoin

**Install**

```bash
wget https://github.com/dogecoin/dogecoin/releases/download/v1.10.0/dogecoin-1.10.0-linux64.tar.gz
tar xzf dogecoin-1.10.0-linux64.tar.gz
rm dogecoin-1.10.0-linux64.tar.gz
mv dogecoin-1.10.0/ Dogecoin
cd Dogecoin/bin/
sudo cp * /usr/bin
```

**Configure**

```bash
dogecoind # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.dogecoin/dogecoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.dogecoin/dogecoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.dogecoin/dogecoin.conf
echo 'rpcport=8832' >> ~/.dogecoin/dogecoin.conf
echo 'server=1' >> ~/.dogecoin/dogecoin.conf
```

**Run & check**

```bash
dogecoind -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:8832/ | python -mjson.tool
```

**Stop**

```bash
dogecoin-cli stop
```

## Dash

**Install**

```bash
wget https://www.dash.org/binaries/dashcore-0.12.1.5-linux64.tar.gz # https://www.dash.org/wallets/#linux
tar xfz dashcore-0.12.1.5-linux64.tar.gz
rm dashcore-0.12.1.5-linux64.tar.gz
mv dashcore-0.12.1/ Dash
cd Dash/bin/
sudo cp * /usr/bin # Make binaries systemwide available
```

**Configure**

```bash
echo 'rpcuser=USERNAME' > ~/.dashcore/dash.conf
echo 'rpcpassword=PASSWORD' >> ~/.dashcore/dash.conf
echo 'rpcbind=127.0.0.1' >> ~/.dashcore/dash.conf
echo 'rpcport=8932' >> ~/.dashcore/dash.conf
echo 'server=1' >> ~/.dashcore/dash.conf
```

**Run & check**

```bash
dashd -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:8932/ | python -mjson.tool
```

**Stop**

```bash
dash-cli stop
```

## Zcash

**Install**

```bash
sudo apt-get install apt-transport-https
wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -
echo "deb [arch=amd64] https://apt.z.cash/ jessie main" | sudo tee /etc/apt/sources.list.d/zcash.list
sudo apt-get update
sudo apt-get install zcash
```

**Configure**

```bash
zcashd # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.zcash/zcash.conf
echo 'rpcpassword=PASSWORD' >> ~/.zcash/zcash.conf
echo 'rpcbind=127.0.0.1' >> ~/.zcash/zcash.conf
echo 'rpcport=9032' >> ~/.zcash/zcash.conf
echo 'server=1' >> ~/.zcash/zcash.conf
```

**Run & check**

```bash
zcash-fetch-params # Run this code before first launch
zcashd -rescan -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:9032/ | python -mjson.tool
```

**Stop**

```bash
zcash-cli stop
```

## Peercoin

**Install**

```bash
# Peercoin releases alavilable only on Sourgeforge, so you should download it manually :(
# Link - https://sourceforge.net/projects/ppcoin/files/
scp ppcoin-0.5.4ppc-linux.tar.gz username@ip:~ # Use scp if necessary, to upload archive
tar xzf ppcoin-0.5.4ppc-linux.tar.gz
mv ppcoin-0.5.4ppc-linux/ Peercoin
rm ppcoin-0.5.4ppc-linux.tar.gz
cd Peercoin/bin/64/
sudo cp * /usr/bin
```

**Configure**

```bash
ppcoind # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.ppcoin/ppcoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.ppcoin/ppcoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.ppcoin/ppcoin.conf
echo 'rpcport=9132' >> ~/.ppcoin/ppcoin.conf
echo 'server=1' >> ~/.ppcoin/ppcoin.conf
```

**Run & check**

```bash
ppcoind -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:9132/ | python -mjson.tool
```

**Stop**

```bash
ppcoind stop
```

## Navcoin

**Install**

```bash
sudo apt-get install curl libcurl3
wget http://www.navcoin.org/files/navcoin-4.0.4/navcoin-4.0.4-x86_64-linux-gnu.tar.gz
tar xzf navcoin-4.0.4-x86_64-linux-gnu.tar.gz
rm navcoin-4.0.4-x86_64-linux-gnu.tar.gz
mv navcoin-4.0.4 Navcoin
cd Navcoin/bin/
sudo cp * /usr/bin
```

**Configure**

```bash
navcoind # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.navcoin4/navcoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.navcoin4/navcoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.navcoin4/navcoin.conf
echo 'rpcport=9532' >> ~/.navcoin4/navcoin.conf
echo 'server=1' >> ~/.navcoin4/navcoin.conf
```

**Run & check**

```bash
navcoind -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:9532/ | python -mjson.tool
```

**Stop**

```bash
namecoind stop
```

## Emercoin

**Install**

```bash
# Emercoin releases alavilable on Sourgeforge, so you should download it manually :(
# Link - https://sourceforge.net/projects/emercoin/?source=typ_redirect
scp emercoin-0.6.2-linux64.tar.gz username@ip:~ # Use scp if necessary, to upload archive
tar xzf emercoin-0.6.2-linux64.tar.gz
mv emercoin-0.6.2/ Emercoin
rm emercoin-0.6.2-linux64.tar.gz
cd Emercoin/bin/
sudo cp * /usr/bin
```

**Configure**

```bash
emercoind # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.emercoin/emercoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.emercoin/emercoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.emercoin/emercoin.conf
echo 'rpcport=9332' >> ~/.emercoin/emercoin.conf
echo 'server=1' >> ~/.emercoin/emercoin.conf
```

**Run & check**

```bash
emercoind -daemon

curl --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://USERNAME:PASSWORD@127.0.0.1:9332/ | python -mjson.tool
```

**Stop**

```bash
emercoin-cli stop
```

## Reddcoin

**Install**

```bash
wget https://github.com/reddcoin-project/reddcoin/releases/download/v2.0.0.0/reddcoin-2.0.0.0-linux.tar.gz
tar xzf reddcoin-2.0.0.0-linux.tar.gz
rm reddcoin-2.0.0.0-linux.tar.gz
mv reddcoin-2.0.0.0-linux Reddcoin
cd Reddcoin/bin/64/
sudo cp * /usr/bin # Make binaries systemwide available
```

**Configure**

```bash
reddcoind # Press CTRL+C right after launch
# All you need right now - is to init datadir

echo 'rpcuser=USERNAME' > ~/.reddcoin/reddcoin.conf
echo 'rpcpassword=PASSWORD' >> ~/.reddcoin/reddcoin.conf
echo 'rpcbind=127.0.0.1' >> ~/.reddcoin/reddcoin.conf
echo 'rpcport=9432' >> ~/.reddcoin/reddcoin.conf
echo 'server=1' >> ~/.reddcoin/reddcoin.conf
```

**Run**

```bash
reddcoind -daemon
```

**Stop**

```bash
reddcoin-cli stop
```

# Install Valets

```bash
sudo apt-get update
sudo apt-get install virtualenv git python-dev python3 python3-pip git

git clone https://github.com/Revain/Valets
cd Valets/
virtualenv --python python3 --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
```

# Run Valets

```bash
$ python Valets/ -c BTC 1000 -c LTC 1000 -c ETH 1000 -c ETC 2000
# Check every 12 currencies
$ python Valets/ -c BTC 1 -c LTC 1 -c DASH 1 -c ZEC 1 -c NAV 1 -c PCC 1 -c BCH 1 -c DOGE 1 -c EMC 1 -c RDD 1 -c ETH 1 -c ETC 1
# Generate 100 wallets per currency
$ python Valets/ -c BTC 100 -c LTC 100 -c DASH 100 -c ZEC 100 -c NAV 100 -c PCC 100 -c BCH 100 -c DOGE 100 -c EMC 100 -c RDD 100 -c ETH 100 -c ETC 100
```
