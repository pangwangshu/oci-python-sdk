# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GatewaySummary(object):
    """
    A summary of the gateway.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GatewaySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GatewaySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this GatewaySummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GatewaySummary.
        :type compartment_id: str

        :param endpoint_type:
            The value to assign to the endpoint_type property of this GatewaySummary.
        :type endpoint_type: str

        :param subnet_id:
            The value to assign to the subnet_id property of this GatewaySummary.
        :type subnet_id: str

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this GatewaySummary.
        :type network_security_group_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this GatewaySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this GatewaySummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GatewaySummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this GatewaySummary.
        :type lifecycle_details: str

        :param hostname:
            The value to assign to the hostname property of this GatewaySummary.
        :type hostname: str

        :param certificate_id:
            The value to assign to the certificate_id property of this GatewaySummary.
        :type certificate_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GatewaySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GatewaySummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'endpoint_type': 'str',
            'subnet_id': 'str',
            'network_security_group_ids': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'hostname': 'str',
            'certificate_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'endpoint_type': 'endpointType',
            'subnet_id': 'subnetId',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'hostname': 'hostname',
            'certificate_id': 'certificateId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._endpoint_type = None
        self._subnet_id = None
        self._network_security_group_ids = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._hostname = None
        self._certificate_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this GatewaySummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this GatewaySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GatewaySummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this GatewaySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this GatewaySummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this GatewaySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this GatewaySummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this GatewaySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this GatewaySummary.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this GatewaySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this GatewaySummary.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this GatewaySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def endpoint_type(self):
        """
        **[Required]** Gets the endpoint_type of this GatewaySummary.
        Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be
        accessible on a private IP address on the subnet.

        Example: `PUBLIC` or `PRIVATE`


        :return: The endpoint_type of this GatewaySummary.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this GatewaySummary.
        Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be
        accessible on a private IP address on the subnet.

        Example: `PUBLIC` or `PRIVATE`


        :param endpoint_type: The endpoint_type of this GatewaySummary.
        :type: str
        """
        self._endpoint_type = endpoint_type

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this GatewaySummary.
        The `OCID`__ of the subnet in which
        related resources are created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this GatewaySummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this GatewaySummary.
        The `OCID`__ of the subnet in which
        related resources are created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this GatewaySummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this GatewaySummary.
        An array of Network Security Groups OCIDs associated with this API Gateway.


        :return: The network_security_group_ids of this GatewaySummary.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this GatewaySummary.
        An array of Network Security Groups OCIDs associated with this API Gateway.


        :param network_security_group_ids: The network_security_group_ids of this GatewaySummary.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def time_created(self):
        """
        Gets the time_created of this GatewaySummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this GatewaySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this GatewaySummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this GatewaySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this GatewaySummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this GatewaySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this GatewaySummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this GatewaySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this GatewaySummary.
        The current state of the gateway.


        :return: The lifecycle_state of this GatewaySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this GatewaySummary.
        The current state of the gateway.


        :param lifecycle_state: The lifecycle_state of this GatewaySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this GatewaySummary.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :return: The lifecycle_details of this GatewaySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this GatewaySummary.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this GatewaySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def hostname(self):
        """
        Gets the hostname of this GatewaySummary.
        The hostname for the APIs deployed on the gateway.


        :return: The hostname of this GatewaySummary.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this GatewaySummary.
        The hostname for the APIs deployed on the gateway.


        :param hostname: The hostname of this GatewaySummary.
        :type: str
        """
        self._hostname = hostname

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this GatewaySummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The certificate_id of this GatewaySummary.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this GatewaySummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param certificate_id: The certificate_id of this GatewaySummary.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this GatewaySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this GatewaySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this GatewaySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this GatewaySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this GatewaySummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this GatewaySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this GatewaySummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this GatewaySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
