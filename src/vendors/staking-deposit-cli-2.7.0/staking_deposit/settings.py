from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.7.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


MAINNET = 'mainnet'
GOERLI = 'goerli'
PRATER = 'prater'
SEPOLIA = 'sepolia'
ZHEJIANG = 'zhejiang'
HOLESKY = 'holesky'

# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('10000001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('6e1583608783377f139b7bac661aff7d5cca656af16ac34f9d0eda27dbf1316c'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('10000001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('6e1583608783377f139b7bac661aff7d5cca656af16ac34f9d0eda27dbf1316c'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('10000001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('6e1583608783377f139b7bac661aff7d5cca656af16ac34f9d0eda27dbf1316c'))
# Zhejiang setting
ZhejiangSetting = BaseChainSetting(
    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('10000001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('6e1583608783377f139b7bac661aff7d5cca656af16ac34f9d0eda27dbf1316c'))
# Holesky setting
HoleskySetting = BaseChainSetting(
    NETWORK_NAME=HOLESKY, GENESIS_FORK_VERSION=bytes.fromhex('10000001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('6e1583608783377f139b7bac661aff7d5cca656af16ac34f9d0eda27dbf1316c'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    SEPOLIA: SepoliaSetting,
    ZHEJIANG: ZhejiangSetting,
    HOLESKY: HoleskySetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
