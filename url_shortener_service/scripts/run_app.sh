#!/bin/bash

set -e

cd /src/app

uvicorn main:app --host "${APP_HOST}" --port "${APP_PORT}" --reload