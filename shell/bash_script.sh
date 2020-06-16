#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# What does the script do
#
# Arguments:
# -r [value], --required-arg [value], --required-arg=[value]
#    Describe the required argument
# -o [value], --optional-arg [value], --optional-arg=[value]
#    Describe the optional argument
# -f [value], --flag [value]
#    Describe the flag
# -h [value], --help [value]
#    Get help and exit
#
# Example:
# bash bash_script.sh --required-arg=value [-h] [--optional-arg=value] [--flag]
# -----------------------------------------------------------------------------


###
# Helper Functions and Setup
###


function log {
  echo "$(date +%c) $1: $2"
}


###
# Argument Parsing
###


# Create Variables, Set Defaults
REQUIRED_ARG=""
OPTIONAL_ARG=""
FLAG="false"


# Parse CLI Arguments
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        -r|--required-arg)
        REQUIRED_ARG="$2"
        shift
        shift
        ;;
        --required-arg=*)
        REQUIRED_ARG="${1#*=}"
        shift
        ;;
        -r|--optional-arg)
        OPTIONAL_ARG="$2"
        shift
        shift
        ;;
        --optional-arg=*)
        OPTIONAL_ARG="${1#*=}"
        shift
        ;;
        -f|--flag)
        FLAG=true
        shift
        ;;
        -h|--help)
        log "INFO" "bash bash_script.sh --required-arg=value [-h] [--optional-arg=value] [--flag]"
        exit 0
        ;;
        *)
        log "ERROR" "Invalid Argument: $1, exiting"
        exit 1
        ;;
    esac
done


###
# Argument Verification
###


# Verify Required Arg is Set
if [ -z "$REQUIRED_ARG" ]; then
    log "ERROR" "Required Arg is not set (--required-arg), exiting"
    exit 1
fi

# Check if flag is set, do something if that is the base
if [ "$FLAG" = "true" ]; then
    log "INFO" "--flag set"
else
    log "INFO" "--flag not set"
fi


###
# Execute Script
###


log "INFO" "REQUIRED_ARG: ${REQUIRED_ARG}"
log "INFO" "OPTIONAL_ARG: ${OPTIONAL_ARG}"
log "INFO" "FLAG: ${FLAG}"
