#!/usr/bin/env python3
"""
    Purpose:
        Do Something

    Steps:
        - Do Something

    Usage:
        execute_script.py [-h] --required-arg REQUIRED_ARG
                                 [--optional-arg OPTIONAL_ARG] [--optional-required]

        Example Script Template

        optional arguments:
          -h, --help            show this help message and exit

        Optional Arguments:
          --required-arg REQUIRED_ARG
                                Required Argument
          --optional-arg OPTIONAL_ARG
                                Optional Argument
          --optional-required   Flag to say optional argument is going to be required

    Example Call:
        python3 execute_script.py --required-arg=test
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
# N/A


###
# Main Execution
###


def main():
    """
    Purpose:
        Read an .avro File
    """
    logging.info("Starting Process")

    cli_args = get_cli_arguments()

    logging.info("Process Complete")


###
# Helper Functions
###


def get_cli_arguments():
    """
    Purpose:
        Parse CLI arguments for script
    Args:
        N/A
    Return:
        cli_arguments (ArgumentParser Obj): Parsed Arguments Object
    """
    logging.info("Getting and Parsing CLI Arguments")

    parser = ArgumentParser(description="Example Script Template")
    required = parser.add_argument_group("Required Arguments")
    optional = parser.add_argument_group("Optional Arguments")

    # Required Arguments
    optional.add_argument(
        "--required-arg",
        dest="required_arg",
        help="Required Argument",
        required=True,
        type=str,
    )

    # Optional Arguments
    optional.add_argument(
        "--optional-arg",
        dest="optional_arg",
        help="Optional Argument",
        required=False,
        default=None,
        type=str,
    )
    optional.add_argument(
        "--optional-required",
        dest="optional_required",
        required=False,
        action="store_true",
        help="Flag to say optional argument is going to be required",
    )


    # Compile/Parse Args
    parsed_args = parser.parse_args()

    # Manual Parsing ig Needed (Limitations in ArgParse)
    if parsed_args.optional_required:
        if not parsed_args.optional_arg:
            raise Exception("--optional-arg is required with --optional-required set")

    return parsed_args


###
# Execute Script
###


if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="[execute_script] %(asctime)s.%(msecs)03d %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        print(f"{os.path.basename(__file__)} failed due to error: {err}")
        raise err
