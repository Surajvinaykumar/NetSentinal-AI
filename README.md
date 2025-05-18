#  NetSentinel AI – Network Anomaly Detection + AI Explanation

An end-to-end Python project that detects anomalies in network traffic using an **Isolation Forest** model and explains suspicious logs using a **Hugging Face LLM** (`zephyr-7b-beta`).

---

##  Overview

NetSentinel AI is an AI-powered assistant that:
-  Ingests and cleans the UNSW-NB15 dataset
-  Flags suspicious traffic using an unsupervised ML model
-  Generates human-friendly explanations for those logs using an LLM
---

<img width="1608" alt="Screenshot 2025-05-18 at 12 17 47 PM" src="https://github.com/user-attachments/assets/0034c455-feb4-4fa9-9699-83de572894f5" />



##  Key Features

- Cleans and preprocesses multi-part CSV log files
- Converts categorical network data to numerical
- Applies `MinMaxScaler` + `IsolationForest` for anomaly detection
- Connects to Hugging Face’s Zephyr model for AI explanations
- Outputs logs + insights in an easy-to-extend format

---

##  Dataset

We use the publicly available [UNSW-NB15 dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset), split across 4 CSV files:
- `UNSW-NB15_1.csv`
- `UNSW-NB15_2.csv`
- `UNSW-NB15_3.csv`
- `UNSW-NB15_4.csv`

---

##  Setup Instructions


### 1. Clone this repository

```bash
git clone https://github.com/yourusername/netsentinel-ai.git
cd netsentinel-ai



