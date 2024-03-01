#!/bin/bash
#Methods
curl -isX OPTIONS "$1" | grep "Allow:" | cut -d ':' -f2 | sed 's/^ *//'
