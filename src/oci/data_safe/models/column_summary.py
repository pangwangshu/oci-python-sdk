# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ColumnSummary(object):
    """
    Details of a column in a table fetched from the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ColumnSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param column_name:
            The value to assign to the column_name property of this ColumnSummary.
        :type column_name: str

        :param data_type:
            The value to assign to the data_type property of this ColumnSummary.
        :type data_type: str

        :param length:
            The value to assign to the length property of this ColumnSummary.
        :type length: int

        :param precision:
            The value to assign to the precision property of this ColumnSummary.
        :type precision: int

        :param scale:
            The value to assign to the scale property of this ColumnSummary.
        :type scale: int

        :param character_length:
            The value to assign to the character_length property of this ColumnSummary.
        :type character_length: int

        :param table_name:
            The value to assign to the table_name property of this ColumnSummary.
        :type table_name: str

        :param schema_name:
            The value to assign to the schema_name property of this ColumnSummary.
        :type schema_name: str

        """
        self.swagger_types = {
            'column_name': 'str',
            'data_type': 'str',
            'length': 'int',
            'precision': 'int',
            'scale': 'int',
            'character_length': 'int',
            'table_name': 'str',
            'schema_name': 'str'
        }

        self.attribute_map = {
            'column_name': 'columnName',
            'data_type': 'dataType',
            'length': 'length',
            'precision': 'precision',
            'scale': 'scale',
            'character_length': 'characterLength',
            'table_name': 'tableName',
            'schema_name': 'schemaName'
        }

        self._column_name = None
        self._data_type = None
        self._length = None
        self._precision = None
        self._scale = None
        self._character_length = None
        self._table_name = None
        self._schema_name = None

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this ColumnSummary.
        Name of the column.


        :return: The column_name of this ColumnSummary.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this ColumnSummary.
        Name of the column.


        :param column_name: The column_name of this ColumnSummary.
        :type: str
        """
        self._column_name = column_name

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this ColumnSummary.
        Data type of the column.


        :return: The data_type of this ColumnSummary.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this ColumnSummary.
        Data type of the column.


        :param data_type: The data_type of this ColumnSummary.
        :type: str
        """
        self._data_type = data_type

    @property
    def length(self):
        """
        **[Required]** Gets the length of this ColumnSummary.
        Length of the data represented by the column.


        :return: The length of this ColumnSummary.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this ColumnSummary.
        Length of the data represented by the column.


        :param length: The length of this ColumnSummary.
        :type: int
        """
        self._length = length

    @property
    def precision(self):
        """
        Gets the precision of this ColumnSummary.
        Precision of the column.


        :return: The precision of this ColumnSummary.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this ColumnSummary.
        Precision of the column.


        :param precision: The precision of this ColumnSummary.
        :type: int
        """
        self._precision = precision

    @property
    def scale(self):
        """
        Gets the scale of this ColumnSummary.
        Scale of the column.


        :return: The scale of this ColumnSummary.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this ColumnSummary.
        Scale of the column.


        :param scale: The scale of this ColumnSummary.
        :type: int
        """
        self._scale = scale

    @property
    def character_length(self):
        """
        Gets the character_length of this ColumnSummary.
        Character length.


        :return: The character_length of this ColumnSummary.
        :rtype: int
        """
        return self._character_length

    @character_length.setter
    def character_length(self, character_length):
        """
        Sets the character_length of this ColumnSummary.
        Character length.


        :param character_length: The character_length of this ColumnSummary.
        :type: int
        """
        self._character_length = character_length

    @property
    def table_name(self):
        """
        **[Required]** Gets the table_name of this ColumnSummary.
        Name of the table.


        :return: The table_name of this ColumnSummary.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this ColumnSummary.
        Name of the table.


        :param table_name: The table_name of this ColumnSummary.
        :type: str
        """
        self._table_name = table_name

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this ColumnSummary.
        Name of the schema.


        :return: The schema_name of this ColumnSummary.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this ColumnSummary.
        Name of the schema.


        :param schema_name: The schema_name of this ColumnSummary.
        :type: str
        """
        self._schema_name = schema_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
