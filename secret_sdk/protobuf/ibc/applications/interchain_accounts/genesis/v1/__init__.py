# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/applications/interchain_accounts/genesis/v1/genesis.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from ...controller import v1 as __controller_v1__
from ...host import v1 as __host_v1__


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the interchain accounts genesis state"""

    controller_genesis_state: "ControllerGenesisState" = betterproto.message_field(1)
    host_genesis_state: "HostGenesisState" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ControllerGenesisState(betterproto.Message):
    """
    ControllerGenesisState defines the interchain accounts controller genesis
    state
    """

    active_channels: List["ActiveChannel"] = betterproto.message_field(1)
    interchain_accounts: List["RegisteredInterchainAccount"] = (
        betterproto.message_field(2)
    )
    ports: List[str] = betterproto.string_field(3)
    params: "__controller_v1__.Params" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class HostGenesisState(betterproto.Message):
    """HostGenesisState defines the interchain accounts host genesis state"""

    active_channels: List["ActiveChannel"] = betterproto.message_field(1)
    interchain_accounts: List["RegisteredInterchainAccount"] = (
        betterproto.message_field(2)
    )
    port: str = betterproto.string_field(3)
    params: "__host_v1__.Params" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ActiveChannel(betterproto.Message):
    """
    ActiveChannel contains a connection ID, port ID and associated active
    channel ID, as well as a boolean flag to indicate if the channel is
    middleware enabled
    """

    connection_id: str = betterproto.string_field(1)
    port_id: str = betterproto.string_field(2)
    channel_id: str = betterproto.string_field(3)
    is_middleware_enabled: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class RegisteredInterchainAccount(betterproto.Message):
    """
    RegisteredInterchainAccount contains a connection ID, port ID and
    associated interchain account address
    """

    connection_id: str = betterproto.string_field(1)
    port_id: str = betterproto.string_field(2)
    account_address: str = betterproto.string_field(3)
