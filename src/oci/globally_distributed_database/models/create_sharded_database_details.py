# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateShardedDatabaseDetails(object):
    """
    Details required for Sharded database creation.
    """

    #: A constant which can be used with the db_deployment_type property of a CreateShardedDatabaseDetails.
    #: This constant has a value of "DEDICATED"
    DB_DEPLOYMENT_TYPE_DEDICATED = "DEDICATED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateShardedDatabaseDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.globally_distributed_database.models.CreateDedicatedShardedDatabase`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateShardedDatabaseDetails.
        :type compartment_id: str

        :param db_deployment_type:
            The value to assign to the db_deployment_type property of this CreateShardedDatabaseDetails.
            Allowed values for this property are: "DEDICATED"
        :type db_deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateShardedDatabaseDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateShardedDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateShardedDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_deployment_type': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_deployment_type': 'dbDeploymentType',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._db_deployment_type = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dbDeploymentType']

        if type == 'DEDICATED':
            return 'CreateDedicatedShardedDatabase'
        else:
            return 'CreateShardedDatabaseDetails'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateShardedDatabaseDetails.
        Identifier of the compartment where sharded database is to be created.


        :return: The compartment_id of this CreateShardedDatabaseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateShardedDatabaseDetails.
        Identifier of the compartment where sharded database is to be created.


        :param compartment_id: The compartment_id of this CreateShardedDatabaseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_deployment_type(self):
        """
        **[Required]** Gets the db_deployment_type of this CreateShardedDatabaseDetails.
        The database deployment type.

        Allowed values for this property are: "DEDICATED"


        :return: The db_deployment_type of this CreateShardedDatabaseDetails.
        :rtype: str
        """
        return self._db_deployment_type

    @db_deployment_type.setter
    def db_deployment_type(self, db_deployment_type):
        """
        Sets the db_deployment_type of this CreateShardedDatabaseDetails.
        The database deployment type.


        :param db_deployment_type: The db_deployment_type of this CreateShardedDatabaseDetails.
        :type: str
        """
        allowed_values = ["DEDICATED"]
        if not value_allowed_none_or_none_sentinel(db_deployment_type, allowed_values):
            raise ValueError(
                f"Invalid value for `db_deployment_type`, must be None or one of {allowed_values}"
            )
        self._db_deployment_type = db_deployment_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateShardedDatabaseDetails.
        Oracle sharded database display name.


        :return: The display_name of this CreateShardedDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateShardedDatabaseDetails.
        Oracle sharded database display name.


        :param display_name: The display_name of this CreateShardedDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateShardedDatabaseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateShardedDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateShardedDatabaseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateShardedDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateShardedDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateShardedDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateShardedDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateShardedDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
