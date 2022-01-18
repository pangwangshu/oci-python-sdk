# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .absolute_wait_criteria import AbsoluteWaitCriteria
from .absolute_wait_criteria_summary import AbsoluteWaitCriteriaSummary
from .actual_build_runner_shape_config import ActualBuildRunnerShapeConfig
from .approval_action import ApprovalAction
from .approval_policy import ApprovalPolicy
from .approve_deployment_details import ApproveDeploymentDetails
from .automated_deploy_stage_rollback_policy import AutomatedDeployStageRollbackPolicy
from .backend_set_ip_collection import BackendSetIpCollection
from .build_outputs import BuildOutputs
from .build_pipeline import BuildPipeline
from .build_pipeline_collection import BuildPipelineCollection
from .build_pipeline_parameter import BuildPipelineParameter
from .build_pipeline_parameter_collection import BuildPipelineParameterCollection
from .build_pipeline_stage import BuildPipelineStage
from .build_pipeline_stage_collection import BuildPipelineStageCollection
from .build_pipeline_stage_predecessor import BuildPipelineStagePredecessor
from .build_pipeline_stage_predecessor_collection import BuildPipelineStagePredecessorCollection
from .build_pipeline_stage_run_progress import BuildPipelineStageRunProgress
from .build_pipeline_stage_summary import BuildPipelineStageSummary
from .build_pipeline_summary import BuildPipelineSummary
from .build_run import BuildRun
from .build_run_argument import BuildRunArgument
from .build_run_argument_collection import BuildRunArgumentCollection
from .build_run_progress import BuildRunProgress
from .build_run_progress_summary import BuildRunProgressSummary
from .build_run_source import BuildRunSource
from .build_run_summary import BuildRunSummary
from .build_run_summary_collection import BuildRunSummaryCollection
from .build_source import BuildSource
from .build_source_collection import BuildSourceCollection
from .build_stage import BuildStage
from .build_stage_run_progress import BuildStageRunProgress
from .build_stage_run_step import BuildStageRunStep
from .build_stage_summary import BuildStageSummary
from .cancel_build_run_details import CancelBuildRunDetails
from .cancel_deployment_details import CancelDeploymentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .commit_info import CommitInfo
from .compute_instance_group_by_ids_selector import ComputeInstanceGroupByIdsSelector
from .compute_instance_group_by_query_selector import ComputeInstanceGroupByQuerySelector
from .compute_instance_group_deploy_environment import ComputeInstanceGroupDeployEnvironment
from .compute_instance_group_deploy_environment_summary import ComputeInstanceGroupDeployEnvironmentSummary
from .compute_instance_group_deploy_stage import ComputeInstanceGroupDeployStage
from .compute_instance_group_deploy_stage_execution_progress import ComputeInstanceGroupDeployStageExecutionProgress
from .compute_instance_group_deploy_stage_summary import ComputeInstanceGroupDeployStageSummary
from .compute_instance_group_failure_policy import ComputeInstanceGroupFailurePolicy
from .compute_instance_group_failure_policy_by_count import ComputeInstanceGroupFailurePolicyByCount
from .compute_instance_group_failure_policy_by_percentage import ComputeInstanceGroupFailurePolicyByPercentage
from .compute_instance_group_linear_rollout_policy_by_count import ComputeInstanceGroupLinearRolloutPolicyByCount
from .compute_instance_group_linear_rollout_policy_by_percentage import ComputeInstanceGroupLinearRolloutPolicyByPercentage
from .compute_instance_group_rollout_policy import ComputeInstanceGroupRolloutPolicy
from .compute_instance_group_selector import ComputeInstanceGroupSelector
from .compute_instance_group_selector_collection import ComputeInstanceGroupSelectorCollection
from .connection import Connection
from .connection_collection import ConnectionCollection
from .connection_summary import ConnectionSummary
from .container_registry_delivered_artifact import ContainerRegistryDeliveredArtifact
from .count_based_approval_policy import CountBasedApprovalPolicy
from .create_absolute_wait_criteria_details import CreateAbsoluteWaitCriteriaDetails
from .create_build_pipeline_details import CreateBuildPipelineDetails
from .create_build_pipeline_stage_details import CreateBuildPipelineStageDetails
from .create_build_run_details import CreateBuildRunDetails
from .create_build_stage_details import CreateBuildStageDetails
from .create_compute_instance_group_deploy_environment_details import CreateComputeInstanceGroupDeployEnvironmentDetails
from .create_compute_instance_group_deploy_stage_details import CreateComputeInstanceGroupDeployStageDetails
from .create_connection_details import CreateConnectionDetails
from .create_deliver_artifact_stage_details import CreateDeliverArtifactStageDetails
from .create_deploy_artifact_details import CreateDeployArtifactDetails
from .create_deploy_environment_details import CreateDeployEnvironmentDetails
from .create_deploy_pipeline_deployment_details import CreateDeployPipelineDeploymentDetails
from .create_deploy_pipeline_details import CreateDeployPipelineDetails
from .create_deploy_pipeline_redeployment_details import CreateDeployPipelineRedeploymentDetails
from .create_deploy_stage_details import CreateDeployStageDetails
from .create_deployment_details import CreateDeploymentDetails
from .create_devops_code_repository_trigger_details import CreateDevopsCodeRepositoryTriggerDetails
from .create_function_deploy_environment_details import CreateFunctionDeployEnvironmentDetails
from .create_function_deploy_stage_details import CreateFunctionDeployStageDetails
from .create_github_access_token_connection_details import CreateGithubAccessTokenConnectionDetails
from .create_github_trigger_details import CreateGithubTriggerDetails
from .create_gitlab_access_token_connection_details import CreateGitlabAccessTokenConnectionDetails
from .create_gitlab_trigger_details import CreateGitlabTriggerDetails
from .create_invoke_function_deploy_stage_details import CreateInvokeFunctionDeployStageDetails
from .create_load_balancer_traffic_shift_deploy_stage_details import CreateLoadBalancerTrafficShiftDeployStageDetails
from .create_manual_approval_deploy_stage_details import CreateManualApprovalDeployStageDetails
from .create_oke_cluster_deploy_environment_details import CreateOkeClusterDeployEnvironmentDetails
from .create_oke_deploy_stage_details import CreateOkeDeployStageDetails
from .create_project_details import CreateProjectDetails
from .create_repository_details import CreateRepositoryDetails
from .create_single_deploy_stage_deployment_details import CreateSingleDeployStageDeploymentDetails
from .create_trigger_deployment_stage_details import CreateTriggerDeploymentStageDetails
from .create_trigger_details import CreateTriggerDetails
from .create_wait_criteria_details import CreateWaitCriteriaDetails
from .create_wait_deploy_stage_details import CreateWaitDeployStageDetails
from .create_wait_stage_details import CreateWaitStageDetails
from .deliver_artifact import DeliverArtifact
from .deliver_artifact_collection import DeliverArtifactCollection
from .deliver_artifact_stage import DeliverArtifactStage
from .deliver_artifact_stage_run_progress import DeliverArtifactStageRunProgress
from .deliver_artifact_stage_summary import DeliverArtifactStageSummary
from .delivered_artifact import DeliveredArtifact
from .delivered_artifact_collection import DeliveredArtifactCollection
from .deploy_artifact import DeployArtifact
from .deploy_artifact_collection import DeployArtifactCollection
from .deploy_artifact_override_argument import DeployArtifactOverrideArgument
from .deploy_artifact_override_argument_collection import DeployArtifactOverrideArgumentCollection
from .deploy_artifact_source import DeployArtifactSource
from .deploy_artifact_summary import DeployArtifactSummary
from .deploy_environment import DeployEnvironment
from .deploy_environment_collection import DeployEnvironmentCollection
from .deploy_environment_summary import DeployEnvironmentSummary
from .deploy_pipeline import DeployPipeline
from .deploy_pipeline_artifact import DeployPipelineArtifact
from .deploy_pipeline_artifact_collection import DeployPipelineArtifactCollection
from .deploy_pipeline_collection import DeployPipelineCollection
from .deploy_pipeline_deployment import DeployPipelineDeployment
from .deploy_pipeline_deployment_summary import DeployPipelineDeploymentSummary
from .deploy_pipeline_environment import DeployPipelineEnvironment
from .deploy_pipeline_environment_collection import DeployPipelineEnvironmentCollection
from .deploy_pipeline_parameter import DeployPipelineParameter
from .deploy_pipeline_parameter_collection import DeployPipelineParameterCollection
from .deploy_pipeline_redeployment import DeployPipelineRedeployment
from .deploy_pipeline_redeployment_summary import DeployPipelineRedeploymentSummary
from .deploy_pipeline_stage import DeployPipelineStage
from .deploy_pipeline_stage_collection import DeployPipelineStageCollection
from .deploy_pipeline_summary import DeployPipelineSummary
from .deploy_stage import DeployStage
from .deploy_stage_collection import DeployStageCollection
from .deploy_stage_execution_progress import DeployStageExecutionProgress
from .deploy_stage_execution_progress_details import DeployStageExecutionProgressDetails
from .deploy_stage_execution_step import DeployStageExecutionStep
from .deploy_stage_predecessor import DeployStagePredecessor
from .deploy_stage_predecessor_collection import DeployStagePredecessorCollection
from .deploy_stage_rollback_policy import DeployStageRollbackPolicy
from .deploy_stage_summary import DeployStageSummary
from .deployment import Deployment
from .deployment_argument import DeploymentArgument
from .deployment_argument_collection import DeploymentArgumentCollection
from .deployment_collection import DeploymentCollection
from .deployment_execution_progress import DeploymentExecutionProgress
from .deployment_summary import DeploymentSummary
from .devops_code_repository_build_run_source import DevopsCodeRepositoryBuildRunSource
from .devops_code_repository_build_source import DevopsCodeRepositoryBuildSource
from .devops_code_repository_filter import DevopsCodeRepositoryFilter
from .devops_code_repository_filter_attributes import DevopsCodeRepositoryFilterAttributes
from .devops_code_repository_trigger import DevopsCodeRepositoryTrigger
from .devops_code_repository_trigger_create_result import DevopsCodeRepositoryTriggerCreateResult
from .devops_code_repository_trigger_summary import DevopsCodeRepositoryTriggerSummary
from .diff_chunk import DiffChunk
from .diff_collection import DiffCollection
from .diff_line_details import DiffLineDetails
from .diff_response import DiffResponse
from .diff_response_entry import DiffResponseEntry
from .diff_section import DiffSection
from .diff_summary import DiffSummary
from .exported_variable import ExportedVariable
from .exported_variable_collection import ExportedVariableCollection
from .file_diff_response import FileDiffResponse
from .file_line_details import FileLineDetails
from .filter import Filter
from .function_deploy_environment import FunctionDeployEnvironment
from .function_deploy_environment_summary import FunctionDeployEnvironmentSummary
from .function_deploy_stage import FunctionDeployStage
from .function_deploy_stage_execution_progress import FunctionDeployStageExecutionProgress
from .function_deploy_stage_summary import FunctionDeployStageSummary
from .generic_delivered_artifact import GenericDeliveredArtifact
from .generic_deploy_artifact_source import GenericDeployArtifactSource
from .github_access_token_connection import GithubAccessTokenConnection
from .github_access_token_connection_summary import GithubAccessTokenConnectionSummary
from .github_build_run_source import GithubBuildRunSource
from .github_build_source import GithubBuildSource
from .github_filter import GithubFilter
from .github_filter_attributes import GithubFilterAttributes
from .github_trigger import GithubTrigger
from .github_trigger_create_result import GithubTriggerCreateResult
from .github_trigger_summary import GithubTriggerSummary
from .gitlab_access_token_connection import GitlabAccessTokenConnection
from .gitlab_access_token_connection_summary import GitlabAccessTokenConnectionSummary
from .gitlab_build_run_source import GitlabBuildRunSource
from .gitlab_build_source import GitlabBuildSource
from .gitlab_filter import GitlabFilter
from .gitlab_filter_attributes import GitlabFilterAttributes
from .gitlab_trigger import GitlabTrigger
from .gitlab_trigger_create_result import GitlabTriggerCreateResult
from .gitlab_trigger_summary import GitlabTriggerSummary
from .inline_deploy_artifact_source import InlineDeployArtifactSource
from .invoke_function_deploy_stage import InvokeFunctionDeployStage
from .invoke_function_deploy_stage_execution_progress import InvokeFunctionDeployStageExecutionProgress
from .invoke_function_deploy_stage_summary import InvokeFunctionDeployStageSummary
from .load_balancer_config import LoadBalancerConfig
from .load_balancer_traffic_shift_deploy_stage import LoadBalancerTrafficShiftDeployStage
from .load_balancer_traffic_shift_deploy_stage_execution_progress import LoadBalancerTrafficShiftDeployStageExecutionProgress
from .load_balancer_traffic_shift_deploy_stage_summary import LoadBalancerTrafficShiftDeployStageSummary
from .load_balancer_traffic_shift_rollout_policy import LoadBalancerTrafficShiftRolloutPolicy
from .manual_approval_deploy_stage import ManualApprovalDeployStage
from .manual_approval_deploy_stage_execution_progress import ManualApprovalDeployStageExecutionProgress
from .manual_approval_deploy_stage_summary import ManualApprovalDeployStageSummary
from .manual_build_run_source import ManualBuildRunSource
from .mirror_repository_config import MirrorRepositoryConfig
from .no_deploy_stage_rollback_policy import NoDeployStageRollbackPolicy
from .notification_config import NotificationConfig
from .ocir_deploy_artifact_source import OcirDeployArtifactSource
from .oke_cluster_deploy_environment import OkeClusterDeployEnvironment
from .oke_cluster_deploy_environment_summary import OkeClusterDeployEnvironmentSummary
from .oke_deploy_stage import OkeDeployStage
from .oke_deploy_stage_execution_progress import OkeDeployStageExecutionProgress
from .oke_deploy_stage_summary import OkeDeployStageSummary
from .project import Project
from .project_collection import ProjectCollection
from .project_summary import ProjectSummary
from .put_repository_branch_details import PutRepositoryBranchDetails
from .put_repository_ref_details import PutRepositoryRefDetails
from .put_repository_tag_details import PutRepositoryTagDetails
from .repository import Repository
from .repository_author_collection import RepositoryAuthorCollection
from .repository_author_summary import RepositoryAuthorSummary
from .repository_branch import RepositoryBranch
from .repository_branch_summary import RepositoryBranchSummary
from .repository_collection import RepositoryCollection
from .repository_commit import RepositoryCommit
from .repository_commit_collection import RepositoryCommitCollection
from .repository_commit_summary import RepositoryCommitSummary
from .repository_file_lines import RepositoryFileLines
from .repository_mirror_record import RepositoryMirrorRecord
from .repository_mirror_record_collection import RepositoryMirrorRecordCollection
from .repository_mirror_record_summary import RepositoryMirrorRecordSummary
from .repository_object import RepositoryObject
from .repository_path_collection import RepositoryPathCollection
from .repository_path_summary import RepositoryPathSummary
from .repository_ref import RepositoryRef
from .repository_ref_collection import RepositoryRefCollection
from .repository_ref_summary import RepositoryRefSummary
from .repository_summary import RepositorySummary
from .repository_tag import RepositoryTag
from .repository_tag_summary import RepositoryTagSummary
from .single_deploy_stage_deployment import SingleDeployStageDeployment
from .single_deploy_stage_deployment_summary import SingleDeployStageDeploymentSummary
from .trigger import Trigger
from .trigger_action import TriggerAction
from .trigger_build_pipeline_action import TriggerBuildPipelineAction
from .trigger_collection import TriggerCollection
from .trigger_create_result import TriggerCreateResult
from .trigger_deployment_pipeline_stage_run_progress import TriggerDeploymentPipelineStageRunProgress
from .trigger_deployment_stage import TriggerDeploymentStage
from .trigger_deployment_stage_summary import TriggerDeploymentStageSummary
from .trigger_info import TriggerInfo
from .trigger_schedule import TriggerSchedule
from .trigger_summary import TriggerSummary
from .update_absolute_wait_criteria_details import UpdateAbsoluteWaitCriteriaDetails
from .update_build_pipeline_details import UpdateBuildPipelineDetails
from .update_build_pipeline_stage_details import UpdateBuildPipelineStageDetails
from .update_build_run_details import UpdateBuildRunDetails
from .update_build_stage_details import UpdateBuildStageDetails
from .update_compute_instance_group_deploy_environment_details import UpdateComputeInstanceGroupDeployEnvironmentDetails
from .update_compute_instance_group_deploy_stage_details import UpdateComputeInstanceGroupDeployStageDetails
from .update_connection_details import UpdateConnectionDetails
from .update_deliver_artifact_stage_details import UpdateDeliverArtifactStageDetails
from .update_deploy_artifact_details import UpdateDeployArtifactDetails
from .update_deploy_environment_details import UpdateDeployEnvironmentDetails
from .update_deploy_pipeline_deployment_details import UpdateDeployPipelineDeploymentDetails
from .update_deploy_pipeline_details import UpdateDeployPipelineDetails
from .update_deploy_pipeline_redeployment_details import UpdateDeployPipelineRedeploymentDetails
from .update_deploy_stage_details import UpdateDeployStageDetails
from .update_deployment_details import UpdateDeploymentDetails
from .update_devops_code_repository_trigger_details import UpdateDevopsCodeRepositoryTriggerDetails
from .update_function_deploy_environment_details import UpdateFunctionDeployEnvironmentDetails
from .update_function_deploy_stage_details import UpdateFunctionDeployStageDetails
from .update_github_access_token_connection_details import UpdateGithubAccessTokenConnectionDetails
from .update_github_trigger_details import UpdateGithubTriggerDetails
from .update_gitlab_access_token_connection_details import UpdateGitlabAccessTokenConnectionDetails
from .update_gitlab_trigger_details import UpdateGitlabTriggerDetails
from .update_invoke_function_deploy_stage_details import UpdateInvokeFunctionDeployStageDetails
from .update_load_balancer_traffic_shift_deploy_stage_details import UpdateLoadBalancerTrafficShiftDeployStageDetails
from .update_manual_approval_deploy_stage_details import UpdateManualApprovalDeployStageDetails
from .update_oke_cluster_deploy_environment_details import UpdateOkeClusterDeployEnvironmentDetails
from .update_oke_deploy_stage_details import UpdateOkeDeployStageDetails
from .update_project_details import UpdateProjectDetails
from .update_repository_details import UpdateRepositoryDetails
from .update_single_deploy_stage_deployment_details import UpdateSingleDeployStageDeploymentDetails
from .update_trigger_deployment_stage_details import UpdateTriggerDeploymentStageDetails
from .update_trigger_details import UpdateTriggerDetails
from .update_wait_criteria_details import UpdateWaitCriteriaDetails
from .update_wait_deploy_stage_details import UpdateWaitDeployStageDetails
from .update_wait_stage_details import UpdateWaitStageDetails
from .wait_criteria import WaitCriteria
from .wait_criteria_summary import WaitCriteriaSummary
from .wait_deploy_stage import WaitDeployStage
from .wait_deploy_stage_execution_progress import WaitDeployStageExecutionProgress
from .wait_deploy_stage_summary import WaitDeployStageSummary
from .wait_stage import WaitStage
from .wait_stage_run_progress import WaitStageRunProgress
from .wait_stage_summary import WaitStageSummary
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for devops services.
devops_type_mapping = {
    "AbsoluteWaitCriteria": AbsoluteWaitCriteria,
    "AbsoluteWaitCriteriaSummary": AbsoluteWaitCriteriaSummary,
    "ActualBuildRunnerShapeConfig": ActualBuildRunnerShapeConfig,
    "ApprovalAction": ApprovalAction,
    "ApprovalPolicy": ApprovalPolicy,
    "ApproveDeploymentDetails": ApproveDeploymentDetails,
    "AutomatedDeployStageRollbackPolicy": AutomatedDeployStageRollbackPolicy,
    "BackendSetIpCollection": BackendSetIpCollection,
    "BuildOutputs": BuildOutputs,
    "BuildPipeline": BuildPipeline,
    "BuildPipelineCollection": BuildPipelineCollection,
    "BuildPipelineParameter": BuildPipelineParameter,
    "BuildPipelineParameterCollection": BuildPipelineParameterCollection,
    "BuildPipelineStage": BuildPipelineStage,
    "BuildPipelineStageCollection": BuildPipelineStageCollection,
    "BuildPipelineStagePredecessor": BuildPipelineStagePredecessor,
    "BuildPipelineStagePredecessorCollection": BuildPipelineStagePredecessorCollection,
    "BuildPipelineStageRunProgress": BuildPipelineStageRunProgress,
    "BuildPipelineStageSummary": BuildPipelineStageSummary,
    "BuildPipelineSummary": BuildPipelineSummary,
    "BuildRun": BuildRun,
    "BuildRunArgument": BuildRunArgument,
    "BuildRunArgumentCollection": BuildRunArgumentCollection,
    "BuildRunProgress": BuildRunProgress,
    "BuildRunProgressSummary": BuildRunProgressSummary,
    "BuildRunSource": BuildRunSource,
    "BuildRunSummary": BuildRunSummary,
    "BuildRunSummaryCollection": BuildRunSummaryCollection,
    "BuildSource": BuildSource,
    "BuildSourceCollection": BuildSourceCollection,
    "BuildStage": BuildStage,
    "BuildStageRunProgress": BuildStageRunProgress,
    "BuildStageRunStep": BuildStageRunStep,
    "BuildStageSummary": BuildStageSummary,
    "CancelBuildRunDetails": CancelBuildRunDetails,
    "CancelDeploymentDetails": CancelDeploymentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "CommitInfo": CommitInfo,
    "ComputeInstanceGroupByIdsSelector": ComputeInstanceGroupByIdsSelector,
    "ComputeInstanceGroupByQuerySelector": ComputeInstanceGroupByQuerySelector,
    "ComputeInstanceGroupDeployEnvironment": ComputeInstanceGroupDeployEnvironment,
    "ComputeInstanceGroupDeployEnvironmentSummary": ComputeInstanceGroupDeployEnvironmentSummary,
    "ComputeInstanceGroupDeployStage": ComputeInstanceGroupDeployStage,
    "ComputeInstanceGroupDeployStageExecutionProgress": ComputeInstanceGroupDeployStageExecutionProgress,
    "ComputeInstanceGroupDeployStageSummary": ComputeInstanceGroupDeployStageSummary,
    "ComputeInstanceGroupFailurePolicy": ComputeInstanceGroupFailurePolicy,
    "ComputeInstanceGroupFailurePolicyByCount": ComputeInstanceGroupFailurePolicyByCount,
    "ComputeInstanceGroupFailurePolicyByPercentage": ComputeInstanceGroupFailurePolicyByPercentage,
    "ComputeInstanceGroupLinearRolloutPolicyByCount": ComputeInstanceGroupLinearRolloutPolicyByCount,
    "ComputeInstanceGroupLinearRolloutPolicyByPercentage": ComputeInstanceGroupLinearRolloutPolicyByPercentage,
    "ComputeInstanceGroupRolloutPolicy": ComputeInstanceGroupRolloutPolicy,
    "ComputeInstanceGroupSelector": ComputeInstanceGroupSelector,
    "ComputeInstanceGroupSelectorCollection": ComputeInstanceGroupSelectorCollection,
    "Connection": Connection,
    "ConnectionCollection": ConnectionCollection,
    "ConnectionSummary": ConnectionSummary,
    "ContainerRegistryDeliveredArtifact": ContainerRegistryDeliveredArtifact,
    "CountBasedApprovalPolicy": CountBasedApprovalPolicy,
    "CreateAbsoluteWaitCriteriaDetails": CreateAbsoluteWaitCriteriaDetails,
    "CreateBuildPipelineDetails": CreateBuildPipelineDetails,
    "CreateBuildPipelineStageDetails": CreateBuildPipelineStageDetails,
    "CreateBuildRunDetails": CreateBuildRunDetails,
    "CreateBuildStageDetails": CreateBuildStageDetails,
    "CreateComputeInstanceGroupDeployEnvironmentDetails": CreateComputeInstanceGroupDeployEnvironmentDetails,
    "CreateComputeInstanceGroupDeployStageDetails": CreateComputeInstanceGroupDeployStageDetails,
    "CreateConnectionDetails": CreateConnectionDetails,
    "CreateDeliverArtifactStageDetails": CreateDeliverArtifactStageDetails,
    "CreateDeployArtifactDetails": CreateDeployArtifactDetails,
    "CreateDeployEnvironmentDetails": CreateDeployEnvironmentDetails,
    "CreateDeployPipelineDeploymentDetails": CreateDeployPipelineDeploymentDetails,
    "CreateDeployPipelineDetails": CreateDeployPipelineDetails,
    "CreateDeployPipelineRedeploymentDetails": CreateDeployPipelineRedeploymentDetails,
    "CreateDeployStageDetails": CreateDeployStageDetails,
    "CreateDeploymentDetails": CreateDeploymentDetails,
    "CreateDevopsCodeRepositoryTriggerDetails": CreateDevopsCodeRepositoryTriggerDetails,
    "CreateFunctionDeployEnvironmentDetails": CreateFunctionDeployEnvironmentDetails,
    "CreateFunctionDeployStageDetails": CreateFunctionDeployStageDetails,
    "CreateGithubAccessTokenConnectionDetails": CreateGithubAccessTokenConnectionDetails,
    "CreateGithubTriggerDetails": CreateGithubTriggerDetails,
    "CreateGitlabAccessTokenConnectionDetails": CreateGitlabAccessTokenConnectionDetails,
    "CreateGitlabTriggerDetails": CreateGitlabTriggerDetails,
    "CreateInvokeFunctionDeployStageDetails": CreateInvokeFunctionDeployStageDetails,
    "CreateLoadBalancerTrafficShiftDeployStageDetails": CreateLoadBalancerTrafficShiftDeployStageDetails,
    "CreateManualApprovalDeployStageDetails": CreateManualApprovalDeployStageDetails,
    "CreateOkeClusterDeployEnvironmentDetails": CreateOkeClusterDeployEnvironmentDetails,
    "CreateOkeDeployStageDetails": CreateOkeDeployStageDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "CreateRepositoryDetails": CreateRepositoryDetails,
    "CreateSingleDeployStageDeploymentDetails": CreateSingleDeployStageDeploymentDetails,
    "CreateTriggerDeploymentStageDetails": CreateTriggerDeploymentStageDetails,
    "CreateTriggerDetails": CreateTriggerDetails,
    "CreateWaitCriteriaDetails": CreateWaitCriteriaDetails,
    "CreateWaitDeployStageDetails": CreateWaitDeployStageDetails,
    "CreateWaitStageDetails": CreateWaitStageDetails,
    "DeliverArtifact": DeliverArtifact,
    "DeliverArtifactCollection": DeliverArtifactCollection,
    "DeliverArtifactStage": DeliverArtifactStage,
    "DeliverArtifactStageRunProgress": DeliverArtifactStageRunProgress,
    "DeliverArtifactStageSummary": DeliverArtifactStageSummary,
    "DeliveredArtifact": DeliveredArtifact,
    "DeliveredArtifactCollection": DeliveredArtifactCollection,
    "DeployArtifact": DeployArtifact,
    "DeployArtifactCollection": DeployArtifactCollection,
    "DeployArtifactOverrideArgument": DeployArtifactOverrideArgument,
    "DeployArtifactOverrideArgumentCollection": DeployArtifactOverrideArgumentCollection,
    "DeployArtifactSource": DeployArtifactSource,
    "DeployArtifactSummary": DeployArtifactSummary,
    "DeployEnvironment": DeployEnvironment,
    "DeployEnvironmentCollection": DeployEnvironmentCollection,
    "DeployEnvironmentSummary": DeployEnvironmentSummary,
    "DeployPipeline": DeployPipeline,
    "DeployPipelineArtifact": DeployPipelineArtifact,
    "DeployPipelineArtifactCollection": DeployPipelineArtifactCollection,
    "DeployPipelineCollection": DeployPipelineCollection,
    "DeployPipelineDeployment": DeployPipelineDeployment,
    "DeployPipelineDeploymentSummary": DeployPipelineDeploymentSummary,
    "DeployPipelineEnvironment": DeployPipelineEnvironment,
    "DeployPipelineEnvironmentCollection": DeployPipelineEnvironmentCollection,
    "DeployPipelineParameter": DeployPipelineParameter,
    "DeployPipelineParameterCollection": DeployPipelineParameterCollection,
    "DeployPipelineRedeployment": DeployPipelineRedeployment,
    "DeployPipelineRedeploymentSummary": DeployPipelineRedeploymentSummary,
    "DeployPipelineStage": DeployPipelineStage,
    "DeployPipelineStageCollection": DeployPipelineStageCollection,
    "DeployPipelineSummary": DeployPipelineSummary,
    "DeployStage": DeployStage,
    "DeployStageCollection": DeployStageCollection,
    "DeployStageExecutionProgress": DeployStageExecutionProgress,
    "DeployStageExecutionProgressDetails": DeployStageExecutionProgressDetails,
    "DeployStageExecutionStep": DeployStageExecutionStep,
    "DeployStagePredecessor": DeployStagePredecessor,
    "DeployStagePredecessorCollection": DeployStagePredecessorCollection,
    "DeployStageRollbackPolicy": DeployStageRollbackPolicy,
    "DeployStageSummary": DeployStageSummary,
    "Deployment": Deployment,
    "DeploymentArgument": DeploymentArgument,
    "DeploymentArgumentCollection": DeploymentArgumentCollection,
    "DeploymentCollection": DeploymentCollection,
    "DeploymentExecutionProgress": DeploymentExecutionProgress,
    "DeploymentSummary": DeploymentSummary,
    "DevopsCodeRepositoryBuildRunSource": DevopsCodeRepositoryBuildRunSource,
    "DevopsCodeRepositoryBuildSource": DevopsCodeRepositoryBuildSource,
    "DevopsCodeRepositoryFilter": DevopsCodeRepositoryFilter,
    "DevopsCodeRepositoryFilterAttributes": DevopsCodeRepositoryFilterAttributes,
    "DevopsCodeRepositoryTrigger": DevopsCodeRepositoryTrigger,
    "DevopsCodeRepositoryTriggerCreateResult": DevopsCodeRepositoryTriggerCreateResult,
    "DevopsCodeRepositoryTriggerSummary": DevopsCodeRepositoryTriggerSummary,
    "DiffChunk": DiffChunk,
    "DiffCollection": DiffCollection,
    "DiffLineDetails": DiffLineDetails,
    "DiffResponse": DiffResponse,
    "DiffResponseEntry": DiffResponseEntry,
    "DiffSection": DiffSection,
    "DiffSummary": DiffSummary,
    "ExportedVariable": ExportedVariable,
    "ExportedVariableCollection": ExportedVariableCollection,
    "FileDiffResponse": FileDiffResponse,
    "FileLineDetails": FileLineDetails,
    "Filter": Filter,
    "FunctionDeployEnvironment": FunctionDeployEnvironment,
    "FunctionDeployEnvironmentSummary": FunctionDeployEnvironmentSummary,
    "FunctionDeployStage": FunctionDeployStage,
    "FunctionDeployStageExecutionProgress": FunctionDeployStageExecutionProgress,
    "FunctionDeployStageSummary": FunctionDeployStageSummary,
    "GenericDeliveredArtifact": GenericDeliveredArtifact,
    "GenericDeployArtifactSource": GenericDeployArtifactSource,
    "GithubAccessTokenConnection": GithubAccessTokenConnection,
    "GithubAccessTokenConnectionSummary": GithubAccessTokenConnectionSummary,
    "GithubBuildRunSource": GithubBuildRunSource,
    "GithubBuildSource": GithubBuildSource,
    "GithubFilter": GithubFilter,
    "GithubFilterAttributes": GithubFilterAttributes,
    "GithubTrigger": GithubTrigger,
    "GithubTriggerCreateResult": GithubTriggerCreateResult,
    "GithubTriggerSummary": GithubTriggerSummary,
    "GitlabAccessTokenConnection": GitlabAccessTokenConnection,
    "GitlabAccessTokenConnectionSummary": GitlabAccessTokenConnectionSummary,
    "GitlabBuildRunSource": GitlabBuildRunSource,
    "GitlabBuildSource": GitlabBuildSource,
    "GitlabFilter": GitlabFilter,
    "GitlabFilterAttributes": GitlabFilterAttributes,
    "GitlabTrigger": GitlabTrigger,
    "GitlabTriggerCreateResult": GitlabTriggerCreateResult,
    "GitlabTriggerSummary": GitlabTriggerSummary,
    "InlineDeployArtifactSource": InlineDeployArtifactSource,
    "InvokeFunctionDeployStage": InvokeFunctionDeployStage,
    "InvokeFunctionDeployStageExecutionProgress": InvokeFunctionDeployStageExecutionProgress,
    "InvokeFunctionDeployStageSummary": InvokeFunctionDeployStageSummary,
    "LoadBalancerConfig": LoadBalancerConfig,
    "LoadBalancerTrafficShiftDeployStage": LoadBalancerTrafficShiftDeployStage,
    "LoadBalancerTrafficShiftDeployStageExecutionProgress": LoadBalancerTrafficShiftDeployStageExecutionProgress,
    "LoadBalancerTrafficShiftDeployStageSummary": LoadBalancerTrafficShiftDeployStageSummary,
    "LoadBalancerTrafficShiftRolloutPolicy": LoadBalancerTrafficShiftRolloutPolicy,
    "ManualApprovalDeployStage": ManualApprovalDeployStage,
    "ManualApprovalDeployStageExecutionProgress": ManualApprovalDeployStageExecutionProgress,
    "ManualApprovalDeployStageSummary": ManualApprovalDeployStageSummary,
    "ManualBuildRunSource": ManualBuildRunSource,
    "MirrorRepositoryConfig": MirrorRepositoryConfig,
    "NoDeployStageRollbackPolicy": NoDeployStageRollbackPolicy,
    "NotificationConfig": NotificationConfig,
    "OcirDeployArtifactSource": OcirDeployArtifactSource,
    "OkeClusterDeployEnvironment": OkeClusterDeployEnvironment,
    "OkeClusterDeployEnvironmentSummary": OkeClusterDeployEnvironmentSummary,
    "OkeDeployStage": OkeDeployStage,
    "OkeDeployStageExecutionProgress": OkeDeployStageExecutionProgress,
    "OkeDeployStageSummary": OkeDeployStageSummary,
    "Project": Project,
    "ProjectCollection": ProjectCollection,
    "ProjectSummary": ProjectSummary,
    "PutRepositoryBranchDetails": PutRepositoryBranchDetails,
    "PutRepositoryRefDetails": PutRepositoryRefDetails,
    "PutRepositoryTagDetails": PutRepositoryTagDetails,
    "Repository": Repository,
    "RepositoryAuthorCollection": RepositoryAuthorCollection,
    "RepositoryAuthorSummary": RepositoryAuthorSummary,
    "RepositoryBranch": RepositoryBranch,
    "RepositoryBranchSummary": RepositoryBranchSummary,
    "RepositoryCollection": RepositoryCollection,
    "RepositoryCommit": RepositoryCommit,
    "RepositoryCommitCollection": RepositoryCommitCollection,
    "RepositoryCommitSummary": RepositoryCommitSummary,
    "RepositoryFileLines": RepositoryFileLines,
    "RepositoryMirrorRecord": RepositoryMirrorRecord,
    "RepositoryMirrorRecordCollection": RepositoryMirrorRecordCollection,
    "RepositoryMirrorRecordSummary": RepositoryMirrorRecordSummary,
    "RepositoryObject": RepositoryObject,
    "RepositoryPathCollection": RepositoryPathCollection,
    "RepositoryPathSummary": RepositoryPathSummary,
    "RepositoryRef": RepositoryRef,
    "RepositoryRefCollection": RepositoryRefCollection,
    "RepositoryRefSummary": RepositoryRefSummary,
    "RepositorySummary": RepositorySummary,
    "RepositoryTag": RepositoryTag,
    "RepositoryTagSummary": RepositoryTagSummary,
    "SingleDeployStageDeployment": SingleDeployStageDeployment,
    "SingleDeployStageDeploymentSummary": SingleDeployStageDeploymentSummary,
    "Trigger": Trigger,
    "TriggerAction": TriggerAction,
    "TriggerBuildPipelineAction": TriggerBuildPipelineAction,
    "TriggerCollection": TriggerCollection,
    "TriggerCreateResult": TriggerCreateResult,
    "TriggerDeploymentPipelineStageRunProgress": TriggerDeploymentPipelineStageRunProgress,
    "TriggerDeploymentStage": TriggerDeploymentStage,
    "TriggerDeploymentStageSummary": TriggerDeploymentStageSummary,
    "TriggerInfo": TriggerInfo,
    "TriggerSchedule": TriggerSchedule,
    "TriggerSummary": TriggerSummary,
    "UpdateAbsoluteWaitCriteriaDetails": UpdateAbsoluteWaitCriteriaDetails,
    "UpdateBuildPipelineDetails": UpdateBuildPipelineDetails,
    "UpdateBuildPipelineStageDetails": UpdateBuildPipelineStageDetails,
    "UpdateBuildRunDetails": UpdateBuildRunDetails,
    "UpdateBuildStageDetails": UpdateBuildStageDetails,
    "UpdateComputeInstanceGroupDeployEnvironmentDetails": UpdateComputeInstanceGroupDeployEnvironmentDetails,
    "UpdateComputeInstanceGroupDeployStageDetails": UpdateComputeInstanceGroupDeployStageDetails,
    "UpdateConnectionDetails": UpdateConnectionDetails,
    "UpdateDeliverArtifactStageDetails": UpdateDeliverArtifactStageDetails,
    "UpdateDeployArtifactDetails": UpdateDeployArtifactDetails,
    "UpdateDeployEnvironmentDetails": UpdateDeployEnvironmentDetails,
    "UpdateDeployPipelineDeploymentDetails": UpdateDeployPipelineDeploymentDetails,
    "UpdateDeployPipelineDetails": UpdateDeployPipelineDetails,
    "UpdateDeployPipelineRedeploymentDetails": UpdateDeployPipelineRedeploymentDetails,
    "UpdateDeployStageDetails": UpdateDeployStageDetails,
    "UpdateDeploymentDetails": UpdateDeploymentDetails,
    "UpdateDevopsCodeRepositoryTriggerDetails": UpdateDevopsCodeRepositoryTriggerDetails,
    "UpdateFunctionDeployEnvironmentDetails": UpdateFunctionDeployEnvironmentDetails,
    "UpdateFunctionDeployStageDetails": UpdateFunctionDeployStageDetails,
    "UpdateGithubAccessTokenConnectionDetails": UpdateGithubAccessTokenConnectionDetails,
    "UpdateGithubTriggerDetails": UpdateGithubTriggerDetails,
    "UpdateGitlabAccessTokenConnectionDetails": UpdateGitlabAccessTokenConnectionDetails,
    "UpdateGitlabTriggerDetails": UpdateGitlabTriggerDetails,
    "UpdateInvokeFunctionDeployStageDetails": UpdateInvokeFunctionDeployStageDetails,
    "UpdateLoadBalancerTrafficShiftDeployStageDetails": UpdateLoadBalancerTrafficShiftDeployStageDetails,
    "UpdateManualApprovalDeployStageDetails": UpdateManualApprovalDeployStageDetails,
    "UpdateOkeClusterDeployEnvironmentDetails": UpdateOkeClusterDeployEnvironmentDetails,
    "UpdateOkeDeployStageDetails": UpdateOkeDeployStageDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "UpdateRepositoryDetails": UpdateRepositoryDetails,
    "UpdateSingleDeployStageDeploymentDetails": UpdateSingleDeployStageDeploymentDetails,
    "UpdateTriggerDeploymentStageDetails": UpdateTriggerDeploymentStageDetails,
    "UpdateTriggerDetails": UpdateTriggerDetails,
    "UpdateWaitCriteriaDetails": UpdateWaitCriteriaDetails,
    "UpdateWaitDeployStageDetails": UpdateWaitDeployStageDetails,
    "UpdateWaitStageDetails": UpdateWaitStageDetails,
    "WaitCriteria": WaitCriteria,
    "WaitCriteriaSummary": WaitCriteriaSummary,
    "WaitDeployStage": WaitDeployStage,
    "WaitDeployStageExecutionProgress": WaitDeployStageExecutionProgress,
    "WaitDeployStageSummary": WaitDeployStageSummary,
    "WaitStage": WaitStage,
    "WaitStageRunProgress": WaitStageRunProgress,
    "WaitStageSummary": WaitStageSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}