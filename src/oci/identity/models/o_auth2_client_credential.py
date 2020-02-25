# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OAuth2ClientCredential(object):
    """
    User can define Oauth clients in IAM, then use it to generate a token to grant access to app resources.
    """

    #: A constant which can be used with the lifecycle_state property of a OAuth2ClientCredential.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OAuth2ClientCredential.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OAuth2ClientCredential.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OAuth2ClientCredential.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OAuth2ClientCredential.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new OAuth2ClientCredential object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scopes:
            The value to assign to the scopes property of this OAuth2ClientCredential.
        :type scopes: list[FullyQualifiedScope]

        :param password:
            The value to assign to the password property of this OAuth2ClientCredential.
        :type password: str

        :param user_id:
            The value to assign to the user_id property of this OAuth2ClientCredential.
        :type user_id: str

        :param expires_on:
            The value to assign to the expires_on property of this OAuth2ClientCredential.
        :type expires_on: datetime

        :param id:
            The value to assign to the id property of this OAuth2ClientCredential.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OAuth2ClientCredential.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this OAuth2ClientCredential.
        :type name: str

        :param description:
            The value to assign to the description property of this OAuth2ClientCredential.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OAuth2ClientCredential.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this OAuth2ClientCredential.
        :type time_created: datetime

        """
        self.swagger_types = {
            'scopes': 'list[FullyQualifiedScope]',
            'password': 'str',
            'user_id': 'str',
            'expires_on': 'datetime',
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'scopes': 'scopes',
            'password': 'password',
            'user_id': 'userId',
            'expires_on': 'expiresOn',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._scopes = None
        self._password = None
        self._user_id = None
        self._expires_on = None
        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def scopes(self):
        """
        Gets the scopes of this OAuth2ClientCredential.
        Allowed scopes for the given oauth credential.


        :return: The scopes of this OAuth2ClientCredential.
        :rtype: list[FullyQualifiedScope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this OAuth2ClientCredential.
        Allowed scopes for the given oauth credential.


        :param scopes: The scopes of this OAuth2ClientCredential.
        :type: list[FullyQualifiedScope]
        """
        self._scopes = scopes

    @property
    def password(self):
        """
        Gets the password of this OAuth2ClientCredential.
        Returned during create and update with password reset requests.


        :return: The password of this OAuth2ClientCredential.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this OAuth2ClientCredential.
        Returned during create and update with password reset requests.


        :param password: The password of this OAuth2ClientCredential.
        :type: str
        """
        self._password = password

    @property
    def user_id(self):
        """
        Gets the user_id of this OAuth2ClientCredential.
        The OCID of the user the Oauth credential belongs to.


        :return: The user_id of this OAuth2ClientCredential.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this OAuth2ClientCredential.
        The OCID of the user the Oauth credential belongs to.


        :param user_id: The user_id of this OAuth2ClientCredential.
        :type: str
        """
        self._user_id = user_id

    @property
    def expires_on(self):
        """
        Gets the expires_on of this OAuth2ClientCredential.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The expires_on of this OAuth2ClientCredential.
        :rtype: datetime
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """
        Sets the expires_on of this OAuth2ClientCredential.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param expires_on: The expires_on of this OAuth2ClientCredential.
        :type: datetime
        """
        self._expires_on = expires_on

    @property
    def id(self):
        """
        Gets the id of this OAuth2ClientCredential.
        The OCID of the Oauth credential.


        :return: The id of this OAuth2ClientCredential.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OAuth2ClientCredential.
        The OCID of the Oauth credential.


        :param id: The id of this OAuth2ClientCredential.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this OAuth2ClientCredential.
        The OCID of the compartment containing the Oauth credential.


        :return: The compartment_id of this OAuth2ClientCredential.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OAuth2ClientCredential.
        The OCID of the compartment containing the Oauth credential.


        :param compartment_id: The compartment_id of this OAuth2ClientCredential.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this OAuth2ClientCredential.
        The name of the Oauth credential.


        :return: The name of this OAuth2ClientCredential.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OAuth2ClientCredential.
        The name of the Oauth credential.


        :param name: The name of this OAuth2ClientCredential.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this OAuth2ClientCredential.
        The description of the Oauth credential.


        :return: The description of this OAuth2ClientCredential.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OAuth2ClientCredential.
        The description of the Oauth credential.


        :param description: The description of this OAuth2ClientCredential.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OAuth2ClientCredential.
        The credential's current state. After creating a Oauth credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OAuth2ClientCredential.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OAuth2ClientCredential.
        The credential's current state. After creating a Oauth credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this OAuth2ClientCredential.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this OAuth2ClientCredential.
        Date and time the `OAuth2ClientCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this OAuth2ClientCredential.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OAuth2ClientCredential.
        Date and time the `OAuth2ClientCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this OAuth2ClientCredential.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
