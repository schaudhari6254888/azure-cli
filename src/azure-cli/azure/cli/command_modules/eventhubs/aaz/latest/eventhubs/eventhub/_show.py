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
    "eventhubs eventhub show",
)
class Show(AAZCommand):
    """Get an Event Hubs description for the specified Event Hub.
    """

    _aaz_info = {
        "version": "2023-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventhub/namespaces/{}/eventhubs/{}", "2023-01-01-preview"],
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
        _args_schema.event_hub_name = AAZStrArg(
            options=["-n", "--name", "--event-hub-name"],
            help="The Event Hub name",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                max_length=256,
                min_length=1,
            ),
        )
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The Namespace name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9-]{6,50}[a-zA-Z0-9]$",
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
        self.EventHubsGet(ctx=self.ctx)()
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

    class EventHubsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}",
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
                    "eventHubName", self.ctx.args.event_hub_name,
                    required=True,
                ),
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
                    "api-version", "2023-01-01-preview",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.capture_description = AAZObjectType(
                serialized_name="captureDescription",
            )
            properties.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            properties.message_retention_in_days = AAZIntType(
                serialized_name="messageRetentionInDays",
            )
            properties.partition_count = AAZIntType(
                serialized_name="partitionCount",
            )
            properties.partition_ids = AAZListType(
                serialized_name="partitionIds",
                flags={"read_only": True},
            )
            properties.retention_description = AAZObjectType(
                serialized_name="retentionDescription",
            )
            properties.status = AAZStrType()
            properties.updated_at = AAZStrType(
                serialized_name="updatedAt",
                flags={"read_only": True},
            )

            capture_description = cls._schema_on_200.properties.capture_description
            capture_description.destination = AAZObjectType()
            capture_description.enabled = AAZBoolType()
            capture_description.encoding = AAZStrType()
            capture_description.identity = AAZObjectType()
            capture_description.interval_in_seconds = AAZIntType(
                serialized_name="intervalInSeconds",
            )
            capture_description.size_limit_in_bytes = AAZIntType(
                serialized_name="sizeLimitInBytes",
            )
            capture_description.skip_empty_archives = AAZBoolType(
                serialized_name="skipEmptyArchives",
            )

            destination = cls._schema_on_200.properties.capture_description.destination
            destination.name = AAZStrType()
            destination.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.capture_description.destination.properties
            properties.archive_name_format = AAZStrType(
                serialized_name="archiveNameFormat",
            )
            properties.blob_container = AAZStrType(
                serialized_name="blobContainer",
            )
            properties.data_lake_account_name = AAZStrType(
                serialized_name="dataLakeAccountName",
            )
            properties.data_lake_folder_path = AAZStrType(
                serialized_name="dataLakeFolderPath",
            )
            properties.data_lake_subscription_id = AAZStrType(
                serialized_name="dataLakeSubscriptionId",
            )
            properties.storage_account_resource_id = AAZStrType(
                serialized_name="storageAccountResourceId",
            )

            identity = cls._schema_on_200.properties.capture_description.identity
            identity.type = AAZStrType()
            identity.user_assigned_identity = AAZStrType(
                serialized_name="userAssignedIdentity",
            )

            partition_ids = cls._schema_on_200.properties.partition_ids
            partition_ids.Element = AAZStrType()

            retention_description = cls._schema_on_200.properties.retention_description
            retention_description.cleanup_policy = AAZStrType(
                serialized_name="cleanupPolicy",
            )
            retention_description.retention_time_in_hours = AAZIntType(
                serialized_name="retentionTimeInHours",
            )
            retention_description.tombstone_retention_time_in_hours = AAZIntType(
                serialized_name="tombstoneRetentionTimeInHours",
            )

            system_data = cls._schema_on_200.system_data
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

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
