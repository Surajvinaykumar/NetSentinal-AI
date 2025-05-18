# NetSentinel AI – Network Anomaly Detection + AI Explanation

An end-to-end Python project that detects anomalies in network traffic using an **Isolation Forest** model and explains suspicious logs using a **Hugging Face LLM** (`zephyr-7b-beta`).

---

## Overview

NetSentinel AI is an AI-powered assistant that:

- Ingests and cleans the UNSW-NB15 dataset
- Flags suspicious traffic using an unsupervised ML model
- Generates human-friendly explanations for those logs using an LLM

---

## Key Features

- Cleans and preprocesses multi-part CSV log files
- Converts categorical network data to numerical
- Applies `MinMaxScaler` + `IsolationForest` for anomaly detection
- Connects to Hugging Face’s Zephyr model for AI explanations
- Outputs logs + insights in an easy-to-extend format

---

## Dataset

We use the publicly available [UNSW-NB15 dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset), split across 4 CSV files:

- `UNSW-NB15_1.csv`
- `UNSW-NB15_2.csv`
- `UNSW-NB15_3.csv`
- `UNSW-NB15_4.csv`

---

## 🛠️ Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/netsentinel-ai.git
cd netsentinel-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**Or manually:**

```bash
pip install pandas numpy scikit-learn requests
```

### 3. Download the dataset and place all 4 `.csv` files in your working directory.

link to the raw datasets --> https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset&ga=1
cleaned dataset --> valid_sample.csv

---

## Hugging Face Token Setup

1. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Create a token with **Read + Inference** access
3. Paste it in the script:

```python
hf_token = "hf_XXXXXXXXXXXXXXXXXXXXXXXX"
```

---

## Running the Project

```bash
python netsentinel.py
```

---

## What You’ll See

- Printed stats of your cleaned dataset
- Number of detected anomalies
- A suspicious log entry formatted as a prompt
- AI-generated explanation from Zephyr-7B

---

## Example LLM Prompt

```text
Explain this suspicious network log entry in simple terms:

proto: tcp
sport: 23910
dsport: 80
dur: 2.59
sbytes: 2082
dbytes: 268
state: FIN
```

---

## Example LLM Output

```text
This is a short TCP session where a large amount of data was sent to port 80 (HTTP) with minimal data received. This might suggest scanning, probing, or incomplete communication.
```

---

## Architecture

```text
[ Raw UNSW CSVs ]
        ↓
[ Data Cleaning + Encoding ]
        ↓
[ MinMaxScaler → Isolation Forest ]
        ↓
[ Anomalies Detected ]
        ↓
[ Prompt → Hugging Face Zephyr-7B ]
        ↓
[ Human-readable Explanation ]
```

---

## Output

- `valid_sample.csv` – a clean, numeric dataset used in the final ML pipeline
- Print logs + AI explanation printed directly to console

---

## Future Work

- ✅ Build a Streamlit frontend
- 🔊 Add voice command integration
- 📊 Integrate visual anomaly dashboards
- 🌐 Deploy as a web service

---

## Acknowledgements

- 📊 Dataset: [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset)
- 🧠 Model: [`zephyr-7b-beta`](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)
- ⚙️ Libraries: `pandas`, `scikit-learn`, `requests`

---

## License

MIT License

---

## Author

**Suraj Vinaykumar** – [LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/yourusername)

---

> Built to help you understand what your network is really doing — one anomaly at a time.
