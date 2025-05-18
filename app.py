import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

# --- Load full pipeline ---
with open("full_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

st.set_page_config(page_title="NetSentinel AI", layout="wide")
st.title("NetSentinel AI - Network Anomaly Detector")
st.markdown("## An AI-powered assistant that analyzes network traffic data")
st.markdown("### - by Suraj Vinaykumar")

uploaded_file = st.file_uploader("Upload preprocessed CSV", type=["csv"])

if uploaded_file:
    try:
        # Debug: check raw file size
        uploaded_file.seek(0)
        raw_bytes = uploaded_file.read()
        st.write(f"Uploaded file size: {len(raw_bytes)} bytes")

        # Reset pointer and read file
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file, header=None)

        if df.empty:
            st.error("Uploaded file is empty.")
            st.stop()

        st.success("File loaded successfully!")
        df.columns = [f"feature_{i}" for i in range(df.shape[1])]
        st.dataframe(df.head())

        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.fillna(0, inplace=True)

        # Predict anomalies
        preds = pipeline.predict(df)
        df["anomaly"] = preds

        st.success(f"🔍 Anomalies detected: {(preds == -1).sum()}")
        st.subheader("Anomalous Logs")
        st.dataframe(df[df["anomaly"] == -1].head(10))

        # --- Hugging Face LLM integration ---
        st.subheader("AI Explanation of a Suspicious Log")

        HF_TOKEN = st.secrets["hf_token"] if "hf_token" in st.secrets else st.text_input(" Enter your Hugging Face token", type="password")

        API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

        headers = {
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json"
        }

        def explain_log(log_row):
            prompt = "Explain this suspicious network log in simple terms:\n\n"
            for col, val in log_row.items():
                prompt += f"{col}: {val}\n"

            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 300,
                    "temperature": 0.7,
                    "do_sample": True
                }
            }

            response = requests.post(API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()[0]["generated_text"]
            else:
                return f"Error: {response.status_code}\n{response.text}"

        anomalies = df[df["anomaly"] == -1]
        if not anomalies.empty:
            selected_idx = st.selectbox("Select a row to explain", anomalies.index)
            if st.button("Explain this log"):
                explanation = explain_log(anomalies.loc[selected_idx])
                st.markdown("#### Explanation:")
                st.write(explanation)

    except Exception as e:
        st.error(f"ERROR WHILE PROCESSING!!: {e}")
else:
    st.info(" upload the cleaned Dataset.")
