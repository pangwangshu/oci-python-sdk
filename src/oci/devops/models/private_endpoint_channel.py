# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .network_channel import NetworkChannel
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpointChannel(NetworkChannel):
    """
    Specifies the configuration to access private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpointChannel object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.PrivateEndpointChannel.network_channel_type` attribute
        of this class is ``PRIVATE_ENDPOINT_CHANNEL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_channel_type:
            The value to assign to the network_channel_type property of this PrivateEndpointChannel.
            Allowed values for this property are: "PRIVATE_ENDPOINT_CHANNEL"
        :type network_channel_type: str

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateEndpointChannel.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this PrivateEndpointChannel.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'network_channel_type': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'network_channel_type': 'networkChannelType',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds'
        }

        self._network_channel_type = None
        self._subnet_id = None
        self._nsg_ids = None
        self._network_channel_type = 'PRIVATE_ENDPOINT_CHANNEL'

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this PrivateEndpointChannel.
        The OCID of the subnet where Virtual Network Interface Cards (VNIC) resources are created for private endpoint access.


        :return: The subnet_id of this PrivateEndpointChannel.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateEndpointChannel.
        The OCID of the subnet where Virtual Network Interface Cards (VNIC) resources are created for private endpoint access.


        :param subnet_id: The subnet_id of this PrivateEndpointChannel.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this PrivateEndpointChannel.
        An array of network security group OCIDs.


        :return: The nsg_ids of this PrivateEndpointChannel.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this PrivateEndpointChannel.
        An array of network security group OCIDs.


        :param nsg_ids: The nsg_ids of this PrivateEndpointChannel.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
