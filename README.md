# smart-healthcare-recommendation-system
Smart Healthcare Recommendation System is a machine learning project that predicts probable diseases from patient symptoms and provides disease descriptions with precautionary suggestions. Built using Python, Random Forest, data preprocessing, feature engineering, and Streamlit for an interactive healthcare web application.
## 📌 Project Overview
The Smart Healthcare Recommendation System is an end-to-end machine learning project that predicts probable diseases based on user symptoms and provides related disease descriptions and precautionary steps. The project combines healthcare datasets, data cleaning, feature engineering, machine learning, and Streamlit deployment to create an interactive healthcare recommendation web application.

## 🎯 Objectives
- Predict probable disease from selected symptoms
- Provide disease descriptions for better understanding
- Suggest precautionary measures based on predicted disease
- Build an end-to-end machine learning healthcare application
- Deploy the prediction system through a Streamlit web interface

## 🗂️ Dataset Files Used
This project uses the following datasets:
- [dataset.csv](https://github.com/user-attachments/files/29234331/dataset.csv) → Main disease and symptom dataset
- [symptom_Description.csv](https://github.com/user-attachments/files/29234381/symptom_Description.csv) → Disease descriptions
- [symptom_precaution.csv](https://github.com/user-attachments/files/29234382/symptom_precaution.csv) → Disease precaution suggestions
- [Symptom-severity.csv](https://github.com/user-attachments/files/29234383/Symptom-severity.csv) → Symptom severity weights

## 🛠️ Technologies Used
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Pickle**
- **Streamlit**

## ⚙️ Project Workflow

### 1. Data Collection
Loaded multiple healthcare datasets containing diseases, symptoms, descriptions, and precautions.

### 2. Data Cleaning
- Checked null values in all datasets
- Removed duplicate rows from the main dataset
- Filled missing values with `"None"`
- Standardized disease names for proper merging

### 3. Data Merging
Merged the main symptom dataset with:
- disease description dataset
- precaution dataset

This created a final healthcare lookup dataset for the web app.

### 4. Feature Engineering
Symptoms were converted into a machine-learning-friendly format using binary encoding:
- **1** = symptom present
- **0** = symptom absent

This created the symptom feature matrix for disease prediction.

### 5. Model Building
Used **Random Forest Classifier** to train the disease prediction model.

### 6. Model Export
Saved the following files using pickle:
- `treatment_rf_model.pkl`
- `symptom_features.pkl`
- `medical_lookup.pkl`

### 7. Web App Development
Built a **Streamlit web application** where users can:
- select symptoms from dropdown
- generate disease prediction
- view disease description
- view precautionary steps

## 🤖 Machine Learning Model
- **Model Used:** Random Forest Classifier
- **Task:** Multi-class disease prediction based on symptoms

## 🌐 Streamlit App Features
- Symptom selection dropdown
- Disease prediction from selected symptoms
- Disease description display
- Precaution recommendation display
- User-friendly healthcare interface

## 📊 Key Features
- End-to-end ML healthcare project
- Multiple dataset integration
- Data cleaning and preprocessing
- Symptom-based disease prediction
- Disease description and precautions lookup
- Streamlit deployment ready

## 📁 Project Structure
```bash
smart-healthcare-recommendation-system/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── dataset.csv
│   ├── symptom_Description.csv
│   ├── symptom_precaution.csv
│   └── Symptom-severity.csv
│
├── models/
│   ├── treatment_rf_model.pkl
│   ├── symptom_features.pkl
│   └── medical_lookup.pkl
│
├── notebook/
│   └── healthcare_project.ipynb
│
└── screenshots/
```
## Project Files

  Home_page.png
  <img width="1913" height="906" alt="Screenshot 2026-06-23 104055" src="https://github.com/user-attachments/assets/60adf07b-40fa-4952-aaf0-c5aa7345c5f1" />   -> 
prediction_output.png
  <img width="1907" height="747" alt="Screenshot 2026-06-23 104140" src="https://github.com/user-attachments/assets/587ae69b-bd75-4ffd-819f-6306c3a74a98" />
<img width="1870" height="753" alt="Screenshot 2026-06-23 104131" src="https://github.com/user-attachments/assets/7716ec4d-b5e0-4464-8015-452df1cd95ea" />
