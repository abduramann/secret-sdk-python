# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/autocli/v1/options.proto, cosmos/autocli/v1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class ModuleOptions(betterproto.Message):
    """ModuleOptions describes the CLI options for a Cosmos SDK module."""

    tx: "ServiceCommandDescriptor" = betterproto.message_field(1)
    """tx describes the tx commands for the module."""

    query: "ServiceCommandDescriptor" = betterproto.message_field(2)
    """query describes the queries commands for the module."""


@dataclass(eq=False, repr=False)
class ServiceCommandDescriptor(betterproto.Message):
    """
    ServiceCommandDescriptor describes a CLI command based on a protobuf
    service.
    """

    service: str = betterproto.string_field(1)
    """
    service is the fully qualified name of the protobuf service to build the
    command from. It can be left empty if sub_commands are used instead which
    may be the case if a module provides multiple tx and/or query services.
    """

    rpc_command_options: List["RpcCommandOptions"] = betterproto.message_field(2)
    """
    rpc_command_options are options for commands generated from rpc methods. If
    no options are specified for a given rpc method on the service, a command
    will be generated for that method with the default options.
    """

    sub_commands: Dict[str, "ServiceCommandDescriptor"] = betterproto.map_field(
        3, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """
    sub_commands is a map of optional sub-commands for this command based on
    different protobuf services. The map key is used as the name of the sub-
    command.
    """


@dataclass(eq=False, repr=False)
class RpcCommandOptions(betterproto.Message):
    """
    RpcCommandOptions specifies options for commands generated from protobuf
    rpc methods.
    """

    rpc_method: str = betterproto.string_field(1)
    """
    rpc_method is short name of the protobuf rpc method that this command is
    generated from.
    """

    use: str = betterproto.string_field(2)
    """
    use is the one-line usage method. It also allows specifying an alternate
    name for the command as the first word of the usage text. By default the
    name of an rpc command is the kebab-case short name of the rpc method.
    """

    long: str = betterproto.string_field(3)
    """long is the long message shown in the 'help <this-command>' output."""

    short: str = betterproto.string_field(4)
    """short is the short description shown in the 'help' output."""

    example: str = betterproto.string_field(5)
    """example is examples of how to use the command."""

    alias: List[str] = betterproto.string_field(6)
    """
    alias is an array of aliases that can be used instead of the first word in
    Use.
    """

    suggest_for: List[str] = betterproto.string_field(7)
    """
    suggest_for is an array of command names for which this command will be
    suggested - similar to aliases but only suggests.
    """

    deprecated: str = betterproto.string_field(8)
    """
    deprecated defines, if this command is deprecated and should print this
    string when used.
    """

    version: str = betterproto.string_field(9)
    """
    version defines the version for this command. If this value is non-empty
    and the command does not define a "version" flag, a "version" boolean flag
    will be added to the command and, if specified, will print content of the
    "Version" variable. A shorthand "v" flag will also be added if the command
    does not define one.
    """

    flag_options: Dict[str, "FlagOptions"] = betterproto.map_field(
        10, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """
    flag_options are options for flags generated from rpc request fields. By
    default all request fields are configured as flags. They can also be
    configured as positional args instead using positional_args.
    """

    positional_args: List["PositionalArgDescriptor"] = betterproto.message_field(11)
    """positional_args specifies positional arguments for the command."""

    skip: bool = betterproto.bool_field(12)
    """
    skip specifies whether to skip this rpc method when generating commands.
    """


@dataclass(eq=False, repr=False)
class FlagOptions(betterproto.Message):
    """
    FlagOptions are options for flags generated from rpc request fields. By
    default, all request fields are configured as flags based on the kebab-case
    name of the field. Fields can be turned into positional arguments instead
    by using RpcCommandOptions.positional_args.
    """

    name: str = betterproto.string_field(1)
    """name is an alternate name to use for the field flag."""

    shorthand: str = betterproto.string_field(2)
    """shorthand is a one-letter abbreviated flag."""

    usage: str = betterproto.string_field(3)
    """usage is the help message."""

    default_value: str = betterproto.string_field(4)
    """default_value is the default value as text."""

    deprecated: str = betterproto.string_field(6)
    """deprecated is the usage text to show if this flag is deprecated."""

    shorthand_deprecated: str = betterproto.string_field(7)
    """
    shorthand_deprecated is the usage text to show if the shorthand of this
    flag is deprecated.
    """

    hidden: bool = betterproto.bool_field(8)
    """hidden hides the flag from help/usage text"""


@dataclass(eq=False, repr=False)
class PositionalArgDescriptor(betterproto.Message):
    """PositionalArgDescriptor describes a positional argument."""

    proto_field: str = betterproto.string_field(1)
    """
    proto_field specifies the proto field to use as the positional arg. Any
    fields used as positional args will not have a flag generated.
    """

    varargs: bool = betterproto.bool_field(2)
    """
    varargs makes a positional parameter a varargs parameter. This can only be
    applied to last positional parameter and the proto_field must a repeated
    field.
    """


@dataclass(eq=False, repr=False)
class AppOptionsRequest(betterproto.Message):
    """AppOptionsRequest is the RemoteInfoService/AppOptions request type."""

    pass


@dataclass(eq=False, repr=False)
class AppOptionsResponse(betterproto.Message):
    """
    AppOptionsResponse is the RemoteInfoService/AppOptions response type.
    """

    module_options: Dict[str, "ModuleOptions"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """module_options is a map of module name to autocli module options."""


class QueryStub(betterproto.ServiceStub):
    async def app_options(
        self,
        app_options_request: "AppOptionsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "AppOptionsResponse":
        return await self._unary_unary(
            "/cosmos.autocli.v1.Query/AppOptions",
            app_options_request,
            AppOptionsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):

    async def app_options(
        self, app_options_request: "AppOptionsRequest"
    ) -> "AppOptionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_app_options(
        self, stream: "grpclib.server.Stream[AppOptionsRequest, AppOptionsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.app_options(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.autocli.v1.Query/AppOptions": grpclib.const.Handler(
                self.__rpc_app_options,
                grpclib.const.Cardinality.UNARY_UNARY,
                AppOptionsRequest,
                AppOptionsResponse,
            ),
        }
