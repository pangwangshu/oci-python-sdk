# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301

from .sharded_database import ShardedDatabase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedShardedDatabase(ShardedDatabase):
    """
    Details of ATP-D based sharded database.
    """

    #: A constant which can be used with the db_workload property of a DedicatedShardedDatabase.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a DedicatedShardedDatabase.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the sharding_method property of a DedicatedShardedDatabase.
    #: This constant has a value of "USER"
    SHARDING_METHOD_USER = "USER"

    #: A constant which can be used with the sharding_method property of a DedicatedShardedDatabase.
    #: This constant has a value of "SYSTEM"
    SHARDING_METHOD_SYSTEM = "SYSTEM"

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedShardedDatabase object with values from keyword arguments. The default value of the :py:attr:`~oci.globally_distributed_database.models.DedicatedShardedDatabase.db_deployment_type` attribute
        of this class is ``DEDICATED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DedicatedShardedDatabase.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DedicatedShardedDatabase.
        :type compartment_id: str

        :param db_deployment_type:
            The value to assign to the db_deployment_type property of this DedicatedShardedDatabase.
            Allowed values for this property are: "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this DedicatedShardedDatabase.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this DedicatedShardedDatabase.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DedicatedShardedDatabase.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DedicatedShardedDatabase.
            Allowed values for this property are: "ACTIVE", "FAILED", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "UPDATING", "CREATING", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this DedicatedShardedDatabase.
        :type lifecycle_state_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DedicatedShardedDatabase.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DedicatedShardedDatabase.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DedicatedShardedDatabase.
        :type system_tags: dict(str, dict(str, object))

        :param cluster_certificate_common_name:
            The value to assign to the cluster_certificate_common_name property of this DedicatedShardedDatabase.
        :type cluster_certificate_common_name: str

        :param character_set:
            The value to assign to the character_set property of this DedicatedShardedDatabase.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this DedicatedShardedDatabase.
        :type ncharacter_set: str

        :param chunks:
            The value to assign to the chunks property of this DedicatedShardedDatabase.
        :type chunks: int

        :param db_workload:
            The value to assign to the db_workload property of this DedicatedShardedDatabase.
            Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_workload: str

        :param sharding_method:
            The value to assign to the sharding_method property of this DedicatedShardedDatabase.
            Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type sharding_method: str

        :param db_version:
            The value to assign to the db_version property of this DedicatedShardedDatabase.
        :type db_version: str

        :param listener_port:
            The value to assign to the listener_port property of this DedicatedShardedDatabase.
        :type listener_port: int

        :param listener_port_tls:
            The value to assign to the listener_port_tls property of this DedicatedShardedDatabase.
        :type listener_port_tls: int

        :param ons_port_local:
            The value to assign to the ons_port_local property of this DedicatedShardedDatabase.
        :type ons_port_local: int

        :param ons_port_remote:
            The value to assign to the ons_port_remote property of this DedicatedShardedDatabase.
        :type ons_port_remote: int

        :param prefix:
            The value to assign to the prefix property of this DedicatedShardedDatabase.
        :type prefix: str

        :param private_endpoint:
            The value to assign to the private_endpoint property of this DedicatedShardedDatabase.
        :type private_endpoint: str

        :param connection_strings:
            The value to assign to the connection_strings property of this DedicatedShardedDatabase.
        :type connection_strings: oci.globally_distributed_database.models.ConnectionString

        :param time_zone:
            The value to assign to the time_zone property of this DedicatedShardedDatabase.
        :type time_zone: str

        :param gsms:
            The value to assign to the gsms property of this DedicatedShardedDatabase.
        :type gsms: list[oci.globally_distributed_database.models.GsmDetails]

        :param shard_details:
            The value to assign to the shard_details property of this DedicatedShardedDatabase.
        :type shard_details: list[oci.globally_distributed_database.models.DedicatedShardDetails]

        :param catalog_details:
            The value to assign to the catalog_details property of this DedicatedShardedDatabase.
        :type catalog_details: list[oci.globally_distributed_database.models.DedicatedCatalogDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_deployment_type': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'cluster_certificate_common_name': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'chunks': 'int',
            'db_workload': 'str',
            'sharding_method': 'str',
            'db_version': 'str',
            'listener_port': 'int',
            'listener_port_tls': 'int',
            'ons_port_local': 'int',
            'ons_port_remote': 'int',
            'prefix': 'str',
            'private_endpoint': 'str',
            'connection_strings': 'ConnectionString',
            'time_zone': 'str',
            'gsms': 'list[GsmDetails]',
            'shard_details': 'list[DedicatedShardDetails]',
            'catalog_details': 'list[DedicatedCatalogDetails]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_deployment_type': 'dbDeploymentType',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'cluster_certificate_common_name': 'clusterCertificateCommonName',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'chunks': 'chunks',
            'db_workload': 'dbWorkload',
            'sharding_method': 'shardingMethod',
            'db_version': 'dbVersion',
            'listener_port': 'listenerPort',
            'listener_port_tls': 'listenerPortTls',
            'ons_port_local': 'onsPortLocal',
            'ons_port_remote': 'onsPortRemote',
            'prefix': 'prefix',
            'private_endpoint': 'privateEndpoint',
            'connection_strings': 'connectionStrings',
            'time_zone': 'timeZone',
            'gsms': 'gsms',
            'shard_details': 'shardDetails',
            'catalog_details': 'catalogDetails'
        }

        self._id = None
        self._compartment_id = None
        self._db_deployment_type = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._cluster_certificate_common_name = None
        self._character_set = None
        self._ncharacter_set = None
        self._chunks = None
        self._db_workload = None
        self._sharding_method = None
        self._db_version = None
        self._listener_port = None
        self._listener_port_tls = None
        self._ons_port_local = None
        self._ons_port_remote = None
        self._prefix = None
        self._private_endpoint = None
        self._connection_strings = None
        self._time_zone = None
        self._gsms = None
        self._shard_details = None
        self._catalog_details = None
        self._db_deployment_type = 'DEDICATED'

    @property
    def cluster_certificate_common_name(self):
        """
        Gets the cluster_certificate_common_name of this DedicatedShardedDatabase.
        The certificate common name used in all cloudAutonomousVmClusters for the sharded database topology. Eg. Production.
        All the clusters used in one sharded database topology shall have same CABundle setup. Valid characterset for
        clusterCertificateCommonName include uppercase or lowercase letters, numbers, hyphens, underscores, and period.


        :return: The cluster_certificate_common_name of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._cluster_certificate_common_name

    @cluster_certificate_common_name.setter
    def cluster_certificate_common_name(self, cluster_certificate_common_name):
        """
        Sets the cluster_certificate_common_name of this DedicatedShardedDatabase.
        The certificate common name used in all cloudAutonomousVmClusters for the sharded database topology. Eg. Production.
        All the clusters used in one sharded database topology shall have same CABundle setup. Valid characterset for
        clusterCertificateCommonName include uppercase or lowercase letters, numbers, hyphens, underscores, and period.


        :param cluster_certificate_common_name: The cluster_certificate_common_name of this DedicatedShardedDatabase.
        :type: str
        """
        self._cluster_certificate_common_name = cluster_certificate_common_name

    @property
    def character_set(self):
        """
        **[Required]** Gets the character_set of this DedicatedShardedDatabase.
        The character set for the database.


        :return: The character_set of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this DedicatedShardedDatabase.
        The character set for the database.


        :param character_set: The character_set of this DedicatedShardedDatabase.
        :type: str
        """
        self._character_set = character_set

    @property
    def ncharacter_set(self):
        """
        **[Required]** Gets the ncharacter_set of this DedicatedShardedDatabase.
        The national character set for the database.


        :return: The ncharacter_set of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this DedicatedShardedDatabase.
        The national character set for the database.


        :param ncharacter_set: The ncharacter_set of this DedicatedShardedDatabase.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def chunks(self):
        """
        Gets the chunks of this DedicatedShardedDatabase.
        The default number of unique chunks in a shardspace. The value of chunks must be
        greater than 2 times the size of the largest shardgroup in any shardspace.


        :return: The chunks of this DedicatedShardedDatabase.
        :rtype: int
        """
        return self._chunks

    @chunks.setter
    def chunks(self, chunks):
        """
        Sets the chunks of this DedicatedShardedDatabase.
        The default number of unique chunks in a shardspace. The value of chunks must be
        greater than 2 times the size of the largest shardgroup in any shardspace.


        :param chunks: The chunks of this DedicatedShardedDatabase.
        :type: int
        """
        self._chunks = chunks

    @property
    def db_workload(self):
        """
        Gets the db_workload of this DedicatedShardedDatabase.
        Possible workload types.

        Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_workload of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this DedicatedShardedDatabase.
        Possible workload types.


        :param db_workload: The db_workload of this DedicatedShardedDatabase.
        :type: str
        """
        allowed_values = ["OLTP", "DW"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            db_workload = 'UNKNOWN_ENUM_VALUE'
        self._db_workload = db_workload

    @property
    def sharding_method(self):
        """
        **[Required]** Gets the sharding_method of this DedicatedShardedDatabase.
        Sharding Method.

        Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The sharding_method of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._sharding_method

    @sharding_method.setter
    def sharding_method(self, sharding_method):
        """
        Sets the sharding_method of this DedicatedShardedDatabase.
        Sharding Method.


        :param sharding_method: The sharding_method of this DedicatedShardedDatabase.
        :type: str
        """
        allowed_values = ["USER", "SYSTEM"]
        if not value_allowed_none_or_none_sentinel(sharding_method, allowed_values):
            sharding_method = 'UNKNOWN_ENUM_VALUE'
        self._sharding_method = sharding_method

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this DedicatedShardedDatabase.
        Oracle Database version number.


        :return: The db_version of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this DedicatedShardedDatabase.
        Oracle Database version number.


        :param db_version: The db_version of this DedicatedShardedDatabase.
        :type: str
        """
        self._db_version = db_version

    @property
    def listener_port(self):
        """
        Gets the listener_port of this DedicatedShardedDatabase.
        The GSM listener port number.


        :return: The listener_port of this DedicatedShardedDatabase.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        """
        Sets the listener_port of this DedicatedShardedDatabase.
        The GSM listener port number.


        :param listener_port: The listener_port of this DedicatedShardedDatabase.
        :type: int
        """
        self._listener_port = listener_port

    @property
    def listener_port_tls(self):
        """
        Gets the listener_port_tls of this DedicatedShardedDatabase.
        The TLS listener port number for sharded database.


        :return: The listener_port_tls of this DedicatedShardedDatabase.
        :rtype: int
        """
        return self._listener_port_tls

    @listener_port_tls.setter
    def listener_port_tls(self, listener_port_tls):
        """
        Sets the listener_port_tls of this DedicatedShardedDatabase.
        The TLS listener port number for sharded database.


        :param listener_port_tls: The listener_port_tls of this DedicatedShardedDatabase.
        :type: int
        """
        self._listener_port_tls = listener_port_tls

    @property
    def ons_port_local(self):
        """
        Gets the ons_port_local of this DedicatedShardedDatabase.
        Ons local port number.


        :return: The ons_port_local of this DedicatedShardedDatabase.
        :rtype: int
        """
        return self._ons_port_local

    @ons_port_local.setter
    def ons_port_local(self, ons_port_local):
        """
        Sets the ons_port_local of this DedicatedShardedDatabase.
        Ons local port number.


        :param ons_port_local: The ons_port_local of this DedicatedShardedDatabase.
        :type: int
        """
        self._ons_port_local = ons_port_local

    @property
    def ons_port_remote(self):
        """
        Gets the ons_port_remote of this DedicatedShardedDatabase.
        Ons remote port number.


        :return: The ons_port_remote of this DedicatedShardedDatabase.
        :rtype: int
        """
        return self._ons_port_remote

    @ons_port_remote.setter
    def ons_port_remote(self, ons_port_remote):
        """
        Sets the ons_port_remote of this DedicatedShardedDatabase.
        Ons remote port number.


        :param ons_port_remote: The ons_port_remote of this DedicatedShardedDatabase.
        :type: int
        """
        self._ons_port_remote = ons_port_remote

    @property
    def prefix(self):
        """
        **[Required]** Gets the prefix of this DedicatedShardedDatabase.
        Unique prefix for the sharded database.


        :return: The prefix of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this DedicatedShardedDatabase.
        Unique prefix for the sharded database.


        :param prefix: The prefix of this DedicatedShardedDatabase.
        :type: str
        """
        self._prefix = prefix

    @property
    def private_endpoint(self):
        """
        Gets the private_endpoint of this DedicatedShardedDatabase.
        The OCID of private endpoint being used by the sharded database.


        :return: The private_endpoint of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        """
        Sets the private_endpoint of this DedicatedShardedDatabase.
        The OCID of private endpoint being used by the sharded database.


        :param private_endpoint: The private_endpoint of this DedicatedShardedDatabase.
        :type: str
        """
        self._private_endpoint = private_endpoint

    @property
    def connection_strings(self):
        """
        Gets the connection_strings of this DedicatedShardedDatabase.

        :return: The connection_strings of this DedicatedShardedDatabase.
        :rtype: oci.globally_distributed_database.models.ConnectionString
        """
        return self._connection_strings

    @connection_strings.setter
    def connection_strings(self, connection_strings):
        """
        Sets the connection_strings of this DedicatedShardedDatabase.

        :param connection_strings: The connection_strings of this DedicatedShardedDatabase.
        :type: oci.globally_distributed_database.models.ConnectionString
        """
        self._connection_strings = connection_strings

    @property
    def time_zone(self):
        """
        Gets the time_zone of this DedicatedShardedDatabase.
        Timezone associated with the sharded database.


        :return: The time_zone of this DedicatedShardedDatabase.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this DedicatedShardedDatabase.
        Timezone associated with the sharded database.


        :param time_zone: The time_zone of this DedicatedShardedDatabase.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def gsms(self):
        """
        Gets the gsms of this DedicatedShardedDatabase.
        Details of GSM instances for the sharded database.


        :return: The gsms of this DedicatedShardedDatabase.
        :rtype: list[oci.globally_distributed_database.models.GsmDetails]
        """
        return self._gsms

    @gsms.setter
    def gsms(self, gsms):
        """
        Sets the gsms of this DedicatedShardedDatabase.
        Details of GSM instances for the sharded database.


        :param gsms: The gsms of this DedicatedShardedDatabase.
        :type: list[oci.globally_distributed_database.models.GsmDetails]
        """
        self._gsms = gsms

    @property
    def shard_details(self):
        """
        Gets the shard_details of this DedicatedShardedDatabase.
        Details of ATP-D based shards.


        :return: The shard_details of this DedicatedShardedDatabase.
        :rtype: list[oci.globally_distributed_database.models.DedicatedShardDetails]
        """
        return self._shard_details

    @shard_details.setter
    def shard_details(self, shard_details):
        """
        Sets the shard_details of this DedicatedShardedDatabase.
        Details of ATP-D based shards.


        :param shard_details: The shard_details of this DedicatedShardedDatabase.
        :type: list[oci.globally_distributed_database.models.DedicatedShardDetails]
        """
        self._shard_details = shard_details

    @property
    def catalog_details(self):
        """
        Gets the catalog_details of this DedicatedShardedDatabase.
        Details of ATP-D based catalogs.


        :return: The catalog_details of this DedicatedShardedDatabase.
        :rtype: list[oci.globally_distributed_database.models.DedicatedCatalogDetails]
        """
        return self._catalog_details

    @catalog_details.setter
    def catalog_details(self, catalog_details):
        """
        Sets the catalog_details of this DedicatedShardedDatabase.
        Details of ATP-D based catalogs.


        :param catalog_details: The catalog_details of this DedicatedShardedDatabase.
        :type: list[oci.globally_distributed_database.models.DedicatedCatalogDetails]
        """
        self._catalog_details = catalog_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
