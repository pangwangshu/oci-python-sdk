# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801

from __future__ import absolute_import

from .capabilities_collection import CapabilitiesCollection
from .capability_details import CapabilityDetails
from .change_cluster_placement_group_compartment_details import ChangeClusterPlacementGroupCompartmentDetails
from .cluster_placement_group import ClusterPlacementGroup
from .cluster_placement_group_collection import ClusterPlacementGroupCollection
from .cluster_placement_group_summary import ClusterPlacementGroupSummary
from .create_cluster_placement_group_details import CreateClusterPlacementGroupDetails
from .placement_instruction_details import PlacementInstructionDetails
from .update_cluster_placement_group_details import UpdateClusterPlacementGroupDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for cluster_placement_groups services.
cluster_placement_groups_type_mapping = {
    "CapabilitiesCollection": CapabilitiesCollection,
    "CapabilityDetails": CapabilityDetails,
    "ChangeClusterPlacementGroupCompartmentDetails": ChangeClusterPlacementGroupCompartmentDetails,
    "ClusterPlacementGroup": ClusterPlacementGroup,
    "ClusterPlacementGroupCollection": ClusterPlacementGroupCollection,
    "ClusterPlacementGroupSummary": ClusterPlacementGroupSummary,
    "CreateClusterPlacementGroupDetails": CreateClusterPlacementGroupDetails,
    "PlacementInstructionDetails": PlacementInstructionDetails,
    "UpdateClusterPlacementGroupDetails": UpdateClusterPlacementGroupDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}