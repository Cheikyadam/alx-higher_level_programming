#!/bin/bash
# Posting
email="test@gmail.com" subject="I will always be here for PLD" && curl -X POST -d "email=$email&subject=$subject" "$1"
