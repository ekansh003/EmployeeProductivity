# Employee Productivity Prediction

A machine learning-powered web application that predicts employee productivity based on workforce, production, and operational metrics.

The application uses a trained **XGBoost Regression model** to estimate productivity and classify the result into different productivity levels.

---

## Overview

Employee productivity can be influenced by several factors such as targeted productivity, overtime, incentives, workforce size, idle time, and production complexity.

This project provides a simple web interface where users can enter these parameters and receive an estimated productivity score.

### Productivity Levels

| Predicted Productivity | Level                |
| ---------------------- | -------------------- |
| ≤ 0.30                 | Averagely Productive |
| 0.30 – 0.80            | Medium Productive    |
| > 0.80                 | Highly Productive    |

> The prediction is a machine learning estimate and should not be treated as an absolute measurement of employee performance.

---

## Features

- Employee productivity prediction using XGBoost
- Continuous productivity score prediction
- Automatic productivity-level classification
- Categorical feature encoding
- Structured prediction form
- Clean and minimalistic user interface
- Responsive design
- Dedicated Home, About, Prediction, and Result pages
- Flask-based backend
- Native XGBoost model format
- Ready for cloud deployment

---

## Machine Learning

The model is trained using the **Garments Worker Productivity** dataset.

### Model

**XGBoost Regressor**

The model predicts the continuous `actual_productivity` value rather than directly predicting a productivity category.

### Input Features

The model uses the following 13 features:

1. Quarter
2. Department
3. Day
4. Team
5. Targeted Productivity
6. SMV
7. Over Time
8. Incentive
9. Idle Time
10. Idle Men
11. Number of Style Changes
12. Number of Workers
13. Month

### Model Evaluation

The retrained model was evaluated on a held-out test set.

| Metric |  Score |
| ------ | -----: |
| MAE    | 0.0754 |
| MSE    | 0.0150 |
| RMSE   | 0.1226 |
| R²     | 0.4795 |

---

## Tech Stack

### Backend

- Python
- Flask
- Gunicorn

### Machine Learning

- XGBoost
- Scikit-learn
- Pandas
- NumPy

### Frontend

- HTML
- CSS
- Jinja2

### Deployment

- Render

---

## Project Structure

```text
EmployeeProductivity/
│
├── Dataset/
│   └── garments_worker_productivity.csv
│
├── Flask/
│   ├── static/
│   │   ├── about.css
│   │   ├── home.css
│   │   ├── predict.css
│   │   ├── result.css
│   │   └── style.css
│   │
│   ├── templates/
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── predict.html
│   │   └── submit.html
│   │
│   ├── app.py
│   ├── productivity_model.json
│   ├── productivity_encoders.pkl
│   ├── requirements.txt
│   └── retrain_model.py
│
├── model making.ipynb
├── .gitignore
└── README.md
```

---

## How It Works

The application follows a simple prediction pipeline:

```text
User Input
    ↓
Categorical Encoding
    ↓
Feature Preparation
    ↓
XGBoost Regression Model
    ↓
Productivity Score
    ↓
Productivity Classification
```

The categorical inputs — Quarter, Department, and Day — are transformed using the saved encoders before being passed to the trained model.

The remaining numerical features are converted to their required data types and arranged in the exact feature order expected by the model.

---

## Running Locally

### 1. Clone the Repository

```bash
git clone <repository-url>
cd EmployeeProductivity/Flask
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## Model Files

The application uses two saved files:

```text
productivity_model.json
productivity_encoders.pkl
```

### `productivity_model.json`

Contains the trained XGBoost regression model.

### `productivity_encoders.pkl`

Contains the categorical encoders used to transform:

- Quarter
- Department
- Day

These files are loaded by the Flask application when it starts.

---

## Retraining the Model

The model can be retrained using:

```bash
python retrain_model.py
```

The script:

1. Loads the original dataset.
2. Preprocesses categorical features.
3. Creates the training and testing datasets.
4. Trains the XGBoost regression model.
5. Evaluates the model.
6. Saves the trained model.
7. Saves the categorical encoders.

The generated files are:

```text
productivity_model.json
productivity_encoders.pkl
```

---

## Deployment

The application is designed to run as a Flask Web Service.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

The application can be deployed on platforms such as **Render**.

---

## Dataset

The project uses the **Garments Worker Productivity** dataset containing production and workforce-related information.

The dataset includes variables related to:

- Production targets
- Workforce size
- Overtime
- Incentives
- Idle time
- Production complexity
- Department
- Workday information
- Actual productivity

---

## Example Prediction

For a given set of workforce and production parameters, the model may produce a result such as:

```text
Predicted Productivity: 0.759
Productivity Level: Medium Productive
```

The numerical score represents the model's estimated productivity value.

---

## Limitations

- The prediction depends on the quality and distribution of the training data.
- Model performance may vary for data that differs significantly from the original dataset.
- The model provides an estimate rather than a definitive measure of employee performance.
- Predictions should not be used as the sole basis for employment-related decisions.

---

## Author

### Ekansh Jaiswal

Computer Science Student  
Machine Learning & Full-Stack Development

**GitHub:** [@ekansh003](https://github.com/ekansh003)

---

## Disclaimer

This project is created for educational and demonstration purposes.

The productivity score generated by the model is an estimate based on the provided input features and should not be used as the sole basis for evaluating real-world employee performance.
