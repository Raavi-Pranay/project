# Rootkit Detection Using Stacked Machine Learning Ensembles

This project aims to enhance system security by detecting potential rootkits using a machine learning-based ensemble model. A Streamlit web application allows users to input system behavior data manually or via a file to detect rootkit presence.

## 📁 Project Structure

- `Rootkit (1).ipynb`: Jupyter Notebook for data processing, model training, and evaluation.
- `app.py`: Streamlit web application for user interaction and rootkit prediction.
- `test.py`: Script to list all the feature names used in the model.
- `model.pkl`: Trained machine learning model (must be placed in the project root).
- `sample_inputs/`: Folder containing sample input files for testing file-based predictions.

## 🚀 How to Run

### Prerequisites

- Python 3.7+
- Required packages: `streamlit`, `pandas`, `scikit-learn`, `pickle`

### Installation

```bash
pip install streamlit pandas scikit-learn
```
Start the Application
```bash
streamlit run app.py
```
## 🧠 How It Works
The model takes a set of binary features representing suspicious Android system behavior and predicts whether the behavior indicates the presence of a rootkit.

### Prediction Options:
#### 1. Upload a File:

Upload a .txt file with feature-value pairs (e.g., SEND_SMS 1.0).

The app parses and feeds the data to the trained model for prediction.

#### 2. Manual Selection:

Select suspicious behaviors from a multiselect widget.

The app constructs a feature vector and uses the model to predict rootkit presence.

## Features
A total of 183+ features derived from Android permissions, API calls, and system operations, such as:

`SEND_SMS`, `READ_PHONE_STATE`, `Runtime.exec`, `INTERNET`, `READ_SMS`

`CALL_PHONE`, `INSTALL_PACKAGES`, `System.loadLibrary`, etc.

See `test.py` or `app.py` for the complete list.

### 📊 Model
Stacked ensemble model trained using multiple base learners (defined in Rootkit (1).ipynb).

Model is saved as model.pkl and loaded in app.py.

### ⚠️ Note
Ensure model.pkl exists in the root directory before running the app.

Input files must be placed in the sample_inputs/ directory and formatted properly.

### 🛡️ Security Purpose
This tool is intended for research and educational use only. Unauthorized detection, surveillance, or classification of software without consent is discouraged.
