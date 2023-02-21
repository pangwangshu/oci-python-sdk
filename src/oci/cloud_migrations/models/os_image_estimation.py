# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OsImageEstimation(object):
    """
    Cost estimation for the OS image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OsImageEstimation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_per_hour:
            The value to assign to the total_per_hour property of this OsImageEstimation.
        :type total_per_hour: float

        :param total_per_hour_by_subscription:
            The value to assign to the total_per_hour_by_subscription property of this OsImageEstimation.
        :type total_per_hour_by_subscription: float

        """
        self.swagger_types = {
            'total_per_hour': 'float',
            'total_per_hour_by_subscription': 'float'
        }

        self.attribute_map = {
            'total_per_hour': 'totalPerHour',
            'total_per_hour_by_subscription': 'totalPerHourBySubscription'
        }

        self._total_per_hour = None
        self._total_per_hour_by_subscription = None

    @property
    def total_per_hour(self):
        """
        **[Required]** Gets the total_per_hour of this OsImageEstimation.
        Total price per hour


        :return: The total_per_hour of this OsImageEstimation.
        :rtype: float
        """
        return self._total_per_hour

    @total_per_hour.setter
    def total_per_hour(self, total_per_hour):
        """
        Sets the total_per_hour of this OsImageEstimation.
        Total price per hour


        :param total_per_hour: The total_per_hour of this OsImageEstimation.
        :type: float
        """
        self._total_per_hour = total_per_hour

    @property
    def total_per_hour_by_subscription(self):
        """
        Gets the total_per_hour_by_subscription of this OsImageEstimation.
        Total price per hour by subscription


        :return: The total_per_hour_by_subscription of this OsImageEstimation.
        :rtype: float
        """
        return self._total_per_hour_by_subscription

    @total_per_hour_by_subscription.setter
    def total_per_hour_by_subscription(self, total_per_hour_by_subscription):
        """
        Sets the total_per_hour_by_subscription of this OsImageEstimation.
        Total price per hour by subscription


        :param total_per_hour_by_subscription: The total_per_hour_by_subscription of this OsImageEstimation.
        :type: float
        """
        self._total_per_hour_by_subscription = total_per_hour_by_subscription

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other