#!/bin/bash

APP_URL=$1
if [ -z "$APP_URL" ]
then
    APP_URL=http://172.17.0.1
fi

SCRIPT_NUM_LOOPS=$2
if [ -z "$SCRIPT_NUM_LOOPS" ]
then
    SCRIPT_NUM_LOOPS=10
fi

LOGGING_LEVEL=$3
if [ -z "$LOGGING_LEVEL" ]
then
    LOGGING_LEVEL=INFO
fi

REPOSITORY=dtdemos
IMAGE=dt-orders-browser
VERSION_TAG=1
FULLIMAGE=$REPOSITORY/$IMAGE:$VERSION_TAG

echo ""
echo "========================================================"
echo "Running $FULLIMAGE"
echo "APP_URL          : $APP_URL"
echo "SCRIPT_NUM_LOOPS : $SCRIPT_NUM_LOOPS"
echo "LOGGING_LEVEL    : $LOGGING_LEVEL"
echo "========================================================"
echo ""

echo "Running docker foreground mode"
docker run -it \
    --env APP_URL=$APP_URL \
    --env SCRIPT_NUM_LOOPS=$SCRIPT_NUM_LOOPS \
    --env LOGGING_LEVEL=$LOGGING_LEVEL \
    --label dt-orders-browser \
    $FULLIMAGE
