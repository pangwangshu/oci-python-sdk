# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StrategyParameter(object):
    """
    The metadata associated with the strategy parameter.
    """

    #: A constant which can be used with the type property of a StrategyParameter.
    #: This constant has a value of "STRING"
    TYPE_STRING = "STRING"

    #: A constant which can be used with the type property of a StrategyParameter.
    #: This constant has a value of "BOOLEAN"
    TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the type property of a StrategyParameter.
    #: This constant has a value of "NUMBER"
    TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the type property of a StrategyParameter.
    #: This constant has a value of "DATETIME"
    TYPE_DATETIME = "DATETIME"

    def __init__(self, **kwargs):
        """
        Initializes a new StrategyParameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this StrategyParameter.
        :type name: str

        :param type:
            The value to assign to the type property of this StrategyParameter.
            Allowed values for this property are: "STRING", "BOOLEAN", "NUMBER", "DATETIME", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param description:
            The value to assign to the description property of this StrategyParameter.
        :type description: str

        :param is_required:
            The value to assign to the is_required property of this StrategyParameter.
        :type is_required: bool

        :param default_value:
            The value to assign to the default_value property of this StrategyParameter.
        :type default_value: object

        :param possible_values:
            The value to assign to the possible_values property of this StrategyParameter.
        :type possible_values: list[object]

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'description': 'str',
            'is_required': 'bool',
            'default_value': 'object',
            'possible_values': 'list[object]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'is_required': 'isRequired',
            'default_value': 'defaultValue',
            'possible_values': 'possibleValues'
        }

        self._name = None
        self._type = None
        self._description = None
        self._is_required = None
        self._default_value = None
        self._possible_values = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this StrategyParameter.
        The name of the strategy parameter.


        :return: The name of this StrategyParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StrategyParameter.
        The name of the strategy parameter.


        :param name: The name of this StrategyParameter.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this StrategyParameter.
        The type of strategy parameter.

        Allowed values for this property are: "STRING", "BOOLEAN", "NUMBER", "DATETIME", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this StrategyParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StrategyParameter.
        The type of strategy parameter.


        :param type: The type of this StrategyParameter.
        :type: str
        """
        allowed_values = ["STRING", "BOOLEAN", "NUMBER", "DATETIME"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def description(self):
        """
        **[Required]** Gets the description of this StrategyParameter.
        Text describing the strategy parameter.


        :return: The description of this StrategyParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StrategyParameter.
        Text describing the strategy parameter.


        :param description: The description of this StrategyParameter.
        :type: str
        """
        self._description = description

    @property
    def is_required(self):
        """
        **[Required]** Gets the is_required of this StrategyParameter.
        Whether this parameter is required.


        :return: The is_required of this StrategyParameter.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this StrategyParameter.
        Whether this parameter is required.


        :param is_required: The is_required of this StrategyParameter.
        :type: bool
        """
        self._is_required = is_required

    @property
    def default_value(self):
        """
        Gets the default_value of this StrategyParameter.
        A default value used for the strategy parameter.


        :return: The default_value of this StrategyParameter.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this StrategyParameter.
        A default value used for the strategy parameter.


        :param default_value: The default_value of this StrategyParameter.
        :type: object
        """
        self._default_value = default_value

    @property
    def possible_values(self):
        """
        Gets the possible_values of this StrategyParameter.
        The list of possible values used for these strategy parameters.


        :return: The possible_values of this StrategyParameter.
        :rtype: list[object]
        """
        return self._possible_values

    @possible_values.setter
    def possible_values(self, possible_values):
        """
        Sets the possible_values of this StrategyParameter.
        The list of possible values used for these strategy parameters.


        :param possible_values: The possible_values of this StrategyParameter.
        :type: list[object]
        """
        self._possible_values = possible_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
