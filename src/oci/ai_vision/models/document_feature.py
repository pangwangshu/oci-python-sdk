# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentFeature(object):
    """
    Type of document analysis.
    """

    #: A constant which can be used with the feature_type property of a DocumentFeature.
    #: This constant has a value of "LANGUAGE_CLASSIFICATION"
    FEATURE_TYPE_LANGUAGE_CLASSIFICATION = "LANGUAGE_CLASSIFICATION"

    #: A constant which can be used with the feature_type property of a DocumentFeature.
    #: This constant has a value of "TEXT_DETECTION"
    FEATURE_TYPE_TEXT_DETECTION = "TEXT_DETECTION"

    #: A constant which can be used with the feature_type property of a DocumentFeature.
    #: This constant has a value of "TABLE_DETECTION"
    FEATURE_TYPE_TABLE_DETECTION = "TABLE_DETECTION"

    #: A constant which can be used with the feature_type property of a DocumentFeature.
    #: This constant has a value of "KEY_VALUE_DETECTION"
    FEATURE_TYPE_KEY_VALUE_DETECTION = "KEY_VALUE_DETECTION"

    #: A constant which can be used with the feature_type property of a DocumentFeature.
    #: This constant has a value of "DOCUMENT_CLASSIFICATION"
    FEATURE_TYPE_DOCUMENT_CLASSIFICATION = "DOCUMENT_CLASSIFICATION"

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentFeature object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_vision.models.DocumentTableDetectionFeature`
        * :class:`~oci.ai_vision.models.DocumentKeyValueDetectionFeature`
        * :class:`~oci.ai_vision.models.DocumentClassificationFeature`
        * :class:`~oci.ai_vision.models.DocumentTextDetectionFeature`
        * :class:`~oci.ai_vision.models.DocumentLanguageClassificationFeature`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this DocumentFeature.
            Allowed values for this property are: "LANGUAGE_CLASSIFICATION", "TEXT_DETECTION", "TABLE_DETECTION", "KEY_VALUE_DETECTION", "DOCUMENT_CLASSIFICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature_type: str

        """
        self.swagger_types = {
            'feature_type': 'str'
        }

        self.attribute_map = {
            'feature_type': 'featureType'
        }

        self._feature_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['featureType']

        if type == 'TABLE_DETECTION':
            return 'DocumentTableDetectionFeature'

        if type == 'KEY_VALUE_DETECTION':
            return 'DocumentKeyValueDetectionFeature'

        if type == 'DOCUMENT_CLASSIFICATION':
            return 'DocumentClassificationFeature'

        if type == 'TEXT_DETECTION':
            return 'DocumentTextDetectionFeature'

        if type == 'LANGUAGE_CLASSIFICATION':
            return 'DocumentLanguageClassificationFeature'
        else:
            return 'DocumentFeature'

    @property
    def feature_type(self):
        """
        **[Required]** Gets the feature_type of this DocumentFeature.
        Type of document analysis requested
        Allowed values are:
        - `LANGUAGE_CLASSIFICATION`: Detect the language.
        - `TEXT_DETECTION`: Recognize text.
        - `TABLE_DETECTION`: Detect and extract data in tables.
        - `KEY_VALUE_DETECTION`: Extract form fields.
        - `DOCUMENT_CLASSIFICATION`: Identify the type of document.

        Allowed values for this property are: "LANGUAGE_CLASSIFICATION", "TEXT_DETECTION", "TABLE_DETECTION", "KEY_VALUE_DETECTION", "DOCUMENT_CLASSIFICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The feature_type of this DocumentFeature.
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """
        Sets the feature_type of this DocumentFeature.
        Type of document analysis requested
        Allowed values are:
        - `LANGUAGE_CLASSIFICATION`: Detect the language.
        - `TEXT_DETECTION`: Recognize text.
        - `TABLE_DETECTION`: Detect and extract data in tables.
        - `KEY_VALUE_DETECTION`: Extract form fields.
        - `DOCUMENT_CLASSIFICATION`: Identify the type of document.


        :param feature_type: The feature_type of this DocumentFeature.
        :type: str
        """
        allowed_values = ["LANGUAGE_CLASSIFICATION", "TEXT_DETECTION", "TABLE_DETECTION", "KEY_VALUE_DETECTION", "DOCUMENT_CLASSIFICATION"]
        if not value_allowed_none_or_none_sentinel(feature_type, allowed_values):
            feature_type = 'UNKNOWN_ENUM_VALUE'
        self._feature_type = feature_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
