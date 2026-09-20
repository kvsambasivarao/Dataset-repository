# Controlled Access Network (CAN) Packets Dataset for Intrusion Detection with Multi-Class Labels

## Dataset Availability and Description

To facilitate reproducible research in automotive cybersecurity, the dataset developed in this study has been made publicly available through a GitHub repository. The repository contains a **research-grade simulated CAN bus dataset** developed by integrating insights from multiple publicly available CAN intrusion detection datasets and incorporating representative attack scenarios reported in the literature.

### Dataset Repository

**GitHub Repository:**
https://github.com/kvsambasivarao/Dataset-repository

**Dataset File:**
`Multi Class - Labelled CAN Dataset for Car Hacking.zip`

The complete dataset is provided as a downloadable ZIP file in the repository. The repository is intended to provide convenient access to the dataset for academic research, benchmarking, algorithm development, and reproducibility.

## Dataset Characteristics

The dataset represents simulated CAN-bus communication containing both normal and malicious traffic. It is designed to provide a standardized environment for the development and evaluation of automotive intrusion detection systems.

The dataset contains:

* **500,000 CAN frames**
* **10 traffic/attack classes**, including normal traffic
* **4 severity levels:** Low, Medium, High, and Critical
* **11 ECU categories**
* CAN identifier (CAN ID)
* Timestamp
* DLC
* Eight CAN data bytes (`DATA0`–`DATA7`)
* Binary attack label
* Multi-class traffic/attack label
* Severity annotation

The dataset is intended to support both conventional machine-learning and deep-learning approaches for automotive cybersecurity research.

## Traffic and Attack Categories

The dataset contains normal CAN traffic and nine representative attack categories commonly investigated in automotive intrusion detection research.

| S. No. | Traffic / Attack Category |
| -----: | ------------------------- |
|      1 | Normal                    |
|      2 | DoS Attack                |
|      3 | Fuzzy Attack              |
|      4 | Replay Attack             |
|      5 | RPM Spoofing              |
|      6 | Gear Spoofing             |
|      7 | Brake Spoofing            |
|      8 | Steering Spoofing         |
|      9 | Speed Spoofing            |
|     10 | Sensor Flooding           |

The multi-class formulation enables researchers to investigate not only binary intrusion detection but also identification of the specific attack category.

## Severity Annotation

Each CAN frame is additionally annotated with a four-level operational severity classification:

| Severity | Description                                         |
| -------- | --------------------------------------------------- |
| Low      | Normal or low-impact traffic condition              |
| Medium   | Moderate security concern                           |
| High     | Significant security concern                        |
| Critical | Severe or potentially disruptive security condition |

The severity annotation enables experiments involving attack prioritization and severity-aware intrusion detection in addition to conventional attack classification.

## ECU Categories

The dataset includes the following ECU categories:

1. Engine
2. Transmission
3. ABS
4. ADAS
5. Steering
6. Body
7. Battery
8. Bus
9. Wheel
10. Airbag
11. Unknown

ECU attribution is provided as an additional metadata field to support research involving ECU-aware intrusion detection and analysis.

## CAN Frame Structure

Each record contains the following principal fields:

| Field        | Description                         |
| ------------ | ----------------------------------- |
| Timestamp    | Simulated CAN-frame timestamp       |
| CAN_ID       | CAN identifier                      |
| ECU          | Associated ECU category             |
| DLC          | Data length code                    |
| DATA0–DATA7  | Eight CAN payload bytes             |
| Binary_Label | Binary normal/attack indicator      |
| Flag         | Multi-class traffic/attack category |
| Severity     | Four-level severity annotation      |

The dataset uses eight data bytes per CAN frame, corresponding to the configured CAN frame representation used for the simulated traffic.

## Simulated CAN Communication

It is important to note that CAN identifiers, message formats, signal definitions, and communication characteristics vary considerably across vehicle manufacturers and vehicle models. Consequently, a single real-world dataset cannot comprehensively represent all possible CAN traffic patterns.

