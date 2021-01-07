#!/bin/bash

clear

REPOSITORY=$1

if [ -z "$REPOSITORY" ]
then
    REPOSITORY=dtdemos
fi

IMAGE=dt-orders-browser
VERSION_TAG=1
FULLIMAGE=$REPOSITORY/$IMAGE:$VERSION_TAG

echo "Building: $FULLIMAGE"
docker build -t $FULLIMAGE .

echo ""
echo "========================================================"
echo "Ready to push $FULLIMAGE ?"
echo "========================================================"
read -rsp "Press ctrl-c to abort. Press any key to continue"

docker push $FULLIMAGE
