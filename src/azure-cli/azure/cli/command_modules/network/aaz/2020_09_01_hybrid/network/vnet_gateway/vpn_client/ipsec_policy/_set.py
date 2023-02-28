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
    "network vnet-gateway vpn-client ipsec-policy set",
    is_preview=True,
)
class Set(AAZCommand):
    """Set the VPN client connection ipsec policy per P2S client connection of the virtual network gateway.

    :example: Set the VPN client connection ipsec policy per P2S client connection of the virtual network gateway.
        az network vnet-gateway vpn-client ipsec-policy set -g MyResourceGroup -n MyVnetGateway --dh-group DHGroup14 --ike-encryption AES256 --ike-integrity SHA384 --ipsec-encryption DES3 --ipsec-integrity GCMAES256 --pfs-group PFS2048 --sa-lifetime 27000 --sa-max-size 102400000
    """

    _aaz_info = {
        "version": "2018-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways/{}/setvpnclientipsecparameters", "2018-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the VNet gateway.",
            required=True,
            id_part="name",
        )

        # define Arg Group "IKE Phase 1"

        _args_schema = cls._args_schema
        _args_schema.dh_group = AAZStrArg(
            options=["--dh-group"],
            arg_group="IKE Phase 1",
            help="The DH Groups used for initial SA.",
            required=True,
            enum={"DHGroup1": "DHGroup1", "DHGroup14": "DHGroup14", "DHGroup2": "DHGroup2", "DHGroup2048": "DHGroup2048", "DHGroup24": "DHGroup24", "ECP256": "ECP256", "ECP384": "ECP384", "None": "None"},
        )
        _args_schema.ipsec_encryption = AAZStrArg(
            options=["--ipsec-encryption"],
            arg_group="IKE Phase 1",
            help="The IPSec encryption algorithm.",
            required=True,
            enum={"AES128": "AES128", "AES192": "AES192", "AES256": "AES256", "DES": "DES", "DES3": "DES3", "GCMAES128": "GCMAES128", "GCMAES192": "GCMAES192", "GCMAES256": "GCMAES256", "None": "None"},
        )
        _args_schema.ipsec_integrity = AAZStrArg(
            options=["--ipsec-integrity"],
            arg_group="IKE Phase 1",
            help="The IPSec integrity algorithm.",
            required=True,
            enum={"GCMAES128": "GCMAES128", "GCMAES192": "GCMAES192", "GCMAES256": "GCMAES256", "MD5": "MD5", "SHA1": "SHA1", "SHA256": "SHA256"},
        )

        # define Arg Group "IKE Phase 2"

        _args_schema = cls._args_schema
        _args_schema.ike_encryption = AAZStrArg(
            options=["--ike-encryption"],
            arg_group="IKE Phase 2",
            help="The IKE encryption algorithm.",
            required=True,
            enum={"AES128": "AES128", "AES192": "AES192", "AES256": "AES256", "DES": "DES", "DES3": "DES3", "GCMAES128": "GCMAES128", "GCMAES256": "GCMAES256"},
        )
        _args_schema.ike_integrity = AAZStrArg(
            options=["--ike-integrity"],
            arg_group="IKE Phase 2",
            help="The IKE integrity algorithm.",
            required=True,
            enum={"GCMAES128": "GCMAES128", "GCMAES256": "GCMAES256", "MD5": "MD5", "SHA1": "SHA1", "SHA256": "SHA256", "SHA384": "SHA384"},
        )
        _args_schema.pfs_group = AAZStrArg(
            options=["--pfs-group"],
            arg_group="IKE Phase 2",
            help="The Pfs Groups used for new child SA.",
            required=True,
            enum={"ECP256": "ECP256", "ECP384": "ECP384", "None": "None", "PFS1": "PFS1", "PFS14": "PFS14", "PFS2": "PFS2", "PFS2048": "PFS2048", "PFS24": "PFS24", "PFSMM": "PFSMM"},
        )

        # define Arg Group "Security Association"

        _args_schema = cls._args_schema
        _args_schema.sa_max_size = AAZIntArg(
            options=["--sa-max-size"],
            arg_group="Security Association",
            help="The payload size in KB for P2S client.",
            required=True,
        )
        _args_schema.sa_lifetime = AAZIntArg(
            options=["--sa-lifetime"],
            arg_group="Security Association",
            help="The lifetime in seconds for P2S client.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VirtualNetworkGatewaysSetVpnclientIpsecParameters(ctx=self.ctx)()
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

    class VirtualNetworkGatewaysSetVpnclientIpsecParameters(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/setvpnclientipsecparameters",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

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
                    "api-version", "2018-11-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("dhGroup", AAZStrType, ".dh_group", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("ikeEncryption", AAZStrType, ".ike_encryption", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("ikeIntegrity", AAZStrType, ".ike_integrity", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("ipsecEncryption", AAZStrType, ".ipsec_encryption", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("ipsecIntegrity", AAZStrType, ".ipsec_integrity", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("pfsGroup", AAZStrType, ".pfs_group", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("saDataSizeKilobytes", AAZIntType, ".sa_max_size", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("saLifeTimeSeconds", AAZIntType, ".sa_lifetime", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

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
            _schema_on_200.dh_group = AAZStrType(
                serialized_name="dhGroup",
                flags={"required": True},
            )
            _schema_on_200.ike_encryption = AAZStrType(
                serialized_name="ikeEncryption",
                flags={"required": True},
            )
            _schema_on_200.ike_integrity = AAZStrType(
                serialized_name="ikeIntegrity",
                flags={"required": True},
            )
            _schema_on_200.ipsec_encryption = AAZStrType(
                serialized_name="ipsecEncryption",
                flags={"required": True},
            )
            _schema_on_200.ipsec_integrity = AAZStrType(
                serialized_name="ipsecIntegrity",
                flags={"required": True},
            )
            _schema_on_200.pfs_group = AAZStrType(
                serialized_name="pfsGroup",
                flags={"required": True},
            )
            _schema_on_200.sa_data_size_kilobytes = AAZIntType(
                serialized_name="saDataSizeKilobytes",
                flags={"required": True},
            )
            _schema_on_200.sa_life_time_seconds = AAZIntType(
                serialized_name="saLifeTimeSeconds",
                flags={"required": True},
            )

            return cls._schema_on_200


class _SetHelper:
    """Helper class for Set"""


__all__ = ["Set"]
