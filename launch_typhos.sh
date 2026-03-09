#!/usr/bin/bash


# shellcheck disable=SC1091
source /cds/group/pcds/pyps/conda/pcds_conda

export PYTHONPATH
PYTHONPATH="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

typhos --scrollable true tests.devices.AllPVs[]
