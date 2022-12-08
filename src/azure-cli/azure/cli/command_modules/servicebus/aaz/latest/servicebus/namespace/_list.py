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
    "servicebus namespace list",
)
class List(AAZCommand):
    """List the available namespaces within a resource group.
    """

    _aaz_info = {
        "version": "2022-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.servicebus/namespaces", "2022-01-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

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
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NamespacesListByResourceGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class NamespacesListByResourceGroup(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _build_schema_system_data_read(_element.system_data)
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.alternate_name = AAZStrType(
                serialized_name="alternateName",
            )
            properties.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            properties.disable_local_auth = AAZBoolType(
                serialized_name="disableLocalAuth",
            )
            properties.encryption = AAZObjectType(
                flags={"client_flatten": True},
            )
            properties.metric_id = AAZStrType(
                serialized_name="metricId",
                flags={"read_only": True},
            )
            properties.minimum_tls_version = AAZStrType(
                serialized_name="minimumTlsVersion",
            )
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_network_access = AAZStrType(
                serialized_name="publicNetworkAccess",
            )
            properties.service_bus_endpoint = AAZStrType(
                serialized_name="serviceBusEndpoint",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.updated_at = AAZStrType(
                serialized_name="updatedAt",
                flags={"read_only": True},
            )
            properties.zone_redundant = AAZBoolType(
                serialized_name="zoneRedundant",
            )

            encryption = cls._schema_on_200.value.Element.properties.encryption
            encryption.key_source = AAZStrType(
                serialized_name="keySource",
            )
            encryption.key_vault_properties = AAZListType(
                serialized_name="keyVaultProperties",
            )
            encryption.require_infrastructure_encryption = AAZBoolType(
                serialized_name="requireInfrastructureEncryption",
            )

            key_vault_properties = cls._schema_on_200.value.Element.properties.encryption.key_vault_properties
            key_vault_properties.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.encryption.key_vault_properties.Element
            _element.identity = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.key_name = AAZStrType(
                serialized_name="keyName",
            )
            _element.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
            )
            _element.key_version = AAZStrType(
                serialized_name="keyVersion",
            )

            identity = cls._schema_on_200.value.Element.properties.encryption.key_vault_properties.Element.identity
            identity.user_assigned_identity = AAZStrType(
                serialized_name="userAssignedIdentity",
            )

            private_endpoint_connections = cls._schema_on_200.value.Element.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _build_schema_system_data_read(_element.system_data)
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            private_endpoint = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType()

            private_link_service_connection_state = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType()

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


_schema_system_data_read = None


def _build_schema_system_data_read(_schema):
    global _schema_system_data_read
    if _schema_system_data_read is not None:
        _schema.created_at = _schema_system_data_read.created_at
        _schema.created_by = _schema_system_data_read.created_by
        _schema.created_by_type = _schema_system_data_read.created_by_type
        _schema.last_modified_at = _schema_system_data_read.last_modified_at
        _schema.last_modified_by = _schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = _schema_system_data_read.last_modified_by_type
        return

    _schema_system_data_read = AAZObjectType(
        flags={"read_only": True}
    )

    system_data_read = _schema_system_data_read
    system_data_read.created_at = AAZStrType(
        serialized_name="createdAt",
    )
    system_data_read.created_by = AAZStrType(
        serialized_name="createdBy",
    )
    system_data_read.created_by_type = AAZStrType(
        serialized_name="createdByType",
    )
    system_data_read.last_modified_at = AAZStrType(
        serialized_name="lastModifiedAt",
    )
    system_data_read.last_modified_by = AAZStrType(
        serialized_name="lastModifiedBy",
    )
    system_data_read.last_modified_by_type = AAZStrType(
        serialized_name="lastModifiedByType",
    )

    _schema.created_at = _schema_system_data_read.created_at
    _schema.created_by = _schema_system_data_read.created_by
    _schema.created_by_type = _schema_system_data_read.created_by_type
    _schema.last_modified_at = _schema_system_data_read.last_modified_at
    _schema.last_modified_by = _schema_system_data_read.last_modified_by
    _schema.last_modified_by_type = _schema_system_data_read.last_modified_by_type


__all__ = ["List"]
