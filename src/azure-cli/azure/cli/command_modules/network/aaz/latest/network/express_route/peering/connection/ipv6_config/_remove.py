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
    "network express-route peering connection ipv6-config remove",
)
class Remove(AAZCommand):
    """Remove connection config to ExpressRoute circuit connection.

    :example: Remove connection config to ExpressRoute circuit connection.
        az network express-route peering connection ipv6-config remove -g MyResourceGroup --circuit-name MyCircuit --peering-name AzurePrivatePeering -n myConnection
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutecircuits/{}/peerings/{}/connections/{}", "2022-01-01", "properties.ipv6CircuitConnectionConfig"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, None)

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
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the peering connection.",
            required=True,
        )
        _args_schema.peering_name = AAZStrArg(
            options=["--peering-name"],
            help="Name of BGP peering (i.e. AzurePrivatePeering).",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRouteCircuitConnectionsGet(ctx=self.ctx)()
        self.InstanceDeleteByJson(ctx=self.ctx)()
        yield self.ExpressRouteCircuitConnectionsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            return result.properties.ipv6CircuitConnectionConfig

        def _set(self, value):
            result = self.ctx.vars.instance
            result.properties.ipv6CircuitConnectionConfig = value
            return

    class ExpressRouteCircuitConnectionsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName}",
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
            _RemoveHelper._build_schema_express_route_circuit_connection_read(cls._schema_on_200)

            return cls._schema_on_200

    class ExpressRouteCircuitConnectionsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

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
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _RemoveHelper._build_schema_express_route_circuit_connection_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceDeleteByJson(AAZJsonInstanceDeleteOperation):

        def __call__(self, *args, **kwargs):
            self.ctx.selectors.subresource.set(self._delete_instance())


class _RemoveHelper:
    """Helper class for Remove"""

    _schema_express_route_circuit_connection_read = None

    @classmethod
    def _build_schema_express_route_circuit_connection_read(cls, _schema):
        if cls._schema_express_route_circuit_connection_read is not None:
            _schema.etag = cls._schema_express_route_circuit_connection_read.etag
            _schema.id = cls._schema_express_route_circuit_connection_read.id
            _schema.name = cls._schema_express_route_circuit_connection_read.name
            _schema.properties = cls._schema_express_route_circuit_connection_read.properties
            _schema.type = cls._schema_express_route_circuit_connection_read.type
            return

        cls._schema_express_route_circuit_connection_read = _schema_express_route_circuit_connection_read = AAZObjectType()

        express_route_circuit_connection_read = _schema_express_route_circuit_connection_read
        express_route_circuit_connection_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        express_route_circuit_connection_read.id = AAZStrType()
        express_route_circuit_connection_read.name = AAZStrType()
        express_route_circuit_connection_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        express_route_circuit_connection_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_express_route_circuit_connection_read.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
        )
        properties.authorization_key = AAZStrType(
            serialized_name="authorizationKey",
        )
        properties.circuit_connection_status = AAZStrType(
            serialized_name="circuitConnectionStatus",
            flags={"read_only": True},
        )
        properties.express_route_circuit_peering = AAZObjectType(
            serialized_name="expressRouteCircuitPeering",
        )
        cls._build_schema_sub_resource_read(properties.express_route_circuit_peering)
        properties.ipv6_circuit_connection_config = AAZObjectType(
            serialized_name="ipv6CircuitConnectionConfig",
        )
        properties.peer_express_route_circuit_peering = AAZObjectType(
            serialized_name="peerExpressRouteCircuitPeering",
        )
        cls._build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        ipv6_circuit_connection_config = _schema_express_route_circuit_connection_read.properties.ipv6_circuit_connection_config
        ipv6_circuit_connection_config.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
        )
        ipv6_circuit_connection_config.circuit_connection_status = AAZStrType(
            serialized_name="circuitConnectionStatus",
            flags={"read_only": True},
        )

        _schema.etag = cls._schema_express_route_circuit_connection_read.etag
        _schema.id = cls._schema_express_route_circuit_connection_read.id
        _schema.name = cls._schema_express_route_circuit_connection_read.name
        _schema.properties = cls._schema_express_route_circuit_connection_read.properties
        _schema.type = cls._schema_express_route_circuit_connection_read.type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Remove"]
