"""This module corresponds to functionality documented
at https://blockchain.info/api/blockchain_api

"""

from . import util
import json


def get_block(block_id, api_code=None):
    """Get a single block based on a block index or hash.
    
    :param str block_id: block hash or index to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Block` class
    """
    
    resource = 'rawblock/' + block_id
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Block(json_response)


def get_tx(tx_id, api_code=None):
    """Get a single transaction based on a transaction index or hash.
    
    :param str tx_id: transaction hash or index to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Transaction` class
    """
    
    resource = 'rawtx/' + tx_id
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Transaction(json_response)


def get_block_height(height, api_code=None):
    """Get an array of blocks at the specified height.
    
    :param int height: block height to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an array of :class:`Block` objects
    """
    
    resource = 'block-height/{0}?format=json'.format(height)
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return [Block(b) for b in json_response['blocks']]


def get_address(address, api_code=None):
    """Get data for a single address.
    
    :param str address: address to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Address` class
    """
    
    resource = 'rawaddr/' + address
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Address(json_response)


def get_unspent_outputs(address, api_code=None):
    """Get unspent outputs for a single address.
    
    :param str address: address to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an array of :class:`UnspentOutput` objects
    """
    
    resource = 'unspent?active=' + address
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return [UnspentOutput(o) for o in json_response['unspent_outputs']]


def get_latest_block(api_code=None):
    """Get the latest block on the main chain.
    
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`LatestBlock` class
    """
    
    resource = 'latestblock'
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return LatestBlock(json_response)


def get_unconfirmed_tx(api_code=None):
    """Get a list of currently unconfirmed transactions.
    
    :param str api_code: Blockchain.info API code (optional)
    :return: an array of :class:`Transaction` objects
    """
    
    resource = 'unconfirmed-transactions?format=json'
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return [Transaction(t) for t in json_response['txs']]


def get_blocks(time=None, pool_name=None, api_code=None):
    """Get a list of blocks for a specific day or mining pool.
    Both parameters are optional but at least one is required.
    
    :param int time: time in milliseconds
    :param str pool_name: name of the mining pool
    :param str api_code: Blockchain.info API code (optional)
    :return: an array of :class:`SimpleBlock` objects
    """
    
    resource = 'blocks/{0}?format=json'
    if api_code is not None:
        resource += '&api_code=' + api_code
    if time is not None:
        resource = resource.format(time)
    elif pool_name is not None:
        resource = resource.format(pool_name)
    else:
        resource = resource.format('')
        
    response = util.call_api(resource)
    json_response = json.loads(response)
    return [SimpleBlock(b) for b in json_response['blocks']]


def get_inventory_data(hash, api_code=None):
    """Get inventory data.
    
    :param str hash: tx or block hash
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`InventoryData` class
    """
    resource = 'inv/{0}?format=json'.format(hash)
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return InventoryData(json_response)


class SimpleBlock:
    def __init__(self, b):
        self.height = b['height']
        self.hash = b['hash']
        self.time = b['time']
        self.main_chain = b['main_chain']


class LatestBlock:
    def __init__(self, b):
        self.hash = b['hash']
        self.time = b['time']
        self.block_index = b['block_index']
        self.height = b['height']
        self.tx_indexes = [i for i in b['txIndexes']]


class UnspentOutput:
    def __init__(self, o):
        self.tx_hash = o['tx_hash']
        self.tx_index = o['tx_index']
        self.tx_output_n = o['tx_output_n']
        self.script = o['script']
        self.value = o['value']
        self.value_hex = o['value_hex']
        self.confirmations = o['confirmations']


class Address:
    def __init__(self, a):
        self.hash160 = a['hash160']
        self.address = a['address']
        self.n_tx = a['n_tx']
        self.total_received = a['total_received']
        self.total_sent = a['total_sent']
        self.final_balance = a['final_balance']
        self.transactions = [Transaction(tx) for tx in a['txs']]


class Input:
    def __init__(self, i):
        obj = i.get('prev_out')
        if obj is not None:
            # regular TX
            self.n = obj['n']
            self.value = obj['value']
            self.address = obj['addr']
            self.tx_index = obj['tx_index']
            self.type = obj['type']
            self.script = obj['script']
            self.script_sig = i['script']
            self.sequence = i['sequence']
        else:
            # coinbase TX
            self.script_sig = i['script']
            self.sequence = i['sequence']


class Output:
    def __init__(self, o):
        self.n = o['n']
        self.value = o['value']
        self.address = o.get('addr')
        self.tx_index = o['tx_index']
        self.script = o['script']
        self.spent = o['spent']


class Transaction:
    def __init__(self, t):
        self.double_spend = t.get('double_spend', False)
        self.block_height = t.get('block_height')
        self.time = t['time']
        self.relayed_by = t['relayed_by']
        self.hash = t['hash']
        self.tx_index = t['tx_index']
        self.version = t['ver']
        self.size = t['size']
        self.inputs = [Input(i) for i in t['inputs']]
        self.outputs = [Output(o) for o in t['out']]
        
        if self.block_height is None:
            self.block_height = -1


class Block:
    def __init__(self, b):
        self.hash = b['hash']
        self.version = b['ver']
        self.previous_block = b['prev_block']
        self.merkle_root = b['mrkl_root']
        self.time = b['time']
        self.bits = b['bits']
        self.fee = b['fee']
        self.nonce = b['nonce']
        self.n_tx = b['n_tx']
        self.size = b['size']
        self.block_index = b['block_index']
        self.main_chain = b['main_chain']
        self.height = b['height']
        self.received_time = b.get('received_time', b['time'])
        self.relayed_by = b.get('relayed_by')
        self.transactions = [Transaction(t) for t in b['tx']]
        for tx in self.transactions:
            tx.block_height = self.height


class InventoryData:
    def __init__(self, i):
        self.hash = i['hash']
        self.type = i['type']
        self.initial_time = int(i['initial_time'])
        self.initial_ip = i['initial_ip']
        self.nconnected = int(i['nconnected'])
        self.relayed_count = int(i['relayed_count'])
        self.relayed_percent = int(i['relayed_percent'])
