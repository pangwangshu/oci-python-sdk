# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config import Config
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricGroup(Config):
    """
    A metric group defines a set of metrics to collect from a span. It uses a span filter to specify which spans to
    process. The set is then published to a namespace, which is a product level subdivision of metrics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricGroup object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_config.models.MetricGroup.config_type` attribute
        of this class is ``METRIC_GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MetricGroup.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this MetricGroup.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"
        :type config_type: str

        :param time_created:
            The value to assign to the time_created property of this MetricGroup.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MetricGroup.
        :type time_updated: datetime

        :param created_by:
            The value to assign to the created_by property of this MetricGroup.
        :type created_by: str

        :param updated_by:
            The value to assign to the updated_by property of this MetricGroup.
        :type updated_by: str

        :param etag:
            The value to assign to the etag property of this MetricGroup.
        :type etag: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MetricGroup.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MetricGroup.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this MetricGroup.
        :type display_name: str

        :param filter_id:
            The value to assign to the filter_id property of this MetricGroup.
        :type filter_id: str

        :param namespace:
            The value to assign to the namespace property of this MetricGroup.
        :type namespace: str

        :param dimensions:
            The value to assign to the dimensions property of this MetricGroup.
        :type dimensions: list[oci.apm_config.models.Dimension]

        :param metrics:
            The value to assign to the metrics property of this MetricGroup.
        :type metrics: list[oci.apm_config.models.Metric]

        """
        self.swagger_types = {
            'id': 'str',
            'config_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by': 'str',
            'updated_by': 'str',
            'etag': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'filter_id': 'str',
            'namespace': 'str',
            'dimensions': 'list[Dimension]',
            'metrics': 'list[Metric]'
        }

        self.attribute_map = {
            'id': 'id',
            'config_type': 'configType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by': 'createdBy',
            'updated_by': 'updatedBy',
            'etag': 'etag',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'filter_id': 'filterId',
            'namespace': 'namespace',
            'dimensions': 'dimensions',
            'metrics': 'metrics'
        }

        self._id = None
        self._config_type = None
        self._time_created = None
        self._time_updated = None
        self._created_by = None
        self._updated_by = None
        self._etag = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._filter_id = None
        self._namespace = None
        self._dimensions = None
        self._metrics = None
        self._config_type = 'METRIC_GROUP'

    @property
    def display_name(self):
        """
        Gets the display_name of this MetricGroup.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this MetricGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MetricGroup.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this MetricGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def filter_id(self):
        """
        Gets the filter_id of this MetricGroup.
        The `OCID`__ of a Span Filter. The filterId is mandatory for the creation
        of MetricGroups. A filterId is generated when a Span Filter is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The filter_id of this MetricGroup.
        :rtype: str
        """
        return self._filter_id

    @filter_id.setter
    def filter_id(self, filter_id):
        """
        Sets the filter_id of this MetricGroup.
        The `OCID`__ of a Span Filter. The filterId is mandatory for the creation
        of MetricGroups. A filterId is generated when a Span Filter is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param filter_id: The filter_id of this MetricGroup.
        :type: str
        """
        self._filter_id = filter_id

    @property
    def namespace(self):
        """
        Gets the namespace of this MetricGroup.
        The namespace to which the metrics are published. It must be one of several predefined namespaces.


        :return: The namespace of this MetricGroup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this MetricGroup.
        The namespace to which the metrics are published. It must be one of several predefined namespaces.


        :param namespace: The namespace of this MetricGroup.
        :type: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """
        Gets the dimensions of this MetricGroup.
        A list of dimensions for the metric. This variable should not be used.


        :return: The dimensions of this MetricGroup.
        :rtype: list[oci.apm_config.models.Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this MetricGroup.
        A list of dimensions for the metric. This variable should not be used.


        :param dimensions: The dimensions of this MetricGroup.
        :type: list[oci.apm_config.models.Dimension]
        """
        self._dimensions = dimensions

    @property
    def metrics(self):
        """
        Gets the metrics of this MetricGroup.
        The list of metrics in this group.


        :return: The metrics of this MetricGroup.
        :rtype: list[oci.apm_config.models.Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this MetricGroup.
        The list of metrics in this group.


        :param metrics: The metrics of this MetricGroup.
        :type: list[oci.apm_config.models.Metric]
        """
        self._metrics = metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
