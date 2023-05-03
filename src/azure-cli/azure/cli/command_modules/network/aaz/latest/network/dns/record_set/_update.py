# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Update(AAZCommand):
    """Update a record set within a DNS zone.
    """

    _aaz_info = {
        "version": "2018-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/dnszones/{}/{}/{}", "2018-05-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.if_match = AAZStrArg(
            options=["--if-match"],
            help="Etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.",
        )
        _args_schema.if_none_match = AAZStrArg(
            options=["--if-none-match"],
            help="Set to `*` to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored.",
        )
        _args_schema.record_type = AAZStrArg(
            options=["--record-type"],
            help="Type of DNS record in this record set.",
            required=True,
            id_part="child_type_1",
            enum={"A": "A", "AAAA": "AAAA", "CAA": "CAA", "CNAME": "CNAME", "MX": "MX", "NS": "NS", "PTR": "PTR", "SOA": "SOA", "SRV": "SRV", "TXT": "TXT"},
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the record set, relative to the name of the zone.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.zone_name = AAZStrArg(
            options=["-z", "--zone-name"],
            help="Name of the DNS zone.",
            required=True,
            id_part="name",
        )
        _args_schema.ttl = AAZIntArg(
            options=["--ttl"],
            help="TTL of the records in the record set.",
            nullable=True,
        )
        _args_schema.metadata = AAZDictArg(
            options=["--metadata"],
            help="Metadata in space-separated key=value pairs. This overwrites any existing metadata.",
            nullable=True,
        )
        _args_schema.target_resource = AAZStrArg(
            options=["--target-resource"],
            help="ID of an Azure resource from which the DNS resource value is taken.",
            nullable=True,
        )

        metadata = cls._args_schema.metadata
        metadata.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.aaaa_records = AAZListArg(
            options=["--aaaa-records"],
            arg_group="Properties",
            help="The list of AAAA records in the record set.",
            nullable=True,
        )
        _args_schema.a_records = AAZListArg(
            options=["--a-records"],
            arg_group="Properties",
            help="The list of A records in the record set.",
            nullable=True,
        )
        _args_schema.cname_record = AAZObjectArg(
            options=["--cname-record"],
            arg_group="Properties",
            help="The CNAME record in the  record set.",
            nullable=True,
        )
        _args_schema.mx_records = AAZListArg(
            options=["--mx-records"],
            arg_group="Properties",
            help="The list of MX records in the record set.",
            nullable=True,
        )
        _args_schema.ns_records = AAZListArg(
            options=["--ns-records"],
            arg_group="Properties",
            help="The list of NS records in the record set.",
            nullable=True,
        )
        _args_schema.ptr_records = AAZListArg(
            options=["--ptr-records"],
            arg_group="Properties",
            help="The list of PTR records in the record set.",
            nullable=True,
        )
        _args_schema.soa_record = AAZObjectArg(
            options=["--soa-record"],
            arg_group="Properties",
            help="The SOA record in the record set.",
            nullable=True,
        )
        _args_schema.srv_records = AAZListArg(
            options=["--srv-records"],
            arg_group="Properties",
            help="The list of SRV records in the record set.",
            nullable=True,
        )
        _args_schema.txt_records = AAZListArg(
            options=["--txt-records"],
            arg_group="Properties",
            help="The list of TXT records in the record set.",
            nullable=True,
        )
        _args_schema.caa_records = AAZListArg(
            options=["--caa-records"],
            arg_group="Properties",
            help="The list of CAA records in the record set.",
            nullable=True,
        )

        aaaa_records = cls._args_schema.aaaa_records
        aaaa_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.aaaa_records.Element
        _element.ipv6_address = AAZStrArg(
            options=["ipv6-address"],
            help="The IPv6 address of this AAAA record.",
            nullable=True,
        )

        a_records = cls._args_schema.a_records
        a_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.a_records.Element
        _element.ipv4_address = AAZStrArg(
            options=["ipv4-address"],
            help="The IPv4 address of this A record.",
            nullable=True,
        )

        cname_record = cls._args_schema.cname_record
        cname_record.cname = AAZStrArg(
            options=["cname"],
            help="The canonical name for this CNAME record.",
            nullable=True,
        )

        mx_records = cls._args_schema.mx_records
        mx_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.mx_records.Element
        _element.exchange = AAZStrArg(
            options=["exchange"],
            help="The domain name of the mail host for this MX record.",
            nullable=True,
        )
        _element.preference = AAZIntArg(
            options=["preference"],
            help="The preference value for this MX record.",
            nullable=True,
        )

        ns_records = cls._args_schema.ns_records
        ns_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.ns_records.Element
        _element.nsdname = AAZStrArg(
            options=["nsdname"],
            help="The name server name for this NS record.",
            nullable=True,
        )

        ptr_records = cls._args_schema.ptr_records
        ptr_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.ptr_records.Element
        _element.ptrdname = AAZStrArg(
            options=["ptrdname"],
            help="The PTR target domain name for this PTR record.",
            nullable=True,
        )

        soa_record = cls._args_schema.soa_record
        soa_record.email = AAZStrArg(
            options=["email"],
            help="The email contact for this SOA record.",
            nullable=True,
        )
        soa_record.expire_time = AAZIntArg(
            options=["expire-time"],
            help="The expire time for this SOA record.",
            nullable=True,
        )
        soa_record.host = AAZStrArg(
            options=["host"],
            help="The domain name of the authoritative name server for this SOA record.",
            nullable=True,
        )
        soa_record.minimum_ttl = AAZIntArg(
            options=["minimum-ttl"],
            help="The minimum value for this SOA record. By convention this is used to determine the negative caching duration.",
            nullable=True,
        )
        soa_record.refresh_time = AAZIntArg(
            options=["refresh-time"],
            help="The refresh value for this SOA record.",
            nullable=True,
        )
        soa_record.retry_time = AAZIntArg(
            options=["retry-time"],
            help="The retry time for this SOA record.",
            nullable=True,
        )
        soa_record.serial_number = AAZIntArg(
            options=["serial-number"],
            help="The serial number for this SOA record.",
            nullable=True,
        )

        srv_records = cls._args_schema.srv_records
        srv_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.srv_records.Element
        _element.port = AAZIntArg(
            options=["port"],
            help="The port value for this SRV record.",
            nullable=True,
        )
        _element.priority = AAZIntArg(
            options=["priority"],
            help="The priority value for this SRV record.",
            nullable=True,
        )
        _element.target = AAZStrArg(
            options=["target"],
            help="The target domain name for this SRV record.",
            nullable=True,
        )
        _element.weight = AAZIntArg(
            options=["weight"],
            help="The weight value for this SRV record.",
            nullable=True,
        )

        txt_records = cls._args_schema.txt_records
        txt_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.txt_records.Element
        _element.value = AAZListArg(
            options=["value"],
            help="The text value of this TXT record.",
            nullable=True,
        )

        value = cls._args_schema.txt_records.Element.value
        value.Element = AAZStrArg(
            nullable=True,
        )

        caa_records = cls._args_schema.caa_records
        caa_records.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.caa_records.Element
        _element.flags = AAZIntArg(
            options=["flags"],
            help="The flags for this CAA record as an integer between 0 and 255.",
            nullable=True,
        )
        _element.tag = AAZStrArg(
            options=["tag"],
            help="The tag for this CAA record.",
            nullable=True,
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The value for this CAA record.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RecordSetsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.RecordSetsCreateOrUpdate(ctx=self.ctx)()
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

    class RecordSetsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName}",
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
                    "recordType", self.ctx.args.record_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "relativeRecordSetName", self.ctx.args.name,
                    skip_quote=True,
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
                **self.serialize_url_param(
                    "zoneName", self.ctx.args.zone_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-05-01",
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
            _UpdateHelper._build_schema_record_set_read(cls._schema_on_200)

            return cls._schema_on_200

    class RecordSetsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName}",
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
                    "recordType", self.ctx.args.record_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "relativeRecordSetName", self.ctx.args.name,
                    skip_quote=True,
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
                **self.serialize_url_param(
                    "zoneName", self.ctx.args.zone_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "If-Match", self.ctx.args.if_match,
                ),
                **self.serialize_header_param(
                    "If-None-Match", self.ctx.args.if_none_match,
                ),
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
            _UpdateHelper._build_schema_record_set_read(cls._schema_on_200_201)

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
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("AAAARecords", AAZListType, ".aaaa_records")
                properties.set_prop("ARecords", AAZListType, ".a_records")
                properties.set_prop("CNAMERecord", AAZObjectType, ".cname_record")
                properties.set_prop("MXRecords", AAZListType, ".mx_records")
                properties.set_prop("NSRecords", AAZListType, ".ns_records")
                properties.set_prop("PTRRecords", AAZListType, ".ptr_records")
                properties.set_prop("SOARecord", AAZObjectType, ".soa_record")
                properties.set_prop("SRVRecords", AAZListType, ".srv_records")
                properties.set_prop("TTL", AAZIntType, ".ttl")
                properties.set_prop("TXTRecords", AAZListType, ".txt_records")
                properties.set_prop("caaRecords", AAZListType, ".caa_records")
                properties.set_prop("metadata", AAZDictType, ".metadata")
                properties.set_prop("targetResource", AAZObjectType)

            aaaa_records = _builder.get(".properties.AAAARecords")
            if aaaa_records is not None:
                aaaa_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.AAAARecords[]")
            if _elements is not None:
                _elements.set_prop("ipv6Address", AAZStrType, ".ipv6_address")

            a_records = _builder.get(".properties.ARecords")
            if a_records is not None:
                a_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.ARecords[]")
            if _elements is not None:
                _elements.set_prop("ipv4Address", AAZStrType, ".ipv4_address")

            cname_record = _builder.get(".properties.CNAMERecord")
            if cname_record is not None:
                cname_record.set_prop("cname", AAZStrType, ".cname")

            mx_records = _builder.get(".properties.MXRecords")
            if mx_records is not None:
                mx_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.MXRecords[]")
            if _elements is not None:
                _elements.set_prop("exchange", AAZStrType, ".exchange")
                _elements.set_prop("preference", AAZIntType, ".preference")

            ns_records = _builder.get(".properties.NSRecords")
            if ns_records is not None:
                ns_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.NSRecords[]")
            if _elements is not None:
                _elements.set_prop("nsdname", AAZStrType, ".nsdname")

            ptr_records = _builder.get(".properties.PTRRecords")
            if ptr_records is not None:
                ptr_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.PTRRecords[]")
            if _elements is not None:
                _elements.set_prop("ptrdname", AAZStrType, ".ptrdname")

            soa_record = _builder.get(".properties.SOARecord")
            if soa_record is not None:
                soa_record.set_prop("email", AAZStrType, ".email")
                soa_record.set_prop("expireTime", AAZIntType, ".expire_time")
                soa_record.set_prop("host", AAZStrType, ".host")
                soa_record.set_prop("minimumTTL", AAZIntType, ".minimum_ttl")
                soa_record.set_prop("refreshTime", AAZIntType, ".refresh_time")
                soa_record.set_prop("retryTime", AAZIntType, ".retry_time")
                soa_record.set_prop("serialNumber", AAZIntType, ".serial_number")

            srv_records = _builder.get(".properties.SRVRecords")
            if srv_records is not None:
                srv_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.SRVRecords[]")
            if _elements is not None:
                _elements.set_prop("port", AAZIntType, ".port")
                _elements.set_prop("priority", AAZIntType, ".priority")
                _elements.set_prop("target", AAZStrType, ".target")
                _elements.set_prop("weight", AAZIntType, ".weight")

            txt_records = _builder.get(".properties.TXTRecords")
            if txt_records is not None:
                txt_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.TXTRecords[]")
            if _elements is not None:
                _elements.set_prop("value", AAZListType, ".value")

            value = _builder.get(".properties.TXTRecords[].value")
            if value is not None:
                value.set_elements(AAZStrType, ".")

            caa_records = _builder.get(".properties.caaRecords")
            if caa_records is not None:
                caa_records.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.caaRecords[]")
            if _elements is not None:
                _elements.set_prop("flags", AAZIntType, ".flags")
                _elements.set_prop("tag", AAZStrType, ".tag")
                _elements.set_prop("value", AAZStrType, ".value")

            metadata = _builder.get(".properties.metadata")
            if metadata is not None:
                metadata.set_elements(AAZStrType, ".")

            target_resource = _builder.get(".properties.targetResource")
            if target_resource is not None:
                target_resource.set_prop("id", AAZStrType, ".target_resource")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_record_set_read = None

    @classmethod
    def _build_schema_record_set_read(cls, _schema):
        if cls._schema_record_set_read is not None:
            _schema.etag = cls._schema_record_set_read.etag
            _schema.id = cls._schema_record_set_read.id
            _schema.name = cls._schema_record_set_read.name
            _schema.properties = cls._schema_record_set_read.properties
            _schema.type = cls._schema_record_set_read.type
            return

        cls._schema_record_set_read = _schema_record_set_read = AAZObjectType()

        record_set_read = _schema_record_set_read
        record_set_read.etag = AAZStrType()
        record_set_read.id = AAZStrType(
            flags={"read_only": True},
        )
        record_set_read.name = AAZStrType(
            flags={"read_only": True},
        )
        record_set_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        record_set_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_record_set_read.properties
        properties.aaaa_records = AAZListType(
            serialized_name="AAAARecords",
        )
        properties.a_records = AAZListType(
            serialized_name="ARecords",
        )
        properties.cname_record = AAZObjectType(
            serialized_name="CNAMERecord",
        )
        properties.mx_records = AAZListType(
            serialized_name="MXRecords",
        )
        properties.ns_records = AAZListType(
            serialized_name="NSRecords",
        )
        properties.ptr_records = AAZListType(
            serialized_name="PTRRecords",
        )
        properties.soa_record = AAZObjectType(
            serialized_name="SOARecord",
        )
        properties.srv_records = AAZListType(
            serialized_name="SRVRecords",
        )
        properties.ttl = AAZIntType(
            serialized_name="TTL",
        )
        properties.txt_records = AAZListType(
            serialized_name="TXTRecords",
        )
        properties.caa_records = AAZListType(
            serialized_name="caaRecords",
        )
        properties.fqdn = AAZStrType(
            flags={"read_only": True},
        )
        properties.metadata = AAZDictType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.target_resource = AAZObjectType(
            serialized_name="targetResource",
        )

        aaaa_records = _schema_record_set_read.properties.aaaa_records
        aaaa_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.aaaa_records.Element
        _element.ipv6_address = AAZStrType(
            serialized_name="ipv6Address",
        )

        a_records = _schema_record_set_read.properties.a_records
        a_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.a_records.Element
        _element.ipv4_address = AAZStrType(
            serialized_name="ipv4Address",
        )

        cname_record = _schema_record_set_read.properties.cname_record
        cname_record.cname = AAZStrType()

        mx_records = _schema_record_set_read.properties.mx_records
        mx_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.mx_records.Element
        _element.exchange = AAZStrType()
        _element.preference = AAZIntType()

        ns_records = _schema_record_set_read.properties.ns_records
        ns_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.ns_records.Element
        _element.nsdname = AAZStrType()

        ptr_records = _schema_record_set_read.properties.ptr_records
        ptr_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.ptr_records.Element
        _element.ptrdname = AAZStrType()

        soa_record = _schema_record_set_read.properties.soa_record
        soa_record.email = AAZStrType()
        soa_record.expire_time = AAZIntType(
            serialized_name="expireTime",
        )
        soa_record.host = AAZStrType()
        soa_record.minimum_ttl = AAZIntType(
            serialized_name="minimumTTL",
        )
        soa_record.refresh_time = AAZIntType(
            serialized_name="refreshTime",
        )
        soa_record.retry_time = AAZIntType(
            serialized_name="retryTime",
        )
        soa_record.serial_number = AAZIntType(
            serialized_name="serialNumber",
        )

        srv_records = _schema_record_set_read.properties.srv_records
        srv_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.srv_records.Element
        _element.port = AAZIntType()
        _element.priority = AAZIntType()
        _element.target = AAZStrType()
        _element.weight = AAZIntType()

        txt_records = _schema_record_set_read.properties.txt_records
        txt_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.txt_records.Element
        _element.value = AAZListType()

        value = _schema_record_set_read.properties.txt_records.Element.value
        value.Element = AAZStrType()

        caa_records = _schema_record_set_read.properties.caa_records
        caa_records.Element = AAZObjectType()

        _element = _schema_record_set_read.properties.caa_records.Element
        _element.flags = AAZIntType()
        _element.tag = AAZStrType()
        _element.value = AAZStrType()

        metadata = _schema_record_set_read.properties.metadata
        metadata.Element = AAZStrType()

        target_resource = _schema_record_set_read.properties.target_resource
        target_resource.id = AAZStrType()

        _schema.etag = cls._schema_record_set_read.etag
        _schema.id = cls._schema_record_set_read.id
        _schema.name = cls._schema_record_set_read.name
        _schema.properties = cls._schema_record_set_read.properties
        _schema.type = cls._schema_record_set_read.type


__all__ = ["Update"]
