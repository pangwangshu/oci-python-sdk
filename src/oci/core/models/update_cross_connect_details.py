# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCrossConnectDetails(object):
    """
    Update a CrossConnect
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCrossConnectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateCrossConnectDetails.
        :type display_name: str

        :param is_active:
            The value to assign to the is_active property of this UpdateCrossConnectDetails.
        :type is_active: bool

        :param customer_reference_name:
            The value to assign to the customer_reference_name property of this UpdateCrossConnectDetails.
        :type customer_reference_name: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_active': 'bool',
            'customer_reference_name': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_active': 'isActive',
            'customer_reference_name': 'customerReferenceName'
        }

        self._display_name = None
        self._is_active = None
        self._customer_reference_name = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateCrossConnectDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateCrossConnectDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_active(self):
        """
        Gets the is_active of this UpdateCrossConnectDetails.
        Set to true to activate the cross-connect. You activate it after the physical cabling
        is complete, and you've confirmed the cross-connect's light levels are good and your side
        of the interface is up. Activation indicates to Oracle that the physical connection is ready.

        Example: `true`


        :return: The is_active of this UpdateCrossConnectDetails.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this UpdateCrossConnectDetails.
        Set to true to activate the cross-connect. You activate it after the physical cabling
        is complete, and you've confirmed the cross-connect's light levels are good and your side
        of the interface is up. Activation indicates to Oracle that the physical connection is ready.

        Example: `true`


        :param is_active: The is_active of this UpdateCrossConnectDetails.
        :type: bool
        """
        self._is_active = is_active

    @property
    def customer_reference_name(self):
        """
        Gets the customer_reference_name of this UpdateCrossConnectDetails.
        A reference name or identifier for the physical fiber connection that this cross-connect
        uses.


        :return: The customer_reference_name of this UpdateCrossConnectDetails.
        :rtype: str
        """
        return self._customer_reference_name

    @customer_reference_name.setter
    def customer_reference_name(self, customer_reference_name):
        """
        Sets the customer_reference_name of this UpdateCrossConnectDetails.
        A reference name or identifier for the physical fiber connection that this cross-connect
        uses.


        :param customer_reference_name: The customer_reference_name of this UpdateCrossConnectDetails.
        :type: str
        """
        self._customer_reference_name = customer_reference_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
