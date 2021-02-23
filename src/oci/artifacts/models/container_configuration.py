# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerConfiguration(object):
    """
    Container configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_repository_created_on_first_push:
            The value to assign to the is_repository_created_on_first_push property of this ContainerConfiguration.
        :type is_repository_created_on_first_push: bool

        :param namespace:
            The value to assign to the namespace property of this ContainerConfiguration.
        :type namespace: str

        """
        self.swagger_types = {
            'is_repository_created_on_first_push': 'bool',
            'namespace': 'str'
        }

        self.attribute_map = {
            'is_repository_created_on_first_push': 'isRepositoryCreatedOnFirstPush',
            'namespace': 'namespace'
        }

        self._is_repository_created_on_first_push = None
        self._namespace = None

    @property
    def is_repository_created_on_first_push(self):
        """
        **[Required]** Gets the is_repository_created_on_first_push of this ContainerConfiguration.
        Whether to create a new container repository when a container is pushed to a new repository path.
        Repositories created in this way belong to the root compartment.


        :return: The is_repository_created_on_first_push of this ContainerConfiguration.
        :rtype: bool
        """
        return self._is_repository_created_on_first_push

    @is_repository_created_on_first_push.setter
    def is_repository_created_on_first_push(self, is_repository_created_on_first_push):
        """
        Sets the is_repository_created_on_first_push of this ContainerConfiguration.
        Whether to create a new container repository when a container is pushed to a new repository path.
        Repositories created in this way belong to the root compartment.


        :param is_repository_created_on_first_push: The is_repository_created_on_first_push of this ContainerConfiguration.
        :type: bool
        """
        self._is_repository_created_on_first_push = is_repository_created_on_first_push

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this ContainerConfiguration.
        The tenancy namespace used in the container repository path.


        :return: The namespace of this ContainerConfiguration.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ContainerConfiguration.
        The tenancy namespace used in the container repository path.


        :param namespace: The namespace of this ContainerConfiguration.
        :type: str
        """
        self._namespace = namespace

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
