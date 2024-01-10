# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFsuActionDetails(object):
    """
    Exadata Fleet Update Action resource details to update.
    """

    #: A constant which can be used with the type property of a UpdateFsuActionDetails.
    #: This constant has a value of "STAGE"
    TYPE_STAGE = "STAGE"

    #: A constant which can be used with the type property of a UpdateFsuActionDetails.
    #: This constant has a value of "PRECHECK"
    TYPE_PRECHECK = "PRECHECK"

    #: A constant which can be used with the type property of a UpdateFsuActionDetails.
    #: This constant has a value of "APPLY"
    TYPE_APPLY = "APPLY"

    #: A constant which can be used with the type property of a UpdateFsuActionDetails.
    #: This constant has a value of "ROLLBACK_AND_REMOVE_TARGET"
    TYPE_ROLLBACK_AND_REMOVE_TARGET = "ROLLBACK_AND_REMOVE_TARGET"

    #: A constant which can be used with the type property of a UpdateFsuActionDetails.
    #: This constant has a value of "CLEANUP"
    TYPE_CLEANUP = "CLEANUP"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFsuActionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.UpdateStageActionDetails`
        * :class:`~oci.fleet_software_update.models.UpdateApplyActionDetails`
        * :class:`~oci.fleet_software_update.models.UpdateRollbackActionDetails`
        * :class:`~oci.fleet_software_update.models.UpdatePrecheckActionDetails`
        * :class:`~oci.fleet_software_update.models.UpdateCleanupActionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateFsuActionDetails.
            Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateFsuActionDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateFsuActionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateFsuActionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._type = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'STAGE':
            return 'UpdateStageActionDetails'

        if type == 'APPLY':
            return 'UpdateApplyActionDetails'

        if type == 'ROLLBACK_AND_REMOVE_TARGET':
            return 'UpdateRollbackActionDetails'

        if type == 'PRECHECK':
            return 'UpdatePrecheckActionDetails'

        if type == 'CLEANUP':
            return 'UpdateCleanupActionDetails'
        else:
            return 'UpdateFsuActionDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this UpdateFsuActionDetails.
        Type of Exadata Fleet Update Action to update.
        Specifying this option will not change the Action type.

        Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"


        :return: The type of this UpdateFsuActionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateFsuActionDetails.
        Type of Exadata Fleet Update Action to update.
        Specifying this option will not change the Action type.


        :param type: The type of this UpdateFsuActionDetails.
        :type: str
        """
        allowed_values = ["STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateFsuActionDetails.
        Exadata Fleet Update Action display name.


        :return: The display_name of this UpdateFsuActionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateFsuActionDetails.
        Exadata Fleet Update Action display name.


        :param display_name: The display_name of this UpdateFsuActionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateFsuActionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateFsuActionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateFsuActionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateFsuActionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateFsuActionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateFsuActionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateFsuActionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateFsuActionDetails.
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