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
    "eventhubs namespace network-rule-set virtual-network-rule list",
)
class List(AAZCommand):
    """eventhubs namespace network-rule-set virtual-network-rule list
    """

    _aaz_info = {
        "version": "2022-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventhub/namespaces/{}/networkrulesets/default", "2022-01-01-preview", "properties.virtualNetworkRules"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
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
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The Namespace name",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NamespacesGetNetworkRuleSet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            return result.properties.virtualNetworkRules

        def _set(self, value):
            result = self.ctx.vars.instance
            result.properties.virtualNetworkRules = value
            return

    class NamespacesGetNetworkRuleSet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/networkRuleSets/default",
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
                    "namespaceName", self.ctx.args.namespace_name,
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
                    "api-version", "2022-01-01-preview",
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
            _ListHelper._build_schema_network_rule_set_read(cls._schema_on_200)

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_network_rule_set_read = None

    @classmethod
    def _build_schema_network_rule_set_read(cls, _schema):
        if cls._schema_network_rule_set_read is not None:
            _schema.id = cls._schema_network_rule_set_read.id
            _schema.location = cls._schema_network_rule_set_read.location
            _schema.name = cls._schema_network_rule_set_read.name
            _schema.properties = cls._schema_network_rule_set_read.properties
            _schema.system_data = cls._schema_network_rule_set_read.system_data
            _schema.type = cls._schema_network_rule_set_read.type
            return

        cls._schema_network_rule_set_read = _schema_network_rule_set_read = AAZObjectType()

        network_rule_set_read = _schema_network_rule_set_read
        network_rule_set_read.id = AAZStrType(
            flags={"read_only": True},
        )
        network_rule_set_read.location = AAZStrType(
            flags={"read_only": True},
        )
        network_rule_set_read.name = AAZStrType(
            flags={"read_only": True},
        )
        network_rule_set_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        network_rule_set_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        network_rule_set_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_network_rule_set_read.properties
        properties.default_action = AAZStrType(
            serialized_name="defaultAction",
        )
        properties.ip_rules = AAZListType(
            serialized_name="ipRules",
        )
        properties.public_network_access = AAZStrType(
            serialized_name="publicNetworkAccess",
        )
        properties.trusted_service_access_enabled = AAZBoolType(
            serialized_name="trustedServiceAccessEnabled",
        )
        properties.virtual_network_rules = AAZListType(
            serialized_name="virtualNetworkRules",
        )

        ip_rules = _schema_network_rule_set_read.properties.ip_rules
        ip_rules.Element = AAZObjectType()

        _element = _schema_network_rule_set_read.properties.ip_rules.Element
        _element.action = AAZStrType()
        _element.ip_mask = AAZStrType(
            serialized_name="ipMask",
        )

        virtual_network_rules = _schema_network_rule_set_read.properties.virtual_network_rules
        virtual_network_rules.Element = AAZObjectType()

        _element = _schema_network_rule_set_read.properties.virtual_network_rules.Element
        _element.ignore_missing_vnet_service_endpoint = AAZBoolType(
            serialized_name="ignoreMissingVnetServiceEndpoint",
        )
        _element.subnet = AAZObjectType()

        subnet = _schema_network_rule_set_read.properties.virtual_network_rules.Element.subnet
        subnet.id = AAZStrType()

        system_data = _schema_network_rule_set_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_network_rule_set_read.id
        _schema.location = cls._schema_network_rule_set_read.location
        _schema.name = cls._schema_network_rule_set_read.name
        _schema.properties = cls._schema_network_rule_set_read.properties
        _schema.system_data = cls._schema_network_rule_set_read.system_data
        _schema.type = cls._schema_network_rule_set_read.type


__all__ = ["List"]
