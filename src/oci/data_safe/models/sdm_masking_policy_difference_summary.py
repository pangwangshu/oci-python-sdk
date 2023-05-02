# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SdmMaskingPolicyDifferenceSummary(object):
    """
    Summary of a SDM masking policy difference.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SdmMaskingPolicyDifferenceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SdmMaskingPolicyDifferenceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SdmMaskingPolicyDifferenceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SdmMaskingPolicyDifferenceSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this SdmMaskingPolicyDifferenceSummary.
        :type time_created: datetime

        :param time_creation_started:
            The value to assign to the time_creation_started property of this SdmMaskingPolicyDifferenceSummary.
        :type time_creation_started: datetime

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this SdmMaskingPolicyDifferenceSummary.
        :type sensitive_data_model_id: str

        :param masking_policy_id:
            The value to assign to the masking_policy_id property of this SdmMaskingPolicyDifferenceSummary.
        :type masking_policy_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SdmMaskingPolicyDifferenceSummary.
        :type lifecycle_state: str

        :param difference_type:
            The value to assign to the difference_type property of this SdmMaskingPolicyDifferenceSummary.
        :type difference_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SdmMaskingPolicyDifferenceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SdmMaskingPolicyDifferenceSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_creation_started': 'datetime',
            'sensitive_data_model_id': 'str',
            'masking_policy_id': 'str',
            'lifecycle_state': 'str',
            'difference_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_creation_started': 'timeCreationStarted',
            'sensitive_data_model_id': 'sensitiveDataModelId',
            'masking_policy_id': 'maskingPolicyId',
            'lifecycle_state': 'lifecycleState',
            'difference_type': 'differenceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_creation_started = None
        self._sensitive_data_model_id = None
        self._masking_policy_id = None
        self._lifecycle_state = None
        self._difference_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the SDM masking policy difference.


        :return: The id of this SdmMaskingPolicyDifferenceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the SDM masking policy difference.


        :param id: The id of this SdmMaskingPolicyDifferenceSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the compartment to contain the SDM masking policy difference.


        :return: The compartment_id of this SdmMaskingPolicyDifferenceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the compartment to contain the SDM masking policy difference.


        :param compartment_id: The compartment_id of this SdmMaskingPolicyDifferenceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SdmMaskingPolicyDifferenceSummary.
        The display name of the SDM masking policy difference.


        :return: The display_name of this SdmMaskingPolicyDifferenceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SdmMaskingPolicyDifferenceSummary.
        The display name of the SDM masking policy difference.


        :param display_name: The display_name of this SdmMaskingPolicyDifferenceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SdmMaskingPolicyDifferenceSummary.
        The date and time the SDM masking policy difference was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SdmMaskingPolicyDifferenceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SdmMaskingPolicyDifferenceSummary.
        The date and time the SDM masking policy difference was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SdmMaskingPolicyDifferenceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_creation_started(self):
        """
        **[Required]** Gets the time_creation_started of this SdmMaskingPolicyDifferenceSummary.
        The date and time the SDM masking policy difference creation started, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_creation_started of this SdmMaskingPolicyDifferenceSummary.
        :rtype: datetime
        """
        return self._time_creation_started

    @time_creation_started.setter
    def time_creation_started(self, time_creation_started):
        """
        Sets the time_creation_started of this SdmMaskingPolicyDifferenceSummary.
        The date and time the SDM masking policy difference creation started, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_creation_started: The time_creation_started of this SdmMaskingPolicyDifferenceSummary.
        :type: datetime
        """
        self._time_creation_started = time_creation_started

    @property
    def sensitive_data_model_id(self):
        """
        **[Required]** Gets the sensitive_data_model_id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the sensitive data model associated with the SDM masking policy difference.


        :return: The sensitive_data_model_id of this SdmMaskingPolicyDifferenceSummary.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the sensitive data model associated with the SDM masking policy difference.


        :param sensitive_data_model_id: The sensitive_data_model_id of this SdmMaskingPolicyDifferenceSummary.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    @property
    def masking_policy_id(self):
        """
        **[Required]** Gets the masking_policy_id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the masking policy associated with the SDM masking policy difference.


        :return: The masking_policy_id of this SdmMaskingPolicyDifferenceSummary.
        :rtype: str
        """
        return self._masking_policy_id

    @masking_policy_id.setter
    def masking_policy_id(self, masking_policy_id):
        """
        Sets the masking_policy_id of this SdmMaskingPolicyDifferenceSummary.
        The OCID of the masking policy associated with the SDM masking policy difference.


        :param masking_policy_id: The masking_policy_id of this SdmMaskingPolicyDifferenceSummary.
        :type: str
        """
        self._masking_policy_id = masking_policy_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SdmMaskingPolicyDifferenceSummary.
        The current state of the SDM masking policy difference.


        :return: The lifecycle_state of this SdmMaskingPolicyDifferenceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SdmMaskingPolicyDifferenceSummary.
        The current state of the SDM masking policy difference.


        :param lifecycle_state: The lifecycle_state of this SdmMaskingPolicyDifferenceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def difference_type(self):
        """
        **[Required]** Gets the difference_type of this SdmMaskingPolicyDifferenceSummary.
        The type of difference.


        :return: The difference_type of this SdmMaskingPolicyDifferenceSummary.
        :rtype: str
        """
        return self._difference_type

    @difference_type.setter
    def difference_type(self, difference_type):
        """
        Sets the difference_type of this SdmMaskingPolicyDifferenceSummary.
        The type of difference.


        :param difference_type: The difference_type of this SdmMaskingPolicyDifferenceSummary.
        :type: str
        """
        self._difference_type = difference_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SdmMaskingPolicyDifferenceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SdmMaskingPolicyDifferenceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SdmMaskingPolicyDifferenceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SdmMaskingPolicyDifferenceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SdmMaskingPolicyDifferenceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SdmMaskingPolicyDifferenceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SdmMaskingPolicyDifferenceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SdmMaskingPolicyDifferenceSummary.
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