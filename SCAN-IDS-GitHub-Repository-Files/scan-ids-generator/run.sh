#!/usr/bin/env bash
set -e
python3 -m pip install -r requirements.txt
python3 -m src.generate_scan_ids --output data/scan_ids.csv
python3 -m src.evaluate --dataset data/scan_ids.csv --sample 100000
echo
echo "For CNN + LSTM evaluation, install TensorFlow and run:"
echo "python3 -m src.evaluate --dataset data/scan_ids.csv --sample 100000 --deep"
