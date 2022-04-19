# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResource(object):
    """
    The information about monitored resource.
    """

    #: A constant which can be used with the lifecycle_state property of a MonitoredResource.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResource.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResource.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResource.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResource.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResource.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MonitoredResource.
        :type id: str

        :param name:
            The value to assign to the name property of this MonitoredResource.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this MonitoredResource.
        :type display_name: str

        :param type:
            The value to assign to the type property of this MonitoredResource.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoredResource.
        :type compartment_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this MonitoredResource.
        :type tenant_id: str

        :param host_name:
            The value to assign to the host_name property of this MonitoredResource.
        :type host_name: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MonitoredResource.
        :type management_agent_id: str

        :param resource_time_zone:
            The value to assign to the resource_time_zone property of this MonitoredResource.
        :type resource_time_zone: str

        :param time_created:
            The value to assign to the time_created property of this MonitoredResource.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MonitoredResource.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoredResource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param properties:
            The value to assign to the properties property of this MonitoredResource.
        :type properties: list[oci.stack_monitoring.models.MonitoredResourceProperty]

        :param database_connection_details:
            The value to assign to the database_connection_details property of this MonitoredResource.
        :type database_connection_details: oci.stack_monitoring.models.ConnectionDetails

        :param credentials:
            The value to assign to the credentials property of this MonitoredResource.
        :type credentials: oci.stack_monitoring.models.MonitoredResourceCredential

        :param aliases:
            The value to assign to the aliases property of this MonitoredResource.
        :type aliases: oci.stack_monitoring.models.MonitoredResourceAliasCredential

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MonitoredResource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MonitoredResource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MonitoredResource.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'tenant_id': 'str',
            'host_name': 'str',
            'management_agent_id': 'str',
            'resource_time_zone': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'properties': 'list[MonitoredResourceProperty]',
            'database_connection_details': 'ConnectionDetails',
            'credentials': 'MonitoredResourceCredential',
            'aliases': 'MonitoredResourceAliasCredential',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'tenant_id': 'tenantId',
            'host_name': 'hostName',
            'management_agent_id': 'managementAgentId',
            'resource_time_zone': 'resourceTimeZone',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'properties': 'properties',
            'database_connection_details': 'databaseConnectionDetails',
            'credentials': 'credentials',
            'aliases': 'aliases',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._display_name = None
        self._type = None
        self._compartment_id = None
        self._tenant_id = None
        self._host_name = None
        self._management_agent_id = None
        self._resource_time_zone = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._properties = None
        self._database_connection_details = None
        self._credentials = None
        self._aliases = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MonitoredResource.
        The `OCID`__ of monitored resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MonitoredResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MonitoredResource.
        The `OCID`__ of monitored resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MonitoredResource.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MonitoredResource.
        Monitored resource name.


        :return: The name of this MonitoredResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MonitoredResource.
        Monitored resource name.


        :param name: The name of this MonitoredResource.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this MonitoredResource.
        Monitored resource display name.


        :return: The display_name of this MonitoredResource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MonitoredResource.
        Monitored resource display name.


        :param display_name: The display_name of this MonitoredResource.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MonitoredResource.
        Monitored resource type


        :return: The type of this MonitoredResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MonitoredResource.
        Monitored resource type


        :param type: The type of this MonitoredResource.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoredResource.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoredResource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoredResource.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoredResource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this MonitoredResource.
        Tenancy Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenant_id of this MonitoredResource.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this MonitoredResource.
        Tenancy Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenant_id: The tenant_id of this MonitoredResource.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def host_name(self):
        """
        Gets the host_name of this MonitoredResource.
        Monitored resource host name.


        :return: The host_name of this MonitoredResource.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this MonitoredResource.
        Monitored resource host name.


        :param host_name: The host_name of this MonitoredResource.
        :type: str
        """
        self._host_name = host_name

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this MonitoredResource.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MonitoredResource.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MonitoredResource.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MonitoredResource.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def resource_time_zone(self):
        """
        Gets the resource_time_zone of this MonitoredResource.
        Time zone in the form of tz database canonical zone ID.


        :return: The resource_time_zone of this MonitoredResource.
        :rtype: str
        """
        return self._resource_time_zone

    @resource_time_zone.setter
    def resource_time_zone(self, resource_time_zone):
        """
        Sets the resource_time_zone of this MonitoredResource.
        Time zone in the form of tz database canonical zone ID.


        :param resource_time_zone: The resource_time_zone of this MonitoredResource.
        :type: str
        """
        self._resource_time_zone = resource_time_zone

    @property
    def time_created(self):
        """
        Gets the time_created of this MonitoredResource.
        The time the the resource was created. An RFC3339 formatted datetime string


        :return: The time_created of this MonitoredResource.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MonitoredResource.
        The time the the resource was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this MonitoredResource.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MonitoredResource.
        The time the the resource was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this MonitoredResource.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MonitoredResource.
        The time the the resource was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this MonitoredResource.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MonitoredResource.
        Lifecycle state of the monitored resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MonitoredResource.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoredResource.
        Lifecycle state of the monitored resource.


        :param lifecycle_state: The lifecycle_state of this MonitoredResource.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def properties(self):
        """
        Gets the properties of this MonitoredResource.
        List of monitored resource properties


        :return: The properties of this MonitoredResource.
        :rtype: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this MonitoredResource.
        List of monitored resource properties


        :param properties: The properties of this MonitoredResource.
        :type: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        self._properties = properties

    @property
    def database_connection_details(self):
        """
        Gets the database_connection_details of this MonitoredResource.

        :return: The database_connection_details of this MonitoredResource.
        :rtype: oci.stack_monitoring.models.ConnectionDetails
        """
        return self._database_connection_details

    @database_connection_details.setter
    def database_connection_details(self, database_connection_details):
        """
        Sets the database_connection_details of this MonitoredResource.

        :param database_connection_details: The database_connection_details of this MonitoredResource.
        :type: oci.stack_monitoring.models.ConnectionDetails
        """
        self._database_connection_details = database_connection_details

    @property
    def credentials(self):
        """
        Gets the credentials of this MonitoredResource.

        :return: The credentials of this MonitoredResource.
        :rtype: oci.stack_monitoring.models.MonitoredResourceCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this MonitoredResource.

        :param credentials: The credentials of this MonitoredResource.
        :type: oci.stack_monitoring.models.MonitoredResourceCredential
        """
        self._credentials = credentials

    @property
    def aliases(self):
        """
        Gets the aliases of this MonitoredResource.

        :return: The aliases of this MonitoredResource.
        :rtype: oci.stack_monitoring.models.MonitoredResourceAliasCredential
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this MonitoredResource.

        :param aliases: The aliases of this MonitoredResource.
        :type: oci.stack_monitoring.models.MonitoredResourceAliasCredential
        """
        self._aliases = aliases

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MonitoredResource.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MonitoredResource.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MonitoredResource.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MonitoredResource.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MonitoredResource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MonitoredResource.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MonitoredResource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MonitoredResource.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MonitoredResource.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MonitoredResource.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MonitoredResource.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MonitoredResource.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
