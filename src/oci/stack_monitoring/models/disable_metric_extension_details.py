# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisableMetricExtensionDetails(object):
    """
    The Resource IDs for which metric extension will be disabled
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DisableMetricExtensionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_ids:
            The value to assign to the resource_ids property of this DisableMetricExtensionDetails.
        :type resource_ids: list[str]

        """
        self.swagger_types = {
            'resource_ids': 'list[str]'
        }

        self.attribute_map = {
            'resource_ids': 'resourceIds'
        }

        self._resource_ids = None

    @property
    def resource_ids(self):
        """
        **[Required]** Gets the resource_ids of this DisableMetricExtensionDetails.
        List of Resource IDs [OCIDs]. Currently supports upto 20 resources per request


        :return: The resource_ids of this DisableMetricExtensionDetails.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """
        Sets the resource_ids of this DisableMetricExtensionDetails.
        List of Resource IDs [OCIDs]. Currently supports upto 20 resources per request


        :param resource_ids: The resource_ids of this DisableMetricExtensionDetails.
        :type: list[str]
        """
        self._resource_ids = resource_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
