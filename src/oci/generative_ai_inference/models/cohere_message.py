# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereMessage(object):
    """
    A message that represents a single chat dialog.
    """

    #: A constant which can be used with the role property of a CohereMessage.
    #: This constant has a value of "CHATBOT"
    ROLE_CHATBOT = "CHATBOT"

    #: A constant which can be used with the role property of a CohereMessage.
    #: This constant has a value of "USER"
    ROLE_USER = "USER"

    #: A constant which can be used with the role property of a CohereMessage.
    #: This constant has a value of "SYSTEM"
    ROLE_SYSTEM = "SYSTEM"

    #: A constant which can be used with the role property of a CohereMessage.
    #: This constant has a value of "TOOL"
    ROLE_TOOL = "TOOL"

    def __init__(self, **kwargs):
        """
        Initializes a new CohereMessage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_inference.models.CohereChatBotMessage`
        * :class:`~oci.generative_ai_inference.models.CohereSystemMessage`
        * :class:`~oci.generative_ai_inference.models.CohereToolMessage`
        * :class:`~oci.generative_ai_inference.models.CohereUserMessage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this CohereMessage.
            Allowed values for this property are: "CHATBOT", "USER", "SYSTEM", "TOOL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        """
        self.swagger_types = {
            'role': 'str'
        }

        self.attribute_map = {
            'role': 'role'
        }

        self._role = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['role']

        if type == 'CHATBOT':
            return 'CohereChatBotMessage'

        if type == 'SYSTEM':
            return 'CohereSystemMessage'

        if type == 'TOOL':
            return 'CohereToolMessage'

        if type == 'USER':
            return 'CohereUserMessage'
        else:
            return 'CohereMessage'

    @property
    def role(self):
        """
        **[Required]** Gets the role of this CohereMessage.
        To identify who the message is coming from, a role is associated to each message.

        Allowed values for this property are: "CHATBOT", "USER", "SYSTEM", "TOOL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this CohereMessage.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this CohereMessage.
        To identify who the message is coming from, a role is associated to each message.


        :param role: The role of this CohereMessage.
        :type: str
        """
        allowed_values = ["CHATBOT", "USER", "SYSTEM", "TOOL"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other