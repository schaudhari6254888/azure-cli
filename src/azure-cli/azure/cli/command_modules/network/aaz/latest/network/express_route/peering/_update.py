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
    "network express-route peering update",
)
class Update(AAZCommand):
    """Update peering settings of an ExpressRoute circuit.

    :example: Add IPv6 Microsoft Peering settings to existing IPv4 config.
        az network express-route peering update -g MyResourceGroup --circuit-name MyCircuit --ip-version ipv6 --primary-peer-subnet 2002:db00::/126 --secondary-peer-subnet 2003:db00::/126 --advertised-public-prefixes 2002:db00::/126

    :example: Update peering settings of an ExpressRoute circuit. (autogenerated)
        az network express-route peering update --circuit-name MyCircuit --name MyPeering --peer-asn 10002 --primary-peer-subnet 2002:db00::/126 --resource-group MyResourceGroup --secondary-peer-subnet 2003:db00::/126 --shared-key Abc123 --vlan-id 103
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutecircuits/{}/peerings/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

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
            help="The name of the peering.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.peer_asn = AAZIntArg(
            options=["--peer-asn"],
            help="Autonomous system number of the customer/connectivity provider.",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=1,
            ),
        )
        _args_schema.peering_type = AAZStrArg(
            options=["--peering-type"],
            help="BGP peering type for the circuit.  Allowed values: AzurePrivatePeering, AzurePublicPeering, MicrosoftPeering.",
            nullable=True,
            enum={"AzurePrivatePeering": "AzurePrivatePeering", "AzurePublicPeering": "AzurePublicPeering", "MicrosoftPeering": "MicrosoftPeering"},
        )
        _args_schema.primary_peer_subnet = AAZStrArg(
            options=["--primary-peer-subnet"],
            help="/30(ipv4) or /126(ipv6) subnet used to configure IP addresses for primary interface.",
            nullable=True,
        )
        _args_schema.secondary_peer_subnet = AAZStrArg(
            options=["--secondary-peer-subnet"],
            help="/30(ipv4) or /126(ipv6) subnet used to configure IP addresses for secondary interface.",
            nullable=True,
        )
        _args_schema.shared_key = AAZStrArg(
            options=["--shared-key"],
            help="Key for generating an MD5 for the BGP session.",
            nullable=True,
        )
        _args_schema.vlan_id = AAZIntArg(
            options=["--vlan-id"],
            help="Identifier used to identify the customer.",
            nullable=True,
        )

        # define Arg Group "Microsoft Peering"

        _args_schema = cls._args_schema
        _args_schema.advertised_public_prefixes = AAZListArg(
            options=["--advertised-public-prefixes"],
            arg_group="Microsoft Peering",
            help="Space-separated list of prefixes to be advertised through the BGP peering.",
            nullable=True,
        )
        _args_schema.customer_asn = AAZIntArg(
            options=["--customer-asn"],
            arg_group="Microsoft Peering",
            help="Autonomous system number of the customer.",
            nullable=True,
        )
        _args_schema.legacy_mode = AAZIntArg(
            options=["--legacy-mode"],
            arg_group="Microsoft Peering",
            help="Integer representing the legacy mode of the peering.",
            nullable=True,
        )
        _args_schema.routing_registry_name = AAZStrArg(
            options=["--routing-registry-name"],
            arg_group="Microsoft Peering",
            help="Internet Routing Registry / Regional Internet Registry. Allowed values: AFRINIC, ALTDB, APNIC, ARIN, LACNIC, LEVEL3, RADB, RIPENCC.",
            nullable=True,
        )
        _args_schema.route_filter = AAZStrArg(
            options=["--route-filter"],
            arg_group="Microsoft Peering",
            help="Name or ID of a route filter to apply to the peering settings.",
            nullable=True,
        )

        advertised_public_prefixes = cls._args_schema.advertised_public_prefixes
        advertised_public_prefixes.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "MicrosoftPeeringConfig"

        # define Arg Group "PeeringParameters"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.ipv6_peering_config = AAZObjectArg(
            options=["--ipv6-peering-config"],
            arg_group="Properties",
            help="The IPv6 peering configuration.",
            nullable=True,
        )

        ipv6_peering_config = cls._args_schema.ipv6_peering_config
        ipv6_peering_config.microsoft_peering_config = AAZObjectArg(
            options=["microsoft-peering-config"],
            help="The Microsoft peering configuration.",
            nullable=True,
        )
        cls._build_args_express_route_circuit_peering_config_update(ipv6_peering_config.microsoft_peering_config)
        ipv6_peering_config.primary_peer_address_prefix = AAZStrArg(
            options=["primary-peer-address-prefix"],
            help="The primary address prefix.",
            nullable=True,
        )
        ipv6_peering_config.route_filter = AAZStrArg(
            options=["route-filter"],
            help="The reference to the RouteFilter resource.",
            nullable=True,
        )
        ipv6_peering_config.secondary_peer_address_prefix = AAZStrArg(
            options=["secondary-peer-address-prefix"],
            help="The secondary address prefix.",
            nullable=True,
        )
        ipv6_peering_config.state = AAZStrArg(
            options=["state"],
            help="The state of peering.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        return cls._args_schema

    _args_express_route_circuit_peering_config_update = None

    @classmethod
    def _build_args_express_route_circuit_peering_config_update(cls, _schema):
        if cls._args_express_route_circuit_peering_config_update is not None:
            _schema.advertised_communities = cls._args_express_route_circuit_peering_config_update.advertised_communities
            _schema.advertised_public_prefixes = cls._args_express_route_circuit_peering_config_update.advertised_public_prefixes
            _schema.customer_asn = cls._args_express_route_circuit_peering_config_update.customer_asn
            _schema.legacy_mode = cls._args_express_route_circuit_peering_config_update.legacy_mode
            _schema.routing_registry_name = cls._args_express_route_circuit_peering_config_update.routing_registry_name
            return

        cls._args_express_route_circuit_peering_config_update = AAZObjectArg(
            nullable=True,
        )

        express_route_circuit_peering_config_update = cls._args_express_route_circuit_peering_config_update
        express_route_circuit_peering_config_update.advertised_communities = AAZListArg(
            options=["advertised-communities"],
            help="The communities of bgp peering. Specified for microsoft peering.",
            nullable=True,
        )
        express_route_circuit_peering_config_update.advertised_public_prefixes = AAZListArg(
            options=["advertised-public-prefixes"],
            help="The reference to AdvertisedPublicPrefixes.",
            nullable=True,
        )
        express_route_circuit_peering_config_update.customer_asn = AAZIntArg(
            options=["customer-asn"],
            help="The CustomerASN of the peering.",
            nullable=True,
        )
        express_route_circuit_peering_config_update.legacy_mode = AAZIntArg(
            options=["legacy-mode"],
            help="The legacy mode of the peering.",
            nullable=True,
        )
        express_route_circuit_peering_config_update.routing_registry_name = AAZStrArg(
            options=["routing-registry-name"],
            help="The RoutingRegistryName of the configuration.",
            nullable=True,
        )

        advertised_communities = cls._args_express_route_circuit_peering_config_update.advertised_communities
        advertised_communities.Element = AAZStrArg(
            nullable=True,
        )

        advertised_public_prefixes = cls._args_express_route_circuit_peering_config_update.advertised_public_prefixes
        advertised_public_prefixes.Element = AAZStrArg(
            nullable=True,
        )

        _schema.advertised_communities = cls._args_express_route_circuit_peering_config_update.advertised_communities
        _schema.advertised_public_prefixes = cls._args_express_route_circuit_peering_config_update.advertised_public_prefixes
        _schema.customer_asn = cls._args_express_route_circuit_peering_config_update.customer_asn
        _schema.legacy_mode = cls._args_express_route_circuit_peering_config_update.legacy_mode
        _schema.routing_registry_name = cls._args_express_route_circuit_peering_config_update.routing_registry_name

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRouteCircuitPeeringsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.ExpressRouteCircuitPeeringsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExpressRouteCircuitPeeringsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}",
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
                    "peeringName", self.ctx.args.name,
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
            _UpdateHelper._build_schema_express_route_circuit_peering_read(cls._schema_on_200)

            return cls._schema_on_200

    class ExpressRouteCircuitPeeringsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}",
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
                    "peeringName", self.ctx.args.name,
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
            _UpdateHelper._build_schema_express_route_circuit_peering_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("ipv6PeeringConfig", AAZObjectType, ".ipv6_peering_config")
                properties.set_prop("microsoftPeeringConfig", AAZObjectType)
                properties.set_prop("peerASN", AAZIntType, ".peer_asn")
                properties.set_prop("peeringType", AAZStrType, ".peering_type")
                properties.set_prop("primaryPeerAddressPrefix", AAZStrType, ".primary_peer_subnet")
                properties.set_prop("routeFilter", AAZObjectType)
                properties.set_prop("secondaryPeerAddressPrefix", AAZStrType, ".secondary_peer_subnet")
                properties.set_prop("sharedKey", AAZStrType, ".shared_key")
                properties.set_prop("vlanId", AAZIntType, ".vlan_id")

            ipv6_peering_config = _builder.get(".properties.ipv6PeeringConfig")
            if ipv6_peering_config is not None:
                _UpdateHelper._build_schema_express_route_circuit_peering_config_update(ipv6_peering_config.set_prop("microsoftPeeringConfig", AAZObjectType, ".microsoft_peering_config"))
                ipv6_peering_config.set_prop("primaryPeerAddressPrefix", AAZStrType, ".primary_peer_address_prefix")
                ipv6_peering_config.set_prop("routeFilter", AAZObjectType)
                ipv6_peering_config.set_prop("secondaryPeerAddressPrefix", AAZStrType, ".secondary_peer_address_prefix")
                ipv6_peering_config.set_prop("state", AAZStrType, ".state")

            route_filter = _builder.get(".properties.ipv6PeeringConfig.routeFilter")
            if route_filter is not None:
                route_filter.set_prop("id", AAZStrType, ".route_filter")

            microsoft_peering_config = _builder.get(".properties.microsoftPeeringConfig")
            if microsoft_peering_config is not None:
                microsoft_peering_config.set_prop("advertisedPublicPrefixes", AAZListType, ".advertised_public_prefixes")
                microsoft_peering_config.set_prop("customerASN", AAZIntType, ".customer_asn")
                microsoft_peering_config.set_prop("legacyMode", AAZIntType, ".legacy_mode")
                microsoft_peering_config.set_prop("routingRegistryName", AAZStrType, ".routing_registry_name")

            advertised_public_prefixes = _builder.get(".properties.microsoftPeeringConfig.advertisedPublicPrefixes")
            if advertised_public_prefixes is not None:
                advertised_public_prefixes.set_elements(AAZStrType, ".")

            route_filter = _builder.get(".properties.routeFilter")
            if route_filter is not None:
                route_filter.set_prop("id", AAZStrType, ".route_filter")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_express_route_circuit_peering_config_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("advertisedCommunities", AAZListType, ".advertised_communities")
        _builder.set_prop("advertisedPublicPrefixes", AAZListType, ".advertised_public_prefixes")
        _builder.set_prop("customerASN", AAZIntType, ".customer_asn")
        _builder.set_prop("legacyMode", AAZIntType, ".legacy_mode")
        _builder.set_prop("routingRegistryName", AAZStrType, ".routing_registry_name")

        advertised_communities = _builder.get(".advertisedCommunities")
        if advertised_communities is not None:
            advertised_communities.set_elements(AAZStrType, ".")

        advertised_public_prefixes = _builder.get(".advertisedPublicPrefixes")
        if advertised_public_prefixes is not None:
            advertised_public_prefixes.set_elements(AAZStrType, ".")

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_express_route_circuit_peering_config_read = None

    @classmethod
    def _build_schema_express_route_circuit_peering_config_read(cls, _schema):
        if cls._schema_express_route_circuit_peering_config_read is not None:
            _schema.advertised_communities = cls._schema_express_route_circuit_peering_config_read.advertised_communities
            _schema.advertised_public_prefixes = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes
            _schema.advertised_public_prefixes_state = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
            _schema.customer_asn = cls._schema_express_route_circuit_peering_config_read.customer_asn
            _schema.legacy_mode = cls._schema_express_route_circuit_peering_config_read.legacy_mode
            _schema.routing_registry_name = cls._schema_express_route_circuit_peering_config_read.routing_registry_name
            return

        cls._schema_express_route_circuit_peering_config_read = _schema_express_route_circuit_peering_config_read = AAZObjectType()

        express_route_circuit_peering_config_read = _schema_express_route_circuit_peering_config_read
        express_route_circuit_peering_config_read.advertised_communities = AAZListType(
            serialized_name="advertisedCommunities",
        )
        express_route_circuit_peering_config_read.advertised_public_prefixes = AAZListType(
            serialized_name="advertisedPublicPrefixes",
        )
        express_route_circuit_peering_config_read.advertised_public_prefixes_state = AAZStrType(
            serialized_name="advertisedPublicPrefixesState",
            flags={"read_only": True},
        )
        express_route_circuit_peering_config_read.customer_asn = AAZIntType(
            serialized_name="customerASN",
        )
        express_route_circuit_peering_config_read.legacy_mode = AAZIntType(
            serialized_name="legacyMode",
        )
        express_route_circuit_peering_config_read.routing_registry_name = AAZStrType(
            serialized_name="routingRegistryName",
        )

        advertised_communities = _schema_express_route_circuit_peering_config_read.advertised_communities
        advertised_communities.Element = AAZStrType()

        advertised_public_prefixes = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes
        advertised_public_prefixes.Element = AAZStrType()

        _schema.advertised_communities = cls._schema_express_route_circuit_peering_config_read.advertised_communities
        _schema.advertised_public_prefixes = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes
        _schema.advertised_public_prefixes_state = cls._schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
        _schema.customer_asn = cls._schema_express_route_circuit_peering_config_read.customer_asn
        _schema.legacy_mode = cls._schema_express_route_circuit_peering_config_read.legacy_mode
        _schema.routing_registry_name = cls._schema_express_route_circuit_peering_config_read.routing_registry_name

    _schema_express_route_circuit_peering_read = None

    @classmethod
    def _build_schema_express_route_circuit_peering_read(cls, _schema):
        if cls._schema_express_route_circuit_peering_read is not None:
            _schema.etag = cls._schema_express_route_circuit_peering_read.etag
            _schema.id = cls._schema_express_route_circuit_peering_read.id
            _schema.name = cls._schema_express_route_circuit_peering_read.name
            _schema.properties = cls._schema_express_route_circuit_peering_read.properties
            _schema.type = cls._schema_express_route_circuit_peering_read.type
            return

        cls._schema_express_route_circuit_peering_read = _schema_express_route_circuit_peering_read = AAZObjectType()

        express_route_circuit_peering_read = _schema_express_route_circuit_peering_read
        express_route_circuit_peering_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        express_route_circuit_peering_read.id = AAZStrType()
        express_route_circuit_peering_read.name = AAZStrType()
        express_route_circuit_peering_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        express_route_circuit_peering_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_express_route_circuit_peering_read.properties
        properties.azure_asn = AAZIntType(
            serialized_name="azureASN",
        )
        properties.connections = AAZListType()
        properties.express_route_connection = AAZObjectType(
            serialized_name="expressRouteConnection",
        )
        properties.gateway_manager_etag = AAZStrType(
            serialized_name="gatewayManagerEtag",
        )
        properties.ipv6_peering_config = AAZObjectType(
            serialized_name="ipv6PeeringConfig",
        )
        properties.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
            flags={"read_only": True},
        )
        properties.microsoft_peering_config = AAZObjectType(
            serialized_name="microsoftPeeringConfig",
        )
        cls._build_schema_express_route_circuit_peering_config_read(properties.microsoft_peering_config)
        properties.peer_asn = AAZIntType(
            serialized_name="peerASN",
        )
        properties.peered_connections = AAZListType(
            serialized_name="peeredConnections",
            flags={"read_only": True},
        )
        properties.peering_type = AAZStrType(
            serialized_name="peeringType",
        )
        properties.primary_azure_port = AAZStrType(
            serialized_name="primaryAzurePort",
        )
        properties.primary_peer_address_prefix = AAZStrType(
            serialized_name="primaryPeerAddressPrefix",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.route_filter = AAZObjectType(
            serialized_name="routeFilter",
        )
        cls._build_schema_sub_resource_read(properties.route_filter)
        properties.secondary_azure_port = AAZStrType(
            serialized_name="secondaryAzurePort",
        )
        properties.secondary_peer_address_prefix = AAZStrType(
            serialized_name="secondaryPeerAddressPrefix",
        )
        properties.shared_key = AAZStrType(
            serialized_name="sharedKey",
        )
        properties.state = AAZStrType()
        properties.stats = AAZObjectType()
        properties.vlan_id = AAZIntType(
            serialized_name="vlanId",
        )

        connections = _schema_express_route_circuit_peering_read.properties.connections
        connections.Element = AAZObjectType()

        _element = _schema_express_route_circuit_peering_read.properties.connections.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_express_route_circuit_peering_read.properties.connections.Element.properties
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

        ipv6_circuit_connection_config = _schema_express_route_circuit_peering_read.properties.connections.Element.properties.ipv6_circuit_connection_config
        ipv6_circuit_connection_config.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
        )
        ipv6_circuit_connection_config.circuit_connection_status = AAZStrType(
            serialized_name="circuitConnectionStatus",
            flags={"read_only": True},
        )

        express_route_connection = _schema_express_route_circuit_peering_read.properties.express_route_connection
        express_route_connection.id = AAZStrType(
            flags={"read_only": True},
        )

        ipv6_peering_config = _schema_express_route_circuit_peering_read.properties.ipv6_peering_config
        ipv6_peering_config.microsoft_peering_config = AAZObjectType(
            serialized_name="microsoftPeeringConfig",
        )
        cls._build_schema_express_route_circuit_peering_config_read(ipv6_peering_config.microsoft_peering_config)
        ipv6_peering_config.primary_peer_address_prefix = AAZStrType(
            serialized_name="primaryPeerAddressPrefix",
        )
        ipv6_peering_config.route_filter = AAZObjectType(
            serialized_name="routeFilter",
        )
        cls._build_schema_sub_resource_read(ipv6_peering_config.route_filter)
        ipv6_peering_config.secondary_peer_address_prefix = AAZStrType(
            serialized_name="secondaryPeerAddressPrefix",
        )
        ipv6_peering_config.state = AAZStrType()

        peered_connections = _schema_express_route_circuit_peering_read.properties.peered_connections
        peered_connections.Element = AAZObjectType()

        _element = _schema_express_route_circuit_peering_read.properties.peered_connections.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_express_route_circuit_peering_read.properties.peered_connections.Element.properties
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
        cls._build_schema_sub_resource_read(properties.express_route_circuit_peering)
        properties.peer_express_route_circuit_peering = AAZObjectType(
            serialized_name="peerExpressRouteCircuitPeering",
        )
        cls._build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        stats = _schema_express_route_circuit_peering_read.properties.stats
        stats.primarybytes_in = AAZIntType(
            serialized_name="primarybytesIn",
        )
        stats.primarybytes_out = AAZIntType(
            serialized_name="primarybytesOut",
        )
        stats.secondarybytes_in = AAZIntType(
            serialized_name="secondarybytesIn",
        )
        stats.secondarybytes_out = AAZIntType(
            serialized_name="secondarybytesOut",
        )

        _schema.etag = cls._schema_express_route_circuit_peering_read.etag
        _schema.id = cls._schema_express_route_circuit_peering_read.id
        _schema.name = cls._schema_express_route_circuit_peering_read.name
        _schema.properties = cls._schema_express_route_circuit_peering_read.properties
        _schema.type = cls._schema_express_route_circuit_peering_read.type

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


__all__ = ["Update"]
