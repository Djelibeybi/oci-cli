# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.data_connectivity.src.oci_cli_network_validation.generated import networkvalidation_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci data-connectivity network-validation test-network-connectivity get-network-connectivity-status-collection -> oci data-connectivity network-validation test-network-connectivity get-status-collection
cli_util.rename_command(networkvalidation_cli, networkvalidation_cli.test_network_connectivity_group, networkvalidation_cli.get_network_connectivity_status_collection, "get-status-collection")
