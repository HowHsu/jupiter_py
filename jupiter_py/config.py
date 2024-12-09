from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore
import os

PRIV_KEY = os.getenv('SOL_PRIV_KEY', '')
RPC = os.getenv('SOL_RPC', '')

client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)
