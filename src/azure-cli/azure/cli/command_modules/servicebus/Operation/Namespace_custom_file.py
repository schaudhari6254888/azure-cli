# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.cli.command_modules.servicebus.constants import *
def create_keyvault_object(col):
    vault_object={}
    if 'userAssignedIdentity' in col['identity']:
        vault_object['user_assigned_identity'] = col['identity']['userAssignedIdentity']

    vault_object.update({
        "key_name" : col['keyName'],
        "key_vault_uri" : col['keyVaultUri'],
        "key_version" : col['keyVersion']
    })
    return  vault_object
def create_servicebus_namespace(cmd, resource_group_name, namespace_name, location=None, tags=None, sku='Standard',
                           capacity=None, zone_redundant=None,  tier='Standard', mi_user_assigned=None, mi_system_assigned=None,
                           encryption_config=None, minimum_tls_version=None,disable_local_auth = None,alternate_name=None,
                           public_network_access=None, require_infrastructure_encryption=None):

    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Create
    user_assigned_identity = {}
    command_args_dict = {}
    type = "None"

    command_args_dict = {
        "resource_group": resource_group_name,
        "namespace_name": namespace_name,
        "tags": tags,
        "sku": {
            "name": sku,
            "capacity": capacity,
            "tier": sku
        },
        "minimum_tls_version": minimum_tls_version,
        "location": location,
        "zone_redundant": zone_redundant,
        "disable_local_auth": disable_local_auth,
        "alternate_name": alternate_name,
        "public_network_access": public_network_access
    }

    if mi_system_assigned:
        type = SYSTEM

    if mi_user_assigned:
        if mi_system_assigned:
            type = SYSTEMUSER
        else:
            type = USER
        for val in mi_user_assigned:
            user_assigned_identity[val] = {}
        command_args_dict.update({"identity": {
            "type": type,
            "user_assigned_identities": user_assigned_identity
        }})
    else:
        command_args_dict.update({
            "identity": {
                "type": type,
                "user_assigned_identities": None
            }
        })

    if encryption_config:
        command_args_dict.update({"encryption": {
            "key_vault_properties": encryption_config,
            "key_source": "Microsoft.KeyVault",
            "require_infrastructure_encryption": require_infrastructure_encryption
        }})

    return Create(cli_ctx=cmd.cli_ctx)(command_args=command_args_dict)
def cli_add_encryption(cmd, resource_group_name, namespace_name, encryption_config,require_infrastructure_encryption=None):
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Update
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Create
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Show

    servicebusnm = Show(cli_ctx=cmd.cli_ctx)(command_args={
        "resource_group": resource_group_name,
        "namespace_name": namespace_name
    })
    key_vault_object = []
    for col in encryption_config:
        key_vault_object.append(col)

    if 'encryption' in servicebusnm:
        for col in servicebusnm['encryption']['keyVaultProperties']:
            object = create_keyvault_object(col)
            if object not in key_vault_object:
                key_vault_object.append(object)
        if require_infrastructure_encryption is None:
            require_infrastructure_encryption = servicebusnm['encryption']['requireInfrastructureEncryption']

    return Update(cli_ctx=cmd.cli_ctx)(command_args={
        "resource_group": resource_group_name,
        "namespace_name": namespace_name,
        "encryption": {
            "key_source": "Microsoft.KeyVault",
            "key_vault_properties": key_vault_object,
            "require_infrastructure_encryption": require_infrastructure_encryption
        }
    })

def cli_remove_encryption(cmd,resource_group_name, namespace_name, encryption_config):
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Update
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Show
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Create

    servicebusnm = Show(cli_ctx=cmd.cli_ctx)(command_args={
        "resource_group": resource_group_name,
        "namespace_name": namespace_name
    })

    key_vault_object = []

    for col in servicebusnm['encryption']['keyVaultProperties']:
        object = create_keyvault_object(col)
        key_vault_object.append(object)
    for col in encryption_config:
        if col in key_vault_object:
            key_vault_object.remove(col)
    return Update(cli_ctx=cmd.cli_ctx)(command_args={
        "resource_group": resource_group_name,
        "namespace_name": namespace_name,
        "encryption": {
            "require_infrastructure_encryption": servicebusnm['encryption']['requireInfrastructureEncryption'],
            "key_vault_properties": key_vault_object,
            "key_source": "Microsoft.KeyVault"
        }
    })
def cli_add_identity(cmd, resource_group_name, namespace_name, system_assigned=None, user_assigned=None):
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Update
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Show
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Create

    servicebusnm = Show(cli_ctx=cmd.cli_ctx)(command_args={
        "resource_group": resource_group_name,
        "namespace_name": namespace_name
    })

    from azure.cli.core import CLIError
    if 'identity' not in servicebusnm:
        servicebusnm['identity'] = {
            "type": "None",
            "userAssignedIdentities": None
        }

    type = servicebusnm['identity']['type']
    if system_assigned:
        if type == USER:
            type = SYSTEMUSER
        elif type == "None":
            type = SYSTEM

    if user_assigned:
        if type == SYSTEM:
            type = SYSTEMUSER
        else:
            type = USER
        user_assigned_identity = {}
        for col in user_assigned:
            user_assigned_identity[col] = {}

        if 'userAssignedIdentities' in servicebusnm['identity']:
            if servicebusnm['identity']['userAssignedIdentities'] is None:
                servicebusnm['identity']['userAssignedIdentities'] = user_assigned_identity
            else:
                servicebusnm['identity']['userAssignedIdentities'].update(user_assigned_identity)
        else:
            servicebusnm['identity'] = {
                'userAssignedIdentities': user_assigned_identity,
                'type': type
            }
    return Update(cli_ctx=cmd.cli_ctx)(command_args={
        "resource_group": resource_group_name,
        "namespace_name": namespace_name,
        "identity": {
            "type": type,
            "user_assigned_identities": servicebusnm['identity']['userAssignedIdentities']
        }
    })


def cli_remove_identity(cmd, resource_group_name, namespace_name, system_assigned=None, user_assigned=None):
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Update
    from azure.cli.command_modules.servicebus.aaz.latest.servicebus.namespace import Show

    servicebusnm = Show(cli_ctx=cmd.cli_ctx)(command_args={
        "resource_group": resource_group_name,
        "namespace_name": namespace_name
    })

    if servicebusnm['identity'] is None:
        raise CLIError('The namespace does not have identity enabled')

    type = servicebusnm['identity']['type']
    if system_assigned:
        if type == SYSTEM:
            type = "None"
        if type == SYSTEMUSER:
            type = USER

    if user_assigned:
        if servicebusnm['identity']['userAssignedIdentities']:
            for x in user_assigned:
                servicebusnm['identity']['userAssignedIdentities'].pop(x)
            if type == USER:
                if len(servicebusnm['identity']['userAssignedIdentities']) == 0:
                    type = "None"
                    servicebusnm['identity']['userAssignedIdentities'] = None
            if type == SYSTEMUSER:
                if len(servicebusnm['identity']['userAssignedIdentities']) == 0:
                    type = "SystemAssigned"
                    servicebusnm['identity']['userAssignedIdentities'] = None

    command_args = {
        "resource_group": resource_group_name,
        "namespace_name": namespace_name,
        "identity": {
            "type": type
        }
    }

    if 'userAssignedIdentities' in servicebusnm['identity']:
        command_args["identity"].update({
            "user_assigned_identities": servicebusnm['identity']['userAssignedIdentities']
        })
    return Update(cli_ctx=cmd.cli_ctx)(command_args=command_args)