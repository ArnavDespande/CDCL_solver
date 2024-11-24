#!/bin/bash
if command -v python3 &>/dev/null; then
	python3 ad_DPLL.py
elif command -v python &>/dev/null; then
	python ad_DPLL.py
else
	exit 1
fi
