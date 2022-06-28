# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtocolParameters(object):
    """
    Defines the IP protocol parameters for a `PathAnalyzerTest` resource.
    """

    #: A constant which can be used with the type property of a ProtocolParameters.
    #: This constant has a value of "TCP"
    TYPE_TCP = "TCP"

    #: A constant which can be used with the type property of a ProtocolParameters.
    #: This constant has a value of "UDP"
    TYPE_UDP = "UDP"

    #: A constant which can be used with the type property of a ProtocolParameters.
    #: This constant has a value of "ICMP"
    TYPE_ICMP = "ICMP"

    def __init__(self, **kwargs):
        """
        Initializes a new ProtocolParameters object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.UdpProtocolParameters`
        * :class:`~oci.vn_monitoring.models.TcpProtocolParameters`
        * :class:`~oci.vn_monitoring.models.IcmpProtocolParameters`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ProtocolParameters.
            Allowed values for this property are: "TCP", "UDP", "ICMP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'UDP':
            return 'UdpProtocolParameters'

        if type == 'TCP':
            return 'TcpProtocolParameters'

        if type == 'ICMP':
            return 'IcmpProtocolParameters'
        else:
            return 'ProtocolParameters'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ProtocolParameters.
        The type of the `ProtocolParameters` object.

        Allowed values for this property are: "TCP", "UDP", "ICMP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ProtocolParameters.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProtocolParameters.
        The type of the `ProtocolParameters` object.


        :param type: The type of this ProtocolParameters.
        :type: str
        """
        allowed_values = ["TCP", "UDP", "ICMP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
