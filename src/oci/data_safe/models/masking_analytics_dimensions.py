# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingAnalyticsDimensions(object):
    """
    The scope of analytics data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingAnalyticsDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_id:
            The value to assign to the target_id property of this MaskingAnalyticsDimensions.
        :type target_id: str

        :param policy_id:
            The value to assign to the policy_id property of this MaskingAnalyticsDimensions.
        :type policy_id: str

        """
        self.swagger_types = {
            'target_id': 'str',
            'policy_id': 'str'
        }

        self.attribute_map = {
            'target_id': 'targetId',
            'policy_id': 'policyId'
        }

        self._target_id = None
        self._policy_id = None

    @property
    def target_id(self):
        """
        Gets the target_id of this MaskingAnalyticsDimensions.
        The OCID of the target database.


        :return: The target_id of this MaskingAnalyticsDimensions.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this MaskingAnalyticsDimensions.
        The OCID of the target database.


        :param target_id: The target_id of this MaskingAnalyticsDimensions.
        :type: str
        """
        self._target_id = target_id

    @property
    def policy_id(self):
        """
        Gets the policy_id of this MaskingAnalyticsDimensions.
        The OCID of the masking policy..


        :return: The policy_id of this MaskingAnalyticsDimensions.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this MaskingAnalyticsDimensions.
        The OCID of the masking policy..


        :param policy_id: The policy_id of this MaskingAnalyticsDimensions.
        :type: str
        """
        self._policy_id = policy_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
