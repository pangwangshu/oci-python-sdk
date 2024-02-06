# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDedicatedCatalogDetail(object):
    """
    Details required for creation of ATP-D based catalog.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDedicatedCatalogDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_key_details:
            The value to assign to the encryption_key_details property of this CreateDedicatedCatalogDetail.
        :type encryption_key_details: oci.globally_distributed_database.models.DedicatedShardOrCatalogEncryptionKeyDetails

        :param admin_password:
            The value to assign to the admin_password property of this CreateDedicatedCatalogDetail.
        :type admin_password: str

        :param compute_count:
            The value to assign to the compute_count property of this CreateDedicatedCatalogDetail.
        :type compute_count: float

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this CreateDedicatedCatalogDetail.
        :type data_storage_size_in_gbs: float

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateDedicatedCatalogDetail.
        :type is_auto_scaling_enabled: bool

        :param cloud_autonomous_vm_cluster_id:
            The value to assign to the cloud_autonomous_vm_cluster_id property of this CreateDedicatedCatalogDetail.
        :type cloud_autonomous_vm_cluster_id: str

        :param peer_cloud_autonomous_vm_cluster_id:
            The value to assign to the peer_cloud_autonomous_vm_cluster_id property of this CreateDedicatedCatalogDetail.
        :type peer_cloud_autonomous_vm_cluster_id: str

        """
        self.swagger_types = {
            'encryption_key_details': 'DedicatedShardOrCatalogEncryptionKeyDetails',
            'admin_password': 'str',
            'compute_count': 'float',
            'data_storage_size_in_gbs': 'float',
            'is_auto_scaling_enabled': 'bool',
            'cloud_autonomous_vm_cluster_id': 'str',
            'peer_cloud_autonomous_vm_cluster_id': 'str'
        }

        self.attribute_map = {
            'encryption_key_details': 'encryptionKeyDetails',
            'admin_password': 'adminPassword',
            'compute_count': 'computeCount',
            'data_storage_size_in_gbs': 'dataStorageSizeInGbs',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'cloud_autonomous_vm_cluster_id': 'cloudAutonomousVmClusterId',
            'peer_cloud_autonomous_vm_cluster_id': 'peerCloudAutonomousVmClusterId'
        }

        self._encryption_key_details = None
        self._admin_password = None
        self._compute_count = None
        self._data_storage_size_in_gbs = None
        self._is_auto_scaling_enabled = None
        self._cloud_autonomous_vm_cluster_id = None
        self._peer_cloud_autonomous_vm_cluster_id = None

    @property
    def encryption_key_details(self):
        """
        Gets the encryption_key_details of this CreateDedicatedCatalogDetail.

        :return: The encryption_key_details of this CreateDedicatedCatalogDetail.
        :rtype: oci.globally_distributed_database.models.DedicatedShardOrCatalogEncryptionKeyDetails
        """
        return self._encryption_key_details

    @encryption_key_details.setter
    def encryption_key_details(self, encryption_key_details):
        """
        Sets the encryption_key_details of this CreateDedicatedCatalogDetail.

        :param encryption_key_details: The encryption_key_details of this CreateDedicatedCatalogDetail.
        :type: oci.globally_distributed_database.models.DedicatedShardOrCatalogEncryptionKeyDetails
        """
        self._encryption_key_details = encryption_key_details

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateDedicatedCatalogDetail.
        Admin password for the catalog database.


        :return: The admin_password of this CreateDedicatedCatalogDetail.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateDedicatedCatalogDetail.
        Admin password for the catalog database.


        :param admin_password: The admin_password of this CreateDedicatedCatalogDetail.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def compute_count(self):
        """
        **[Required]** Gets the compute_count of this CreateDedicatedCatalogDetail.
        The compute count for the catalog database. It has to be in multiple of 2.


        :return: The compute_count of this CreateDedicatedCatalogDetail.
        :rtype: float
        """
        return self._compute_count

    @compute_count.setter
    def compute_count(self, compute_count):
        """
        Sets the compute_count of this CreateDedicatedCatalogDetail.
        The compute count for the catalog database. It has to be in multiple of 2.


        :param compute_count: The compute_count of this CreateDedicatedCatalogDetail.
        :type: float
        """
        self._compute_count = compute_count

    @property
    def data_storage_size_in_gbs(self):
        """
        **[Required]** Gets the data_storage_size_in_gbs of this CreateDedicatedCatalogDetail.
        The data disk group size to be allocated in GBs for the catalog database.


        :return: The data_storage_size_in_gbs of this CreateDedicatedCatalogDetail.
        :rtype: float
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this CreateDedicatedCatalogDetail.
        The data disk group size to be allocated in GBs for the catalog database.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this CreateDedicatedCatalogDetail.
        :type: float
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def is_auto_scaling_enabled(self):
        """
        **[Required]** Gets the is_auto_scaling_enabled of this CreateDedicatedCatalogDetail.
        Determines the auto-scaling mode for the catalog database.


        :return: The is_auto_scaling_enabled of this CreateDedicatedCatalogDetail.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this CreateDedicatedCatalogDetail.
        Determines the auto-scaling mode for the catalog database.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this CreateDedicatedCatalogDetail.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def cloud_autonomous_vm_cluster_id(self):
        """
        **[Required]** Gets the cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        The `OCID`__ of the cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        :rtype: str
        """
        return self._cloud_autonomous_vm_cluster_id

    @cloud_autonomous_vm_cluster_id.setter
    def cloud_autonomous_vm_cluster_id(self, cloud_autonomous_vm_cluster_id):
        """
        Sets the cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        The `OCID`__ of the cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_autonomous_vm_cluster_id: The cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        :type: str
        """
        self._cloud_autonomous_vm_cluster_id = cloud_autonomous_vm_cluster_id

    @property
    def peer_cloud_autonomous_vm_cluster_id(self):
        """
        Gets the peer_cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        The `OCID`__ of the peer cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        :rtype: str
        """
        return self._peer_cloud_autonomous_vm_cluster_id

    @peer_cloud_autonomous_vm_cluster_id.setter
    def peer_cloud_autonomous_vm_cluster_id(self, peer_cloud_autonomous_vm_cluster_id):
        """
        Sets the peer_cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        The `OCID`__ of the peer cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_cloud_autonomous_vm_cluster_id: The peer_cloud_autonomous_vm_cluster_id of this CreateDedicatedCatalogDetail.
        :type: str
        """
        self._peer_cloud_autonomous_vm_cluster_id = peer_cloud_autonomous_vm_cluster_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
