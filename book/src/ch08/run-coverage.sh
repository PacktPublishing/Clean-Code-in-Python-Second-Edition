#!/bin/bash

PYTHONPATH=src pytest \
    --cov-report term-missing \
    --cov=coverage_1 \
    tests/test_coverage_1.py
