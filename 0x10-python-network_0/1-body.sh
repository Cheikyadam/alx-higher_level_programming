#!/bin/bash
#Body
curl -siL "$1" | grep -q "HTTP/1.1 200 OK"  && curl -sL "$1"
