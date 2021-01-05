#!/bin/bash

clear

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

REPOSITORY=dtdemos
IMAGE=dt-orders-selenium
VERSION_TAG=1
FULLIMAGE=$REPOSITORY/$IMAGE:$VERSION_TAG

echo ""
echo "========================================================"
echo "Running $FULLIMAGE"
echo "APP_URL          : $APP_URL"
echo "SCRIPT_NUM_LOOPS : $SCRIPT_NUM_LOOPS"
echo "========================================================"
echo ""
docker run -it \
    --env APP_URL=$APP_URL \
    --env SCRIPT_NUM_LOOPS=$SCRIPT_NUM_LOOPS \
    $FULLIMAGE
