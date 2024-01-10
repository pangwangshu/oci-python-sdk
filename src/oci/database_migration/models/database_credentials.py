# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210929


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseCredentials(object):
    """
    Database Credentials details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseCredentials object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param username:
            The value to assign to the username property of this DatabaseCredentials.
        :type username: str

        :param password:
            The value to assign to the password property of this DatabaseCredentials.
        :type password: str

        """
        self.swagger_types = {
            'username': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password'
        }

        self._username = None
        self._password = None

    @property
    def username(self):
        """
        **[Required]** Gets the username of this DatabaseCredentials.
        Database username


        :return: The username of this DatabaseCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DatabaseCredentials.
        Database username


        :param username: The username of this DatabaseCredentials.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this DatabaseCredentials.
        Database  password


        :return: The password of this DatabaseCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this DatabaseCredentials.
        Database  password


        :param password: The password of this DatabaseCredentials.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other