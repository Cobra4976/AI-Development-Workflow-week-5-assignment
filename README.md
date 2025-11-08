
### 📘 `README.md`

```markdown
# 🧠 Readmission Prediction API

This project implements a **machine learning model** that predicts whether a patient is likely to be readmitted to the hospital based on their medical information.  
It demonstrates a complete **AI Development Workflow** — from model training to deployment using **FastAPI**.

---

## 🚀 Project Overview

This project is part of the **AI Development Workflow** assignment.  
It includes the following major steps:

1. **Data Preprocessing and Model Training** – Using XGBoost and Scikit-learn.
2. **Model Saving** – Exporting the trained model using `joblib`.
3. **API Deployment** – Serving predictions through a FastAPI REST API.
4. **Testing and Validation** – Using Swagger UI and `curl` requests.

---

## 🧩 Project Structure

```

AI-Development-Workflow/
│
├── data/
│   └── hospital_readmissions.csv        # Example dataset (optional)
│
├── model/
│   └── readmission_model.pkl            # Trained ML model (generated after training)
│
├── Deployment/
│   ├── deployment_api.py                # FastAPI app
│   └── requirements.txt                 # Dependencies
│
├── training/
│   ├── train_model.py                   # Model training script
│   └── preprocess_data.py               # Optional: Data cleaning logic
│
├── README.md                            # Documentation (this file)
└── screenshots/
├── swagger_ui.png                   # [Insert Screenshot Here]
└── prediction_result.png            # [Insert Screenshot Here]

````

---

## 🛠️ Installation & Setup

### 1️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On macOS/Linux
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
fastapi
uvicorn
pandas
xgboost
scikit-learn
joblib
```

---

## 🧮 Model Training

Run the training script to train and save the model:

```bash
python training/train_model.py
```

This script:

* Loads the dataset
* Splits data into training and testing sets
* Trains an `XGBClassifier` model
* Saves the model as `readmission_model.pkl`

You should see:

```
✅ Model training complete. Model saved as readmission_model.pkl
```

---

## 🌐 Run the API Server

Start the FastAPI app using **Uvicorn**:

```bash
uvicorn deployment_api:app --reload
```

Expected output:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

Then open:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Example API Request (Swagger UI or cURL)

### JSON Input Example

```json
{
  "age": 65,
  "gender": "Male",
  "num_procedures": 2,
  "num_medications": 8,
  "time_in_hospital": 5,
  "has_diabetes": 1,
  "previous_visits": 2
}
```

### Example Output

```json
{
  "readmission_risk": 1
}
```

---

## 🧪 Test with cURL

You can test directly from your terminal:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 65,
  "gender": "Male",
  "num_procedures": 2,
  "num_medications": 8,
  "time_in_hospital": 5,
  "has_diabetes": 1,
  "previous_visits": 2
}'

## 📚 Learning Objectives

* Implement end-to-end AI model deployment using FastAPI
* Understand how to serve ML predictions via REST APIs
* Practice modular structuring of AI projects
* Gain hands-on experience with real-world MLOps workflow

---

## 👨‍💻 Author

**Name:** *[Brian Kiptoo]*
**Course:** AI Development Workflow
**Institution:** *[PLP]*


---

## 🏁 Conclusion

This project successfully demonstrates the **AI lifecycle** — from model creation to deployment.
The FastAPI interface allows quick integration and testing, making it a practical example of deploying machine learning in production.


