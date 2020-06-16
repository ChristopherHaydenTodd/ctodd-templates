#!/usr/bin/env python3
"""
    Purpose:
        Code for Parsing Both CLI and ENV Arugments and Merging Them
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser


###
# Scrpt Configuration Functions
###


def get_script_configuration():
    """
    Returns dictionary containing  variables needed for trainrunner and verifies that
    everything that needs to be set is set
    :return: dictionary containing environment variables needed for trainrunner to
        run experiments
    """

    cli_arguments = get_cli_arguments()

    possible_env_arguments = vars(cli_arguments).keys()
    env_arguments = get_env_arguments(possible_env_arguments)
    merged_arguments = merge_settings(env_arguments, cli_arguments)

    verify_arguments(merged_arguments)

    return merged_arguments


def merge_settings(settings_from_env, settings_from_cli):
    """
    Returns dictionary containing variables needed for trainrunner after merging
    values from the CLI and environemnt. CLI will take precidence as it is more
    direct
    :return: dictionary containing merged variables needed for trainrunner to
        run experiments
    """

    return {**settings_from_env, **settings_from_cli}


def verify_settings(settings):
    """

    Throws an exception if any environment variables needed for trainrunner
    are not specified. Otherwise returns dictionary containing these variables
    :return: dictionary containing environment variables needed for trainrunner to
             run experiments
    """

    missing_settings = []
    for setting in REQUIRED_SETTINGS:
        if setting not in settings.keys():
            missing_settings.append(setting)

    if missing_settings:
        error_msg = "Missing the following settings: {settings} - Exiting".format(
            settings=", ".join(missing_settings)
        )
        logging.error(error_msg)
        raise Exception(error_msg)


def get_cli_arguments():
    """
    Purpose:
        Parse CLI arguments for script
    Args:
        N/A
    Return:
        N/A
    """
    logging.info("Getting and Parsing CLI Arguments")

    parser = ArgumentParser(description="Describe the Script")
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Required Arguments\
    required.add_argument(
        "--required-argument",
        dest="required_argument",
        help="Help Info For The Arg",
        required=True,
    )

    # Optional Arguments
    optional.add_argument(
        "--optional-argument",
        dest="optional_argument",
        default=None,
        help="Help Info For The Arg",
        required=False
    )

    return parser.parse_args()


def get_env_arguments(possible_arguments):
    """
    Purpose:
        Parse ENV arguments for script. Will look at the os.environ for values matching
        the argument names from the CLI and return the values if they are set.

        Will ignore env variables not matching the CLI args
    Args:
        possible_arguments (List of Strings): Names of Possible args for the script.
            will look for corresponding env variable
    Return:
        N/A
    """

    env_arguments = {}
    for argument in possible_arguments:
        argument_value = os.environ.get(argument, None)
        if argument_value:
            env_arguments[argument] = argument_value

    return env_arguments



if __name__ == "__main__":
    get_script_configuration()
