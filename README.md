<img src="logo.png" alt="MedNER-X Logo" width="100" align="left"/>

# MedNER-X
🚀 AI-powered Medical NLP for Named Entity Recognition (NER) & Classification.

---

## 📖 About the Project  
MedNER-X is a **cutting-edge AI-powered medical NLP system** designed for **Named Entity Recognition (NER)** and **medical text classification**.  
It leverages **BioBERT & ClinicalBERT** to extract and classify diseases, symptoms, and treatments from clinical text.  

---

## ⚡ Features  
✔ **Medical Named Entity Recognition (NER)** with **BioBERT**  
✔ **Medical Text Classification** with **ClinicalBERT**  
✔ **FastAPI-based REST API** for real-time inference  
✔ **DVC for Dataset Versioning** & **MLflow for Experiment Tracking**  
✔ **Scalable & Modular Codebase**  

---

## 📂 Project Structure  
```
MedNER-X/
│── mednerx/              # Custom Python module (NER & Classification)
│   ├── init.py
│   ├── nlp.py            # NER & Classification models
│   ├── preprocess.py     # Text cleaning functions
│   ├── data_loader.py    # Loads datasets
│   ├── utils.py          # Helper functions
│── data/                 # Datasets (Tracked with DVC)
│── models/               # Trained models
│── api/                  # FastAPI for inference
│── notebooks/            # Jupyter experiments
│── scripts/              # Utility scripts
│── setup.py              # Installable package config
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── dvc.yaml              # DVC pipeline config
│── mlflow/               # Experiment tracking

```
---

## 🛠 Installation  

