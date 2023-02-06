# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route peering peer-connection show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get the specified Peer Express Route Circuit Connection from the specified express route circuit.

    :example: Show ExpressRouteCircuit Connection
        az network express-route peering peer-connection show --circuit-name MyCircuit --name MyPeeringConnection --peering-name MyPeering --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutecircuits/{}/peerings/{}/peerconnections/{}", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.circuit_name = AAZStrArg(
            options=["--circuit-name"],
            help="ExpressRoute circuit name.",
            required=True,
            id_part="name",
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the peering connection.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.peering_name = AAZStrArg(
            options=["--peering-name"],
            help="Name of BGP peering (i.e. AzurePrivatePeering).",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PeerExpressRouteCircuitConnectionsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PeerExpressRouteCircuitConnectionsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/peerConnections/{connectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "circuitName", self.ctx.args.circuit_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "connectionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "peeringName", self.ctx.args.peering_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.auth_resource_guid = AAZStrType(
                serialized_name="authResourceGuid",
            )
            properties.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )
            properties.connection_name = AAZStrType(
                serialized_name="connectionName",
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.express_route_circuit_peering)
            properties.peer_express_route_circuit_peering = AAZObjectType(
                serialized_name="peerExpressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            return cls._schema_on_200


_schema_sub_resource_read = None


def _build_schema_sub_resource_read(_schema):
    global _schema_sub_resource_read
    if _schema_sub_resource_read is not None:
        _schema.id = _schema_sub_resource_read.id
        return

    _schema_sub_resource_read = AAZObjectType()

    sub_resource_read = _schema_sub_resource_read
    sub_resource_read.id = AAZStrType()

    _schema.id = _schema_sub_resource_read.id


__all__ = ["Show"]
