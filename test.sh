#!/bin/bash

set -eux -o pipefail

pycodestyle --ignore=E501 -- *.py
bashate -- *.sh
shellcheck -- *.sh

echo Success

