# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertSummary(object):
    """
    Summary of a Data Safe Alert.
    """

    #: A constant which can be used with the status property of a AlertSummary.
    #: This constant has a value of "OPEN"
    STATUS_OPEN = "OPEN"

    #: A constant which can be used with the status property of a AlertSummary.
    #: This constant has a value of "CLOSED"
    STATUS_CLOSED = "CLOSED"

    #: A constant which can be used with the severity property of a AlertSummary.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a AlertSummary.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a AlertSummary.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a AlertSummary.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    #: A constant which can be used with the severity property of a AlertSummary.
    #: This constant has a value of "EVALUATE"
    SEVERITY_EVALUATE = "EVALUATE"

    #: A constant which can be used with the operation_status property of a AlertSummary.
    #: This constant has a value of "SUCCEEDED"
    OPERATION_STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the operation_status property of a AlertSummary.
    #: This constant has a value of "FAILED"
    OPERATION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the alert_type property of a AlertSummary.
    #: This constant has a value of "AUDITING"
    ALERT_TYPE_AUDITING = "AUDITING"

    #: A constant which can be used with the alert_type property of a AlertSummary.
    #: This constant has a value of "SECURITY_ASSESSMENT"
    ALERT_TYPE_SECURITY_ASSESSMENT = "SECURITY_ASSESSMENT"

    #: A constant which can be used with the alert_type property of a AlertSummary.
    #: This constant has a value of "USER_ASSESSMENT"
    ALERT_TYPE_USER_ASSESSMENT = "USER_ASSESSMENT"

    #: A constant which can be used with the lifecycle_state property of a AlertSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AlertSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a AlertSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AlertSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AlertSummary.
        :type id: str

        :param status:
            The value to assign to the status property of this AlertSummary.
            Allowed values for this property are: "OPEN", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param display_name:
            The value to assign to the display_name property of this AlertSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AlertSummary.
        :type description: str

        :param severity:
            The value to assign to the severity property of this AlertSummary.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param operation_time:
            The value to assign to the operation_time property of this AlertSummary.
        :type operation_time: datetime

        :param operation:
            The value to assign to the operation property of this AlertSummary.
        :type operation: str

        :param operation_status:
            The value to assign to the operation_status property of this AlertSummary.
            Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_status: str

        :param target_ids:
            The value to assign to the target_ids property of this AlertSummary.
        :type target_ids: list[str]

        :param target_names:
            The value to assign to the target_names property of this AlertSummary.
        :type target_names: list[str]

        :param policy_id:
            The value to assign to the policy_id property of this AlertSummary.
        :type policy_id: str

        :param alert_type:
            The value to assign to the alert_type property of this AlertSummary.
            Allowed values for this property are: "AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type alert_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AlertSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this AlertSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AlertSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AlertSummary.
            Allowed values for this property are: "UPDATING", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param feature_details:
            The value to assign to the feature_details property of this AlertSummary.
        :type feature_details: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AlertSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AlertSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'display_name': 'str',
            'description': 'str',
            'severity': 'str',
            'operation_time': 'datetime',
            'operation': 'str',
            'operation_status': 'str',
            'target_ids': 'list[str]',
            'target_names': 'list[str]',
            'policy_id': 'str',
            'alert_type': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'feature_details': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'display_name': 'displayName',
            'description': 'description',
            'severity': 'severity',
            'operation_time': 'operationTime',
            'operation': 'operation',
            'operation_status': 'operationStatus',
            'target_ids': 'targetIds',
            'target_names': 'targetNames',
            'policy_id': 'policyId',
            'alert_type': 'alertType',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'feature_details': 'featureDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._status = None
        self._display_name = None
        self._description = None
        self._severity = None
        self._operation_time = None
        self._operation = None
        self._operation_status = None
        self._target_ids = None
        self._target_names = None
        self._policy_id = None
        self._alert_type = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._feature_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AlertSummary.
        The OCID of the alert.


        :return: The id of this AlertSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AlertSummary.
        The OCID of the alert.


        :param id: The id of this AlertSummary.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AlertSummary.
        The status of the alert.

        Allowed values for this property are: "OPEN", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AlertSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AlertSummary.
        The status of the alert.


        :param status: The status of this AlertSummary.
        :type: str
        """
        allowed_values = ["OPEN", "CLOSED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AlertSummary.
        The display name of the alert.


        :return: The display_name of this AlertSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AlertSummary.
        The display name of the alert.


        :param display_name: The display_name of this AlertSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this AlertSummary.
        The details of the alert.


        :return: The description of this AlertSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AlertSummary.
        The details of the alert.


        :param description: The description of this AlertSummary.
        :type: str
        """
        self._description = description

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this AlertSummary.
        Severity level of the alert.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this AlertSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this AlertSummary.
        Severity level of the alert.


        :param severity: The severity of this AlertSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def operation_time(self):
        """
        Gets the operation_time of this AlertSummary.
        Creation date and time of the operation that triggered alert, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The operation_time of this AlertSummary.
        :rtype: datetime
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        """
        Sets the operation_time of this AlertSummary.
        Creation date and time of the operation that triggered alert, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param operation_time: The operation_time of this AlertSummary.
        :type: datetime
        """
        self._operation_time = operation_time

    @property
    def operation(self):
        """
        Gets the operation of this AlertSummary.
        The operation that triggered alert.


        :return: The operation of this AlertSummary.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this AlertSummary.
        The operation that triggered alert.


        :param operation: The operation of this AlertSummary.
        :type: str
        """
        self._operation = operation

    @property
    def operation_status(self):
        """
        Gets the operation_status of this AlertSummary.
        The result of the operation (event) that triggered alert.

        Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_status of this AlertSummary.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """
        Sets the operation_status of this AlertSummary.
        The result of the operation (event) that triggered alert.


        :param operation_status: The operation_status of this AlertSummary.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(operation_status, allowed_values):
            operation_status = 'UNKNOWN_ENUM_VALUE'
        self._operation_status = operation_status

    @property
    def target_ids(self):
        """
        Gets the target_ids of this AlertSummary.
        Array of OCIDs of the target database.


        :return: The target_ids of this AlertSummary.
        :rtype: list[str]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        """
        Sets the target_ids of this AlertSummary.
        Array of OCIDs of the target database.


        :param target_ids: The target_ids of this AlertSummary.
        :type: list[str]
        """
        self._target_ids = target_ids

    @property
    def target_names(self):
        """
        Gets the target_names of this AlertSummary.
        Array of names of the target database.


        :return: The target_names of this AlertSummary.
        :rtype: list[str]
        """
        return self._target_names

    @target_names.setter
    def target_names(self, target_names):
        """
        Sets the target_names of this AlertSummary.
        Array of names of the target database.


        :param target_names: The target_names of this AlertSummary.
        :type: list[str]
        """
        self._target_names = target_names

    @property
    def policy_id(self):
        """
        Gets the policy_id of this AlertSummary.
        The OCID of the policy that triggered alert.


        :return: The policy_id of this AlertSummary.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this AlertSummary.
        The OCID of the policy that triggered alert.


        :param policy_id: The policy_id of this AlertSummary.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def alert_type(self):
        """
        Gets the alert_type of this AlertSummary.
        Type of the alert. Indicates the Data Safe feature triggering the alert.

        Allowed values for this property are: "AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The alert_type of this AlertSummary.
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """
        Sets the alert_type of this AlertSummary.
        Type of the alert. Indicates the Data Safe feature triggering the alert.


        :param alert_type: The alert_type of this AlertSummary.
        :type: str
        """
        allowed_values = ["AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT"]
        if not value_allowed_none_or_none_sentinel(alert_type, allowed_values):
            alert_type = 'UNKNOWN_ENUM_VALUE'
        self._alert_type = alert_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AlertSummary.
        The OCID of the compartment that contains the alert.


        :return: The compartment_id of this AlertSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AlertSummary.
        The OCID of the compartment that contains the alert.


        :param compartment_id: The compartment_id of this AlertSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AlertSummary.
        Creation date and time of the alert, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AlertSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AlertSummary.
        Creation date and time of the alert, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AlertSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AlertSummary.
        Last date and time the alert was updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this AlertSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AlertSummary.
        Last date and time the alert was updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this AlertSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AlertSummary.
        The current state of the alert.

        Allowed values for this property are: "UPDATING", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AlertSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AlertSummary.
        The current state of the alert.


        :param lifecycle_state: The lifecycle_state of this AlertSummary.
        :type: str
        """
        allowed_values = ["UPDATING", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def feature_details(self):
        """
        Gets the feature_details of this AlertSummary.
        Map that contains maps of values.
         Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The feature_details of this AlertSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._feature_details

    @feature_details.setter
    def feature_details(self, feature_details):
        """
        Sets the feature_details of this AlertSummary.
        Map that contains maps of values.
         Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param feature_details: The feature_details of this AlertSummary.
        :type: dict(str, dict(str, object))
        """
        self._feature_details = feature_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AlertSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AlertSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AlertSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AlertSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AlertSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AlertSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AlertSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AlertSummary.
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
