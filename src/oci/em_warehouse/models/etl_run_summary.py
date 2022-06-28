# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EtlRunSummary(object):
    """
    Contains summary of a run.
    """

    #: A constant which can be used with the lifecycle_state property of a EtlRunSummary.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a EtlRunSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a EtlRunSummary.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a EtlRunSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a EtlRunSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a EtlRunSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new EtlRunSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this EtlRunSummary.
        :type compartment_id: str

        :param data_read_in_bytes:
            The value to assign to the data_read_in_bytes property of this EtlRunSummary.
        :type data_read_in_bytes: int

        :param data_written:
            The value to assign to the data_written property of this EtlRunSummary.
        :type data_written: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EtlRunSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this EtlRunSummary.
        :type display_name: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EtlRunSummary.
        :type lifecycle_details: str

        :param run_duration_in_milliseconds:
            The value to assign to the run_duration_in_milliseconds property of this EtlRunSummary.
        :type run_duration_in_milliseconds: int

        :param time_created:
            The value to assign to the time_created property of this EtlRunSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EtlRunSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EtlRunSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EtlRunSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'data_read_in_bytes': 'int',
            'data_written': 'int',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'lifecycle_details': 'str',
            'run_duration_in_milliseconds': 'int',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'data_read_in_bytes': 'dataReadInBytes',
            'data_written': 'dataWritten',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'lifecycle_details': 'lifecycleDetails',
            'run_duration_in_milliseconds': 'runDurationInMilliseconds',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._data_read_in_bytes = None
        self._data_written = None
        self._lifecycle_state = None
        self._display_name = None
        self._lifecycle_details = None
        self._run_duration_in_milliseconds = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EtlRunSummary.
        Compartment Identifier


        :return: The compartment_id of this EtlRunSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EtlRunSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this EtlRunSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def data_read_in_bytes(self):
        """
        Gets the data_read_in_bytes of this EtlRunSummary.
        Data read by the dataflow run


        :return: The data_read_in_bytes of this EtlRunSummary.
        :rtype: int
        """
        return self._data_read_in_bytes

    @data_read_in_bytes.setter
    def data_read_in_bytes(self, data_read_in_bytes):
        """
        Sets the data_read_in_bytes of this EtlRunSummary.
        Data read by the dataflow run


        :param data_read_in_bytes: The data_read_in_bytes of this EtlRunSummary.
        :type: int
        """
        self._data_read_in_bytes = data_read_in_bytes

    @property
    def data_written(self):
        """
        Gets the data_written of this EtlRunSummary.
        Data written by the dataflow run


        :return: The data_written of this EtlRunSummary.
        :rtype: int
        """
        return self._data_written

    @data_written.setter
    def data_written(self, data_written):
        """
        Sets the data_written of this EtlRunSummary.
        Data written by the dataflow run


        :param data_written: The data_written of this EtlRunSummary.
        :type: int
        """
        self._data_written = data_written

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this EtlRunSummary.
        The current state of the etlRun.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EtlRunSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EtlRunSummary.
        The current state of the etlRun.


        :param lifecycle_state: The lifecycle_state of this EtlRunSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        Gets the display_name of this EtlRunSummary.
        The name of the ETLRun.


        :return: The display_name of this EtlRunSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EtlRunSummary.
        The name of the ETLRun.


        :param display_name: The display_name of this EtlRunSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this EtlRunSummary.
        Details of the lifecycle state


        :return: The lifecycle_details of this EtlRunSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this EtlRunSummary.
        Details of the lifecycle state


        :param lifecycle_details: The lifecycle_details of this EtlRunSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def run_duration_in_milliseconds(self):
        """
        Gets the run_duration_in_milliseconds of this EtlRunSummary.
        Dataflow run duration


        :return: The run_duration_in_milliseconds of this EtlRunSummary.
        :rtype: int
        """
        return self._run_duration_in_milliseconds

    @run_duration_in_milliseconds.setter
    def run_duration_in_milliseconds(self, run_duration_in_milliseconds):
        """
        Sets the run_duration_in_milliseconds of this EtlRunSummary.
        Dataflow run duration


        :param run_duration_in_milliseconds: The run_duration_in_milliseconds of this EtlRunSummary.
        :type: int
        """
        self._run_duration_in_milliseconds = run_duration_in_milliseconds

    @property
    def time_created(self):
        """
        Gets the time_created of this EtlRunSummary.
        Time when the dataflow run was created


        :return: The time_created of this EtlRunSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EtlRunSummary.
        Time when the dataflow run was created


        :param time_created: The time_created of this EtlRunSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EtlRunSummary.
        Time when the dataflow run was updated


        :return: The time_updated of this EtlRunSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EtlRunSummary.
        Time when the dataflow run was updated


        :param time_updated: The time_updated of this EtlRunSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EtlRunSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EtlRunSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EtlRunSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EtlRunSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EtlRunSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EtlRunSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EtlRunSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EtlRunSummary.
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
