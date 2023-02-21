# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalAsm(object):
    """
    The details of an external ASM.
    """

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "NOT_CONNECTED"
    LIFECYCLE_STATE_NOT_CONNECTED = "NOT_CONNECTED"

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExternalAsm.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalAsm object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalAsm.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalAsm.
        :type display_name: str

        :param component_name:
            The value to assign to the component_name property of this ExternalAsm.
        :type component_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalAsm.
        :type compartment_id: str

        :param external_db_system_id:
            The value to assign to the external_db_system_id property of this ExternalAsm.
        :type external_db_system_id: str

        :param external_connector_id:
            The value to assign to the external_connector_id property of this ExternalAsm.
        :type external_connector_id: str

        :param grid_home:
            The value to assign to the grid_home property of this ExternalAsm.
        :type grid_home: str

        :param is_cluster:
            The value to assign to the is_cluster property of this ExternalAsm.
        :type is_cluster: bool

        :param is_flex_enabled:
            The value to assign to the is_flex_enabled property of this ExternalAsm.
        :type is_flex_enabled: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalAsm.
            Allowed values for this property are: "CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalAsm.
        :type lifecycle_details: str

        :param serviced_databases:
            The value to assign to the serviced_databases property of this ExternalAsm.
        :type serviced_databases: list[oci.database_management.models.ExternalAsmServicedDatabase]

        :param additional_details:
            The value to assign to the additional_details property of this ExternalAsm.
        :type additional_details: dict(str, str)

        :param time_created:
            The value to assign to the time_created property of this ExternalAsm.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalAsm.
        :type time_updated: datetime

        :param version:
            The value to assign to the version property of this ExternalAsm.
        :type version: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'component_name': 'str',
            'compartment_id': 'str',
            'external_db_system_id': 'str',
            'external_connector_id': 'str',
            'grid_home': 'str',
            'is_cluster': 'bool',
            'is_flex_enabled': 'bool',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'serviced_databases': 'list[ExternalAsmServicedDatabase]',
            'additional_details': 'dict(str, str)',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'version': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'component_name': 'componentName',
            'compartment_id': 'compartmentId',
            'external_db_system_id': 'externalDbSystemId',
            'external_connector_id': 'externalConnectorId',
            'grid_home': 'gridHome',
            'is_cluster': 'isCluster',
            'is_flex_enabled': 'isFlexEnabled',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'serviced_databases': 'servicedDatabases',
            'additional_details': 'additionalDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'version': 'version'
        }

        self._id = None
        self._display_name = None
        self._component_name = None
        self._compartment_id = None
        self._external_db_system_id = None
        self._external_connector_id = None
        self._grid_home = None
        self._is_cluster = None
        self._is_flex_enabled = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._serviced_databases = None
        self._additional_details = None
        self._time_created = None
        self._time_updated = None
        self._version = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalAsm.
        The `OCID`__ of the external ASM.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalAsm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalAsm.
        The `OCID`__ of the external ASM.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalAsm.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalAsm.
        The user-friendly name for the external ASM. The name does not have to be unique.


        :return: The display_name of this ExternalAsm.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalAsm.
        The user-friendly name for the external ASM. The name does not have to be unique.


        :param display_name: The display_name of this ExternalAsm.
        :type: str
        """
        self._display_name = display_name

    @property
    def component_name(self):
        """
        **[Required]** Gets the component_name of this ExternalAsm.
        The name of the external ASM.


        :return: The component_name of this ExternalAsm.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this ExternalAsm.
        The name of the external ASM.


        :param component_name: The component_name of this ExternalAsm.
        :type: str
        """
        self._component_name = component_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalAsm.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalAsm.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalAsm.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalAsm.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def external_db_system_id(self):
        """
        **[Required]** Gets the external_db_system_id of this ExternalAsm.
        The `OCID`__ of the external DB system that the ASM is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_db_system_id of this ExternalAsm.
        :rtype: str
        """
        return self._external_db_system_id

    @external_db_system_id.setter
    def external_db_system_id(self, external_db_system_id):
        """
        Sets the external_db_system_id of this ExternalAsm.
        The `OCID`__ of the external DB system that the ASM is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_db_system_id: The external_db_system_id of this ExternalAsm.
        :type: str
        """
        self._external_db_system_id = external_db_system_id

    @property
    def external_connector_id(self):
        """
        Gets the external_connector_id of this ExternalAsm.
        The `OCID`__ of the external connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_connector_id of this ExternalAsm.
        :rtype: str
        """
        return self._external_connector_id

    @external_connector_id.setter
    def external_connector_id(self, external_connector_id):
        """
        Sets the external_connector_id of this ExternalAsm.
        The `OCID`__ of the external connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_connector_id: The external_connector_id of this ExternalAsm.
        :type: str
        """
        self._external_connector_id = external_connector_id

    @property
    def grid_home(self):
        """
        Gets the grid_home of this ExternalAsm.
        The directory in which ASM is installed. This is the same directory in which Oracle Grid Infrastructure is installed.


        :return: The grid_home of this ExternalAsm.
        :rtype: str
        """
        return self._grid_home

    @grid_home.setter
    def grid_home(self, grid_home):
        """
        Sets the grid_home of this ExternalAsm.
        The directory in which ASM is installed. This is the same directory in which Oracle Grid Infrastructure is installed.


        :param grid_home: The grid_home of this ExternalAsm.
        :type: str
        """
        self._grid_home = grid_home

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this ExternalAsm.
        Indicates whether the ASM is a cluster ASM or not.


        :return: The is_cluster of this ExternalAsm.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this ExternalAsm.
        Indicates whether the ASM is a cluster ASM or not.


        :param is_cluster: The is_cluster of this ExternalAsm.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def is_flex_enabled(self):
        """
        Gets the is_flex_enabled of this ExternalAsm.
        Indicates whether Oracle Flex ASM is enabled or not.


        :return: The is_flex_enabled of this ExternalAsm.
        :rtype: bool
        """
        return self._is_flex_enabled

    @is_flex_enabled.setter
    def is_flex_enabled(self, is_flex_enabled):
        """
        Sets the is_flex_enabled of this ExternalAsm.
        Indicates whether Oracle Flex ASM is enabled or not.


        :param is_flex_enabled: The is_flex_enabled of this ExternalAsm.
        :type: bool
        """
        self._is_flex_enabled = is_flex_enabled

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExternalAsm.
        The current lifecycle state of the external ASM.

        Allowed values for this property are: "CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExternalAsm.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalAsm.
        The current lifecycle state of the external ASM.


        :param lifecycle_state: The lifecycle_state of this ExternalAsm.
        :type: str
        """
        allowed_values = ["CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExternalAsm.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExternalAsm.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExternalAsm.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExternalAsm.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def serviced_databases(self):
        """
        Gets the serviced_databases of this ExternalAsm.
        The list of databases that are serviced by the ASM.


        :return: The serviced_databases of this ExternalAsm.
        :rtype: list[oci.database_management.models.ExternalAsmServicedDatabase]
        """
        return self._serviced_databases

    @serviced_databases.setter
    def serviced_databases(self, serviced_databases):
        """
        Sets the serviced_databases of this ExternalAsm.
        The list of databases that are serviced by the ASM.


        :param serviced_databases: The serviced_databases of this ExternalAsm.
        :type: list[oci.database_management.models.ExternalAsmServicedDatabase]
        """
        self._serviced_databases = serviced_databases

    @property
    def additional_details(self):
        """
        Gets the additional_details of this ExternalAsm.
        The additional details of the external ASM defined in `{\"key\": \"value\"}` format.
        Example: `{\"bar-key\": \"value\"}`


        :return: The additional_details of this ExternalAsm.
        :rtype: dict(str, str)
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this ExternalAsm.
        The additional details of the external ASM defined in `{\"key\": \"value\"}` format.
        Example: `{\"bar-key\": \"value\"}`


        :param additional_details: The additional_details of this ExternalAsm.
        :type: dict(str, str)
        """
        self._additional_details = additional_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExternalAsm.
        The date and time the external ASM was created.


        :return: The time_created of this ExternalAsm.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalAsm.
        The date and time the external ASM was created.


        :param time_created: The time_created of this ExternalAsm.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ExternalAsm.
        The date and time the external ASM was last updated.


        :return: The time_updated of this ExternalAsm.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExternalAsm.
        The date and time the external ASM was last updated.


        :param time_updated: The time_updated of this ExternalAsm.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def version(self):
        """
        Gets the version of this ExternalAsm.
        The ASM version.


        :return: The version of this ExternalAsm.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ExternalAsm.
        The ASM version.


        :param version: The version of this ExternalAsm.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other