The proposed simulated dataset is therefore intended as a **research and benchmarking resource** that captures representative structures and behaviors of CAN communication under normal and malicious operating conditions. It does not claim to reproduce the proprietary CAN database or communication configuration of any particular vehicle manufacturer.

The dataset is consequently suitable for algorithm development and comparative experimentation while allowing researchers to work with a controlled and reproducible CAN traffic environment.

## Dataset Applications

The dataset can be used for research in areas including:

* CAN intrusion detection
* Binary intrusion detection
* Multi-class attack classification
* Attack-type identification
* Severity-aware intrusion detection
* Cyber-risk prioritization
* ECU-aware security analysis
* Machine-learning-based IDS
* Deep-learning-based IDS
* Automotive cybersecurity benchmarking
* Intelligent and autonomous vehicle security
* Comparative evaluation of intrusion detection algorithms

The dataset supports experimentation with classical machine-learning algorithms as well as deep-learning architectures.

## Reproducible Dataset Generation

A companion Python generator can be used to reproduce the configured simulated CAN traffic.

The generator project follows the structure:

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

The configuration file contains the principal dataset-generation parameters, including:

* traffic and attack taxonomy
* ECU categories
* CAN-ID mapping
* severity mapping
* frame counts
* payload configuration
* spoofing rules
* timing parameters
* random seed

A 1,000-frame sample is also provided for convenient inspection before downloading or generating the complete dataset.

## Model Evaluation

The companion evaluation program supports comparative experiments using:

* Decision Tree
* Random Forest
* RBF-SVM
* Multilayer Perceptron (MLP)
* 1D Convolutional Neural Network (1D-CNN)
* Long Short-Term Memory (LSTM)

Classical machine-learning models can be evaluated using the standard Python dependencies. The CNN and LSTM implementations require TensorFlow.

These evaluation facilities are provided to support reproducible comparison of different intrusion-detection approaches using a common dataset and feature representation.

## Reproducibility

The dataset and supporting resources are provided to encourage reproducible automotive cybersecurity research.

Researchers using the dataset are encouraged to report:

* Dataset version
* Number of samples used
* Feature representation
* Training/testing methodology
* Random seed
* Model architecture
* Hyperparameters
* Evaluation metrics
* Computational environment

This information facilitates meaningful comparison between different intrusion-detection studies.

## Intended Use

The dataset is intended exclusively for:

* Academic research
* Research benchmarking
* Algorithm development
* Machine-learning and deep-learning experimentation
* Educational purposes

It provides a standardized platform for evaluating intrusion detection systems and facilitates comparative analysis across different computational approaches in in-vehicle network security.

The dataset should not be interpreted as a substitute for validation using independent real-world automotive CAN traffic when assessing deployment readiness.

## Dataset Access

The complete dataset can be downloaded from:

**GitHub:**
https://github.com/kvsambasivarao/Dataset-repository

**Dataset ZIP:**
`Multi Class - Labelled CAN Dataset for Car Hacking.zip`

The GitHub repository currently provides the dataset ZIP together with this README documentation.

## Citation

Researchers using this dataset in publications, theses, reports, or other scholarly work are requested to cite the associated research publication describing the dataset and its methodology.

## License

The dataset and associated software should be used in accordance with the license and usage conditions provided with the repository.

## Disclaimer

This dataset is a simulated research resource. CAN communication behavior, identifiers, payloads, timing characteristics, and attack manifestations in production vehicles can differ substantially from the simulated environment.

Researchers should therefore consider the dataset as a controlled benchmarking environment and should use independent datasets or real-world CAN traffic when validating the generalization and practical applicability of an intrusion detection system.

---

**Repository:** https://github.com/kvsambasivarao/Dataset-repository
**Dataset:** `Multi Class - Labelled CAN Dataset for Car Hacking.zip`
