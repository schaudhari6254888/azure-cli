# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=inconsistent-return-statements
# pylint: disable=protected-access
# pylint: disable=too-many-locals

import argparse


class AlertAddEncryption(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AlertAddEncryption, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        from azure.cli.core import CLIError
        from azure.cli.core.azclierror import InvalidArgumentValueError
        keyVaultObject = {}
        for (k, v) in (x.split('=', 1) for x in values):
            if k == 'key-name':
                keyVaultObject["key_name"] = v
            elif k == 'key-vault-uri':
                keyVaultObject["key_vault_uri"] = v
                if keyVaultObject["key_vault_uri"].endswith('/'):
                    keyVaultObject["key_vault_uri"] = keyVaultObject["key_vault_uri"][:-1]
            elif k == 'key-version':
                keyVaultObject["key_version"] = v
            elif k == 'user-assigned-identity':
                keyVaultObject["user_assigned_identity"] = {}
                keyVaultObject["user_assigned_identity"] = v
                if keyVaultObject["user_assigned_identity"].endswith('/'):
                    keyVaultObject["user_assigned_identity"] = keyVaultObject["user_assigned_identity"][:-1]
            else:
                raise InvalidArgumentValueError(
                    "Invalid Argument for:'{}' Only allowed arguments are 'key-name, key-vault-uri, key-version and user-assigned-identity'".format(
                        option_string))

        if (keyVaultObject["key_name"] is None) or (keyVaultObject["key_vault_uri"] is None):
            raise CLIError('key-name and key-vault-uri are mandatory properties')

        if "key_version" not in keyVaultObject:
            keyVaultObject["key_version"] = ''

        if "user_assigned_identity" not in keyVaultObject:
            keyVaultObject["user_assigned_identity"] = None
        return keyVaultObject


class ConstructPolicy(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(ConstructPolicy, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        from azure.cli.core import CLIError
        from azure.cli.core.azclierror import InvalidArgumentValueError
        from azure.cli.command_modules.eventhubs.constants import INCOMING_MESSAGES
        from azure.cli.command_modules.eventhubs.constants import INCOMING_BYTES
        from azure.cli.command_modules.eventhubs.constants import OUTGOING_BYTES
        from azure.cli.command_modules.eventhubs.constants import OUTGOING_MESSAGES

        throttling_policy = {}
        for (k, v) in (x.split('=', 1) for x in values):
            if k == 'name':
                throttling_policy["name"] = v

            elif k == 'rate-limit-threshold':
                if v.isdigit() is False:
                    raise CLIError('rate-limit-threshold should be an integer')
                throttling_policy["rate_limit_threshold"] = int(v)

            elif k == 'metric-id':
                if v.lower() == INCOMING_MESSAGES.lower():
                    throttling_policy["metric_id"] = INCOMING_MESSAGES
                elif v.lower() == INCOMING_BYTES.lower():
                    throttling_policy["metric_id"] = INCOMING_BYTES
                elif v.lower() == OUTGOING_MESSAGES.lower():
                    throttling_policy["metric_id"] = OUTGOING_MESSAGES
                elif v.lower() == OUTGOING_BYTES.lower():
                    throttling_policy["metric_id"] = OUTGOING_BYTES
                else:
                    raise CLIError('Only allowed values for metric_id are: {0}, {1}, {2}, {3}'.format(INCOMING_MESSAGES, INCOMING_BYTES, OUTGOING_MESSAGES, OUTGOING_BYTES))

            else:
                raise InvalidArgumentValueError("Invalid Argument for:'{}' Only allowed arguments are 'name, rate-limit-threshold and metric-id'".format(option_string))

        if (throttling_policy["name"] is None) or (throttling_policy["metric_id"] is None) or (throttling_policy["rate_limit_threshold"] is None):
            raise CLIError('One of the throttling policies is missing one of these parameters: name, metric-id, rate-limit-threshold')

        return throttling_policy


class ConstructPolicyName(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(ConstructPolicyName, self).__call__(parser, namespace, action, option_string)
    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        from azure.cli.core import CLIError
        from azure.cli.core.azclierror import InvalidArgumentValueError
        policy = {}
        for (k, v) in (x.split('=', 1) for x in values):
            print("hello")
            if k == 'name':
                policy["name"] = v
                print("helo")
            else:
                raise InvalidArgumentValueError(
                    "Invalid Argument for:'{}' Only allowed arguments are 'name' ".format(option_string))
        if policy["name"] is None:
            raise CLIError('Throttling policies is missing the parameters: name')

        return policy
