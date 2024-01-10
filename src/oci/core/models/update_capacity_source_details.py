# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCapacitySourceDetails(object):
    """
    A capacity source of bare metal hosts.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCapacitySourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.UpdateDedicatedCapacitySourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity_type:
            The value to assign to the capacity_type property of this UpdateCapacitySourceDetails.
        :type capacity_type: str

        """
        self.swagger_types = {
            'capacity_type': 'str'
        }

        self.attribute_map = {
            'capacity_type': 'capacityType'
        }

        self._capacity_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['capacityType']

        if type == 'DEDICATED':
            return 'UpdateDedicatedCapacitySourceDetails'
        else:
            return 'UpdateCapacitySourceDetails'

    @property
    def capacity_type(self):
        """
        **[Required]** Gets the capacity_type of this UpdateCapacitySourceDetails.
        The capacity type of bare metal hosts.


        :return: The capacity_type of this UpdateCapacitySourceDetails.
        :rtype: str
        """
        return self._capacity_type

    @capacity_type.setter
    def capacity_type(self, capacity_type):
        """
        Sets the capacity_type of this UpdateCapacitySourceDetails.
        The capacity type of bare metal hosts.


        :param capacity_type: The capacity_type of this UpdateCapacitySourceDetails.
        :type: str
        """
        self._capacity_type = capacity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other