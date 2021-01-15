#!/bin/bash

echo ""
echo "========================================================"
echo "Stopping Browser traffic container"
echo "========================================================"
echo ""

CONTAINER_ID=$(sudo docker ps --filter="label=dt-orders-browser" -q)

if [ -z "$CONTAINER_ID" ]
then
    echo "No container running"
else
    echo "Stopping container"
    docker stop $CONTAINER_ID
    
    echo "Removing continer"
    docker rm $CONTAINER_ID
fi
