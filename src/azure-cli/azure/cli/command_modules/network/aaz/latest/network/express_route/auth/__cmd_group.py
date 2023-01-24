# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network express-route auth",
)
class __CMDGroup(AAZCommandGroup):
    """Manage authentication of an ExpressRoute circuit.

    To learn more about ExpressRoute circuit authentication visit https://docs.microsoft.com/azure/expressroute/howto-linkvnet-cli#connect-a-virtual-network-in-a-different-subscription-to-a-circuit.
    """
    pass


__all__ = ["__CMDGroup"]
