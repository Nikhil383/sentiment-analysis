#!/bin/bash
set -e

IMAGE=yourdocker/mlops-sentiment-flask-hf:latest

docker build -t $IMAGE -f src/Dockerfile .
docker push $IMAGE
