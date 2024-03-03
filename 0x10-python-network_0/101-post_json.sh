#!/bin/bash
#file json post
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
