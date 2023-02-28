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
    "network vnet-gateway show",
)
class Show(AAZCommand):
    """Get the details of a virtual network gateway.

    :example: Get the details of a virtual network gateway.
        az network vnet-gateway show -g MyResourceGroup -n MyVnetGateway
    """

    _aaz_info = {
        "version": "2017-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways/{}", "2017-10-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the VNet gateway.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualNetworkGatewaysGet(ctx=self.ctx)()
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

    class VirtualNetworkGatewaysGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkGatewayName", self.ctx.args.name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2017-10-01",
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
            _schema_on_200.etag = AAZStrType()
            _schema_on_200.id = AAZStrType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.active_active = AAZBoolType(
                serialized_name="activeActive",
            )
            properties.bgp_settings = AAZObjectType(
                serialized_name="bgpSettings",
            )
            properties.enable_bgp = AAZBoolType(
                serialized_name="enableBgp",
            )
            properties.gateway_default_site = AAZObjectType(
                serialized_name="gatewayDefaultSite",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.gateway_default_site)
            properties.gateway_type = AAZStrType(
                serialized_name="gatewayType",
            )
            properties.ip_configurations = AAZListType(
                serialized_name="ipConfigurations",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
            )
            properties.sku = AAZObjectType()
            properties.vpn_client_configuration = AAZObjectType(
                serialized_name="vpnClientConfiguration",
            )
            properties.vpn_type = AAZStrType(
                serialized_name="vpnType",
            )

            bgp_settings = cls._schema_on_200.properties.bgp_settings
            bgp_settings.asn = AAZIntType()
            bgp_settings.bgp_peering_address = AAZStrType(
                serialized_name="bgpPeeringAddress",
            )
            bgp_settings.peer_weight = AAZIntType(
                serialized_name="peerWeight",
            )

            ip_configurations = cls._schema_on_200.properties.ip_configurations
            ip_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.ip_configurations.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.ip_configurations.Element.properties
            properties.private_ip_allocation_method = AAZStrType(
                serialized_name="privateIPAllocationMethod",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address = AAZObjectType(
                serialized_name="publicIPAddress",
            )
            _ShowHelper._build_schema_sub_resource_read(properties.public_ip_address)
            properties.subnet = AAZObjectType()
            _ShowHelper._build_schema_sub_resource_read(properties.subnet)

            sku = cls._schema_on_200.properties.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            vpn_client_configuration = cls._schema_on_200.properties.vpn_client_configuration
            vpn_client_configuration.radius_server_address = AAZStrType(
                serialized_name="radiusServerAddress",
            )
            vpn_client_configuration.radius_server_secret = AAZStrType(
                serialized_name="radiusServerSecret",
            )
            vpn_client_configuration.vpn_client_address_pool = AAZObjectType(
                serialized_name="vpnClientAddressPool",
            )
            vpn_client_configuration.vpn_client_protocols = AAZListType(
                serialized_name="vpnClientProtocols",
            )
            vpn_client_configuration.vpn_client_revoked_certificates = AAZListType(
                serialized_name="vpnClientRevokedCertificates",
            )
            vpn_client_configuration.vpn_client_root_certificates = AAZListType(
                serialized_name="vpnClientRootCertificates",
            )

            vpn_client_address_pool = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_address_pool
            vpn_client_address_pool.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )

            address_prefixes = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_address_pool.address_prefixes
            address_prefixes.Element = AAZStrType()

            vpn_client_protocols = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_protocols
            vpn_client_protocols.Element = AAZStrType()

            vpn_client_revoked_certificates = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_revoked_certificates
            vpn_client_revoked_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.thumbprint = AAZStrType()

            vpn_client_root_certificates = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_root_certificates
            vpn_client_root_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_root_certificates.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.properties.vpn_client_configuration.vpn_client_root_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_cert_data = AAZStrType(
                serialized_name="publicCertData",
                flags={"required": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

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


__all__ = ["Show"]
