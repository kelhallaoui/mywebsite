#!/bin/bash

cd /root/workspace/fast_api_http;
source env/bin/activate;
#uvicorn app.main:app --reload --host 137.184.26.165 --port 80
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

