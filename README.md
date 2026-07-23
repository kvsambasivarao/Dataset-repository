**Controlled Access Network (CAN) packets dataset for Intrusion Detection  with multi class labels**

**Dataset Availability and Description**

To facilitate reproducible research in automotive cybersecurity, the dataset developed in this study has been made publicly available through a GitHub repository. The repository contains a **research-grade simulated CAN bus dataset** that was developed by integrating insights from multiple publicly available CAN intrusion detection datasets and by incorporating representative attack scenarios reported in the literature.

Now available at : https://github.com/kvsambasivarao/Dataset-repository/commit/f274293fa9fc89b8e733a79d368f44fb00aa5293 

It is important to note that CAN identifiers (CAN IDs), message formats, and communication characteristics vary considerably across vehicle manufacturers and models. Consequently, a single real-world dataset cannot comprehensively represent all possible CAN traffic patterns. The proposed simulated dataset is therefore intended as a research and benchmarking resource that captures the structure, behavior, and characteristics of CAN communication under both normal and malicious operating conditions, rather than replicating the proprietary CAN database of any specific vehicle manufacturer.

The dataset includes normal CAN traffic together with **ten representative cyberattack categories** commonly investigated in automotive security research. In addition to attack labels, each CAN frame is annotated with a **four-level severity classification** (Low, Medium, High, and Critical), enabling both attack detection and attack severity assessment. This dual annotation supports the development and evaluation of machine learning and deep learning models for intrusion detection, attack classification, and cyber-risk prioritization in intelligent and autonomous vehicle networks.

The dataset is intended exclusively for academic research, benchmarking, algorithm development, and educational purposes. It provides a standardized platform for evaluating intrusion detection systems and facilitates comparative analysis across different machine learning approaches while promoting reproducible research in in-vehicle network security.
