#!/usr/bin/env bash

gunicorn app:app --daemon && python -m zlzl
