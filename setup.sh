#!/usr/bin/env bash
set -e

pip3 install --user virtualenv
python3 -m virtualenv -p python3.8 venv

./venv/bin/pip3 install -r requirements.txt
