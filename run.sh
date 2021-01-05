#!/bin/bash

clear

REPOSITORY=$1

if [ -z "$REPOSITORY" ]
then
    REPOSITORY=dtdemos
fi

IMAGE=dt-orders-selenium
VERSION_TAG=1
FULLIMAGE=$REPOSITORY/$IMAGE:$VERSION_TAG

echo ""
echo "========================================================"
echo "Running $FULLIMAGE"
echo "========================================================"
echo ""
echo "access app @ http://localhost"
echo ""
docker run -it \
    --env SCRIPT_NUM_LOOPS=1 \
    --env APP_URL=http://172.17.0.1 \
    $FULLIMAGE
