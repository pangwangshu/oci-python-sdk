# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlCollectionDimensions(object):
    """
    The dimensions available for SQL collection analytics.
    """

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "COLLECTING"
    LIFECYCLE_STATE_COLLECTING = "COLLECTING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "COMPLETED"
    LIFECYCLE_STATE_COMPLETED = "COMPLETED"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionDimensions.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlCollectionDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_id:
            The value to assign to the target_id property of this SqlCollectionDimensions.
        :type target_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SqlCollectionDimensions.
            Allowed values for this property are: "CREATING", "UPDATING", "COLLECTING", "COMPLETED", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'target_id': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'target_id': 'targetId',
            'lifecycle_state': 'lifecycleState'
        }

        self._target_id = None
        self._lifecycle_state = None

    @property
    def target_id(self):
        """
        Gets the target_id of this SqlCollectionDimensions.
        The OCID of the target corresponding to the security policy deployment.


        :return: The target_id of this SqlCollectionDimensions.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this SqlCollectionDimensions.
        The OCID of the target corresponding to the security policy deployment.


        :param target_id: The target_id of this SqlCollectionDimensions.
        :type: str
        """
        self._target_id = target_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SqlCollectionDimensions.
        The current state of the SQL collection.

        Allowed values for this property are: "CREATING", "UPDATING", "COLLECTING", "COMPLETED", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SqlCollectionDimensions.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SqlCollectionDimensions.
        The current state of the SQL collection.


        :param lifecycle_state: The lifecycle_state of this SqlCollectionDimensions.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "COLLECTING", "COMPLETED", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
