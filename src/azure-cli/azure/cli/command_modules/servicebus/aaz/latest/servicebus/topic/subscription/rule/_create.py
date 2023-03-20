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
    "servicebus topic subscription rule create",
)
class Create(AAZCommand):
    """Create a new rule and updates an existing rule
    """

    _aaz_info = {
        "version": "2022-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.servicebus/namespaces/{}/topics/{}/subscriptions/{}/rules/{}", "2022-10-01-preview"],
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
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The namespace name",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.rule_name = AAZStrArg(
            options=["-n", "--name", "--rule-name"],
            help="The rule name.",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=1,
            ),
        )
        _args_schema.subscription_name = AAZStrArg(
            options=["--subscription-name"],
            help="The subscription name.",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=1,
            ),
        )
        _args_schema.topic_name = AAZStrArg(
            options=["--topic-name"],
            help="The topic name.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        # define Arg Group "Action"

        _args_schema = cls._args_schema
        _args_schema.action_compatibility_level = AAZIntArg(
            options=["--action-compatibility-level"],
            arg_group="Action",
            help="This property is reserved for future use. An integer value showing the compatibility level, currently hard-coded to 20.",
        )
        _args_schema.action_requires_preprocessing = AAZBoolArg(
            options=["--action-requires-preprocessing"],
            arg_group="Action",
            help="Value that indicates whether the rule action requires preprocessing.",
            default=True,
        )
        _args_schema.action_sql_expression = AAZStrArg(
            options=["--action-sql-expression"],
            arg_group="Action",
            help="SQL expression. e.g. MyProperty='ABC'",
        )

        # define Arg Group "CorrelationFilter"

        _args_schema = cls._args_schema
        _args_schema.content_type = AAZStrArg(
            options=["--content-type"],
            arg_group="CorrelationFilter",
            help="Content type of the message.",
        )
        _args_schema.correlation_filter_property = AAZDictArg(
            options=["--correlation-filter", "--correlation-filter-property"],
            arg_group="CorrelationFilter",
            help="dictionary object for custom filters",
        )
        _args_schema.correlation_id = AAZStrArg(
            options=["--correlation-id"],
            arg_group="CorrelationFilter",
            help="Identifier of the correlation.",
        )
        _args_schema.label = AAZStrArg(
            options=["--label"],
            arg_group="CorrelationFilter",
            help="Application specific label.",
        )
        _args_schema.message_id = AAZStrArg(
            options=["--message-id"],
            arg_group="CorrelationFilter",
            help="Identifier of the message.",
        )
        _args_schema.reply_to = AAZStrArg(
            options=["--reply-to"],
            arg_group="CorrelationFilter",
            help="Address of the queue to reply to.",
        )
        _args_schema.reply_to_session_id = AAZStrArg(
            options=["--reply-to-session-id"],
            arg_group="CorrelationFilter",
            help="Session identifier to reply to.",
        )
        _args_schema.enable_correlation_preprocessing = AAZBoolArg(
            options=["--requires-preprocessing", "--enable-correlation-preprocessing"],
            arg_group="CorrelationFilter",
            help="Value that indicates whether the rule action requires preprocessing.",
        )
        _args_schema.session_id = AAZStrArg(
            options=["--session-id"],
            arg_group="CorrelationFilter",
            help="Session identifier.",
        )
        _args_schema.to = AAZStrArg(
            options=["--to"],
            arg_group="CorrelationFilter",
            help="Address to send to.",
        )

        correlation_filter_property = cls._args_schema.correlation_filter_property
        correlation_filter_property.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.filter_type = AAZStrArg(
            options=["--filter-type"],
            arg_group="Properties",
            help="Filter type that is evaluated against a BrokeredMessage.",
            enum={"CorrelationFilter": "CorrelationFilter", "SqlFilter": "SqlFilter"},
        )

        # define Arg Group "SqlFilter"

        _args_schema = cls._args_schema
        _args_schema.compatibility_level = AAZIntArg(
            options=["--compatibility-level"],
            arg_group="SqlFilter",
            help="This property is reserved for future use. An integer value showing the compatibility level, currently hard-coded to 20.",
        )
        _args_schema.enable_sql_preprocessing = AAZBoolArg(
            options=["--enable-sql-preprocessing"],
            arg_group="SqlFilter",
            help="Value that indicates whether the rule action requires preprocessing.",
        )
        _args_schema.filter_sql_expression = AAZStrArg(
            options=["--filter-sql-expression"],
            arg_group="SqlFilter",
            help="The SQL expression. e.g. MyProperty='ABC'",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RulesCreateOrUpdate(ctx=self.ctx)()
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

    class RulesCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName}/rules/{ruleName}",
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
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "ruleName", self.ctx.args.rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionName", self.ctx.args.subscription_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "topicName", self.ctx.args.topic_name,
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
                properties.set_prop("action", AAZObjectType)
                properties.set_prop("correlationFilter", AAZObjectType)
                properties.set_prop("filterType", AAZStrType, ".filter_type")
                properties.set_prop("sqlFilter", AAZObjectType)

            action = _builder.get(".properties.action")
            if action is not None:
                action.set_prop("compatibilityLevel", AAZIntType, ".action_compatibility_level")
                action.set_prop("requiresPreprocessing", AAZBoolType, ".action_requires_preprocessing")
                action.set_prop("sqlExpression", AAZStrType, ".action_sql_expression")

            correlation_filter = _builder.get(".properties.correlationFilter")
            if correlation_filter is not None:
                correlation_filter.set_prop("contentType", AAZStrType, ".content_type")
                correlation_filter.set_prop("correlationFilterProperty", AAZDictType, ".correlation_filter_property")
                correlation_filter.set_prop("correlationId", AAZStrType, ".correlation_id")
                correlation_filter.set_prop("label", AAZStrType, ".label")
                correlation_filter.set_prop("messageId", AAZStrType, ".message_id")
                correlation_filter.set_prop("replyTo", AAZStrType, ".reply_to")
                correlation_filter.set_prop("replyToSessionId", AAZStrType, ".reply_to_session_id")
                correlation_filter.set_prop("requiresPreprocessing", AAZBoolType, ".enable_correlation_preprocessing")
                correlation_filter.set_prop("sessionId", AAZStrType, ".session_id")
                correlation_filter.set_prop("to", AAZStrType, ".to")

            correlation_filter_property = _builder.get(".properties.correlationFilter.correlationFilterProperty")
            if correlation_filter_property is not None:
                correlation_filter_property.set_elements(AAZStrType, ".")

            sql_filter = _builder.get(".properties.sqlFilter")
            if sql_filter is not None:
                sql_filter.set_prop("compatibilityLevel", AAZIntType, ".compatibility_level")
                sql_filter.set_prop("requiresPreprocessing", AAZBoolType, ".enable_sql_preprocessing")
                sql_filter.set_prop("sqlExpression", AAZStrType, ".filter_sql_expression")

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
            properties.action = AAZObjectType()
            properties.correlation_filter = AAZObjectType(
                serialized_name="correlationFilter",
            )
            properties.filter_type = AAZStrType(
                serialized_name="filterType",
            )
            properties.sql_filter = AAZObjectType(
                serialized_name="sqlFilter",
            )

            action = cls._schema_on_200.properties.action
            action.compatibility_level = AAZIntType(
                serialized_name="compatibilityLevel",
            )
            action.requires_preprocessing = AAZBoolType(
                serialized_name="requiresPreprocessing",
            )
            action.sql_expression = AAZStrType(
                serialized_name="sqlExpression",
            )

            correlation_filter = cls._schema_on_200.properties.correlation_filter
            correlation_filter.content_type = AAZStrType(
                serialized_name="contentType",
            )
            correlation_filter.correlation_filter_property = AAZDictType(
                serialized_name="correlationFilterProperty",
            )
            correlation_filter.correlation_id = AAZStrType(
                serialized_name="correlationId",
            )
            correlation_filter.label = AAZStrType()
            correlation_filter.message_id = AAZStrType(
                serialized_name="messageId",
            )
            correlation_filter.reply_to = AAZStrType(
                serialized_name="replyTo",
            )
            correlation_filter.reply_to_session_id = AAZStrType(
                serialized_name="replyToSessionId",
            )
            correlation_filter.requires_preprocessing = AAZBoolType(
                serialized_name="requiresPreprocessing",
            )
            correlation_filter.session_id = AAZStrType(
                serialized_name="sessionId",
            )
            correlation_filter.to = AAZStrType()

            correlation_filter_property = cls._schema_on_200.properties.correlation_filter.correlation_filter_property
            correlation_filter_property.Element = AAZStrType()

            sql_filter = cls._schema_on_200.properties.sql_filter
            sql_filter.compatibility_level = AAZIntType(
                serialized_name="compatibilityLevel",
            )
            sql_filter.requires_preprocessing = AAZBoolType(
                serialized_name="requiresPreprocessing",
            )
            sql_filter.sql_expression = AAZStrType(
                serialized_name="sqlExpression",
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
