#!/bin/bash

gunicorn --worker-tmp-dir /dev/shm -k uvicorn.workers.UvicornWorker app.main:app

RUN_PORT=${PORT:-8000}

/usr/local/bin/gunicorn --worker-tmp-dir /dev/shm -k uvicorn.workers.UvicornWorker app.main:app --bind "0.0.0.0:${PORT:-8000}"


