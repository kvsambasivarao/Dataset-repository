# SCAN-IDS Generator

A reproducible Python implementation for generating and evaluating a simulated
multi-class CAN intrusion-detection dataset.

## Repository structure

```text
scan-ids-generator/
├── LICENSE
├── README.md
├── requirements.txt
├── run.sh
├── data/
│   └── sample_scan_ids_1k.csv
└── src/
    ├── __init__.py
    ├── config.py
    ├── utils.py
    ├── generate_scan_ids.py
    └── evaluate.py
```

## Dataset taxonomy

The generator supports normal CAN traffic and nine representative attack
categories: DoS Attack, Fuzzy Attack, Replay Attack, RPM Spoofing, Gear
Spoofing, Brake Spoofing, Steering Spoofing, Speed Spoofing, and Sensor
Flooding.

Each frame contains timestamp, CAN ID, ECU category, DLC, eight data bytes,
binary label, attack/traffic flag, and severity.

## Severity

Severity is assigned operationally from the traffic/attack category:

| Category | Severity |
|---|---|
| Normal | Low |
| DoS Attack | Critical |
| Fuzzy Attack | Medium |
| Replay Attack | Medium |
| RPM Spoofing | High |
| Gear Spoofing | Critical |
| Brake Spoofing | Critical |
| Steering Spoofing | Critical |
| Speed Spoofing | High |
| Sensor Flooding | High |

## Generation

The generator uses a fixed seed for reproducibility. Normal frames use the
defined CAN-ID/ECU mapping and ECU payload baselines with bounded byte noise.
Attack generators implement the corresponding traffic and payload patterns.

Run the complete generator:

```bash
python3 -m src.generate_scan_ids --output data/scan_ids.csv
```

Generate a 1,000-frame preview:

```bash
python3 -m src.generate_scan_ids --output data/sample_scan_ids_1k.csv --sample
```

Run the baseline evaluation:

```bash
python3 -m src.evaluate --dataset data/scan_ids.csv
```

Or use:

```bash
bash run.sh
```

## Optional source-data support

`src/utils.py` includes a small loader for user-supplied CSV files. The core
generator does not require external datasets and can run independently.

## Reproducibility

The principal configuration is centralized in `src/config.py`, including:
- class taxonomy
- ECU categories
- CAN-ID mapping
- severity mapping
- frame counts
- payload baselines
- spoofing rules
- timing parameters
- random seed

## Research use

This software is intended for academic research, benchmarking, algorithm
development, and educational use. Users should validate models on independent
real-world or independently generated CAN traffic before drawing deployment
conclusions.

## Citation

Please cite the associated SCAN-IDS dataset/manuscript when using the dataset
or generator in academic work.


## Evaluation models

`src/evaluate.py` provides six model families for comparative experiments:

- Decision Tree
- Random Forest
- RBF Support Vector Machine
- Multilayer Perceptron (MLP)
- 1D Convolutional Neural Network (1D-CNN)
- Long Short-Term Memory network (LSTM)

The first four run with the packages in `requirements.txt`. The CNN and LSTM
require TensorFlow, which is intentionally optional because it is substantially
larger than the classical ML dependencies.

Classical evaluation:

```bash
python3 -m src.evaluate --dataset data/scan_ids.csv --sample 100000
```

Classical + deep-learning evaluation:

```bash
pip install tensorflow
python3 -m src.evaluate --dataset data/scan_ids.csv --sample 100000 --deep
```

Save results:

```bash
python3 -m src.evaluate --dataset data/scan_ids.csv --sample 100000 --deep \
  --output results.json
```

For fair comparisons, use the same input representation, train/test split,
random seed, and evaluation sample across all models. Results should be
reported with accuracy and macro-F1, and computational settings should be
reported with the experiment.
