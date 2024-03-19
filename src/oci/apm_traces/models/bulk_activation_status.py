# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkActivationStatus(object):
    """
    Response of a bulk attribute activation operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkActivationStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_statuses:
            The value to assign to the attribute_statuses property of this BulkActivationStatus.
        :type attribute_statuses: list[oci.apm_traces.models.AttributeResponse]

        :param bulk_activation_metadata:
            The value to assign to the bulk_activation_metadata property of this BulkActivationStatus.
        :type bulk_activation_metadata: oci.apm_traces.models.BulkActivationMetadata

        """
        self.swagger_types = {
            'attribute_statuses': 'list[AttributeResponse]',
            'bulk_activation_metadata': 'BulkActivationMetadata'
        }

        self.attribute_map = {
            'attribute_statuses': 'attributeStatuses',
            'bulk_activation_metadata': 'bulkActivationMetadata'
        }

        self._attribute_statuses = None
        self._bulk_activation_metadata = None

    @property
    def attribute_statuses(self):
        """
        **[Required]** Gets the attribute_statuses of this BulkActivationStatus.
        We preserve the order of the attribute items from the bulk activation request in this collection.  The ith object in this collection represents the
        bulk activation operation status of the ith object in the BulkActivateAttributeDetails object from the Bulk Activation request.  If the
        bulk activation operation results in a processing error or a validation error, the operationStatus property in the  BulkActivationMetadata object will
        contain the appropriate bulk error status for the bulk operation.


        :return: The attribute_statuses of this BulkActivationStatus.
        :rtype: list[oci.apm_traces.models.AttributeResponse]
        """
        return self._attribute_statuses

    @attribute_statuses.setter
    def attribute_statuses(self, attribute_statuses):
        """
        Sets the attribute_statuses of this BulkActivationStatus.
        We preserve the order of the attribute items from the bulk activation request in this collection.  The ith object in this collection represents the
        bulk activation operation status of the ith object in the BulkActivateAttributeDetails object from the Bulk Activation request.  If the
        bulk activation operation results in a processing error or a validation error, the operationStatus property in the  BulkActivationMetadata object will
        contain the appropriate bulk error status for the bulk operation.


        :param attribute_statuses: The attribute_statuses of this BulkActivationStatus.
        :type: list[oci.apm_traces.models.AttributeResponse]
        """
        self._attribute_statuses = attribute_statuses

    @property
    def bulk_activation_metadata(self):
        """
        **[Required]** Gets the bulk_activation_metadata of this BulkActivationStatus.

        :return: The bulk_activation_metadata of this BulkActivationStatus.
        :rtype: oci.apm_traces.models.BulkActivationMetadata
        """
        return self._bulk_activation_metadata

    @bulk_activation_metadata.setter
    def bulk_activation_metadata(self, bulk_activation_metadata):
        """
        Sets the bulk_activation_metadata of this BulkActivationStatus.

        :param bulk_activation_metadata: The bulk_activation_metadata of this BulkActivationStatus.
        :type: oci.apm_traces.models.BulkActivationMetadata
        """
        self._bulk_activation_metadata = bulk_activation_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other