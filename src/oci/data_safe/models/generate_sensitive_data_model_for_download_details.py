# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateSensitiveDataModelForDownloadDetails(object):
    """
    Details to generate a downloadable sensitive data model.
    """

    #: A constant which can be used with the data_model_format property of a GenerateSensitiveDataModelForDownloadDetails.
    #: This constant has a value of "XML"
    DATA_MODEL_FORMAT_XML = "XML"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateSensitiveDataModelForDownloadDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_model_format:
            The value to assign to the data_model_format property of this GenerateSensitiveDataModelForDownloadDetails.
            Allowed values for this property are: "XML"
        :type data_model_format: str

        """
        self.swagger_types = {
            'data_model_format': 'str'
        }

        self.attribute_map = {
            'data_model_format': 'dataModelFormat'
        }

        self._data_model_format = None

    @property
    def data_model_format(self):
        """
        Gets the data_model_format of this GenerateSensitiveDataModelForDownloadDetails.
        The format of the sensitive data model file.

        Allowed values for this property are: "XML"


        :return: The data_model_format of this GenerateSensitiveDataModelForDownloadDetails.
        :rtype: str
        """
        return self._data_model_format

    @data_model_format.setter
    def data_model_format(self, data_model_format):
        """
        Sets the data_model_format of this GenerateSensitiveDataModelForDownloadDetails.
        The format of the sensitive data model file.


        :param data_model_format: The data_model_format of this GenerateSensitiveDataModelForDownloadDetails.
        :type: str
        """
        allowed_values = ["XML"]
        if not value_allowed_none_or_none_sentinel(data_model_format, allowed_values):
            raise ValueError(
                "Invalid value for `data_model_format`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._data_model_format = data_model_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other