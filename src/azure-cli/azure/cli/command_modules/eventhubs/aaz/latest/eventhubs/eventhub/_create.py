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
    "eventhubs eventhub create",
)
class Create(AAZCommand):
    """Create a new Event Hub as a nested resource within a Namespace.
    """

    _aaz_info = {
        "version": "2022-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventhub/namespaces/{}/eventhubs/{}", "2022-10-01-preview"],
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
            fmt=AAZStrArgFormat(
                max_length=256,
                min_length=1,
            ),
        )
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

        # define Arg Group "CaptureDescription"

        _args_schema = cls._args_schema
        _args_schema.destination_name = AAZStrArg(
            options=["--destination-name"],
            arg_group="CaptureDescription",
            help="Name for capture destination",
        )
        _args_schema.archive_name_format = AAZStrArg(
            options=["--archive-name-format"],
            arg_group="CaptureDescription",
            help="Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order",
        )
        _args_schema.blob_container = AAZStrArg(
            options=["--blob-container"],
            arg_group="CaptureDescription",
            help="Blob container Name",
        )
        _args_schema.storage_account = AAZStrArg(
            options=["--storage-account"],
            arg_group="CaptureDescription",
            help="Resource id of the storage account to be used to create the blobs",
        )
        _args_schema.enable_capture = AAZBoolArg(
            options=["--enable-capture"],
            arg_group="CaptureDescription",
            help="A value that indicates whether capture description is enabled.",
        )
        _args_schema.encoding = AAZStrArg(
            options=["--encoding"],
            arg_group="CaptureDescription",
            help="Enumerates the possible values for the encoding format of capture description. Note: 'AvroDeflate' will be deprecated in New API Version",
            enum={"Avro": "Avro", "AvroDeflate": "AvroDeflate"},
        )
        _args_schema.capture_interval = AAZIntArg(
            options=["--capture-interval"],
            arg_group="CaptureDescription",
            help="The time window allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds",
        )
        _args_schema.capture_size_limit = AAZIntArg(
            options=["--capture-size-limit"],
            arg_group="CaptureDescription",
            help="The size window defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 to 524288000 bytes",
        )
        _args_schema.skip_empty_archives = AAZBoolArg(
            options=["--skip-empty-archives"],
            arg_group="CaptureDescription",
            help="A value that indicates whether to Skip Empty Archives",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.message_retention_in_days = AAZIntArg(
            options=["--message-retention-in-days"],
            arg_group="Properties",
            help="Number of days to retain the events for this Event Hub, value should be 1 to 7 days",
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )
        _args_schema.partition_count = AAZIntArg(
            options=["--partition-count"],
            arg_group="Properties",
            help="Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions.",
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="Enumerates the possible values for the status of the Event Hub.",
            enum={"Active": "Active", "Creating": "Creating", "Deleting": "Deleting", "Disabled": "Disabled", "ReceiveDisabled": "ReceiveDisabled", "Renaming": "Renaming", "Restoring": "Restoring", "SendDisabled": "SendDisabled", "Unknown": "Unknown"},
        )

        # define Arg Group "RetentionDescription"

        _args_schema = cls._args_schema
        _args_schema.cleanup_policy = AAZStrArg(
            options=["--cleanup-policy"],
            arg_group="RetentionDescription",
            help="Enumerates the possible values for cleanup policy",
            enum={"Compact": "Compact", "Delete": "Delete"},
        )
        _args_schema.retention_time_in_hours = AAZIntArg(
            options=["--retention-time", "--retention-time-in-hours"],
            arg_group="RetentionDescription",
            help="Number of hours to retain the events for this Event Hub. This value is only used when cleanupPolicy is Delete. If cleanupPolicy is Compaction the returned value of this property is Long.MaxValue",
        )
        _args_schema.tombstone_retention_time_in_hours = AAZIntArg(
            options=["-t", "--tombstone-retention-time-in-hours"],
            arg_group="RetentionDescription",
            help="Number of hours to retain the tombstone markers of a compacted Event Hub. This value is only used when cleanupPolicy is Compaction. Consumer must complete reading the tombstone marker within this specified amount of time if consumer begins from starting offset to ensure they get a valid snapshot for the specific key described by the tombstone marker within the compacted Event Hub",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.EventHubsCreateOrUpdate(ctx=self.ctx)()
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

    class EventHubsCreateOrUpdate(AAZHttpOperation):
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
            return "PUT"

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
                    "api-version", "2022-10-01-preview",
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
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("captureDescription", AAZObjectType)
                properties.set_prop("messageRetentionInDays", AAZIntType, ".message_retention_in_days")
                properties.set_prop("partitionCount", AAZIntType, ".partition_count")
                properties.set_prop("retentionDescription", AAZObjectType)
                properties.set_prop("status", AAZStrType, ".status")

            capture_description = _builder.get(".properties.captureDescription")
            if capture_description is not None:
                capture_description.set_prop("destination", AAZObjectType)
                capture_description.set_prop("enabled", AAZBoolType, ".enable_capture")
                capture_description.set_prop("encoding", AAZStrType, ".encoding")
                capture_description.set_prop("intervalInSeconds", AAZIntType, ".capture_interval")
                capture_description.set_prop("sizeLimitInBytes", AAZIntType, ".capture_size_limit")
                capture_description.set_prop("skipEmptyArchives", AAZBoolType, ".skip_empty_archives")

            destination = _builder.get(".properties.captureDescription.destination")
            if destination is not None:
                destination.set_prop("name", AAZStrType, ".destination_name")
                destination.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties.captureDescription.destination.properties")
            if properties is not None:
                properties.set_prop("archiveNameFormat", AAZStrType, ".archive_name_format")
                properties.set_prop("blobContainer", AAZStrType, ".blob_container")
                properties.set_prop("storageAccountResourceId", AAZStrType, ".storage_account")

            retention_description = _builder.get(".properties.retentionDescription")
            if retention_description is not None:
                retention_description.set_prop("cleanupPolicy", AAZStrType, ".cleanup_policy")
                retention_description.set_prop("retentionTimeInHours", AAZIntType, ".retention_time_in_hours")
                retention_description.set_prop("tombstoneRetentionTimeInHours", AAZIntType, ".tombstone_retention_time_in_hours")

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


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
