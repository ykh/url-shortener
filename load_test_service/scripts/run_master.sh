#!/bin/bash

set -e

cd /src

locust --master -f ./tests/url_shortener_test.py --host="${LOCUST_TARGET_HOST}"