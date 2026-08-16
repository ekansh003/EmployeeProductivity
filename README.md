# 🚀 Employee Productivity Prediction Using Machine Learning

Welcome to the **Employee Productivity Prediction** project!  
This web application uses a trained XGBoost model to predict the productivity level of employees based on various input features like department, working hours, incentives, and more.

![Banner](Flask/static/banner.png)

---

## 📌 Table of Contents

- [🔍 Project Overview](#-project-overview)
- [📊 Features](#-features)
- [📁 Dataset](#-dataset)
- [⚙️ Tech Stack](#️-tech-stack)
- [🖥️ UI Screenshots](#️-ui-screenshots)
- [📦 Installation](#-installation)
- [🧠 Model Details](#-model-details)
- [📌 Future Improvements](#-future-improvements)
- [📃 License](#-license)

---

## 🔍 Project Overview

This project helps organizations **analyze and predict employee productivity** using machine learning.  
Businesses can enter key productivity metrics into a simple form and receive an estimate of whether the employee is:

- 🟡 Averagely Productive
- 🔵 Medium Productive
- 🟢 Highly Productive

---

## 📊 Features

- 🔮 Machine Learning-powered prediction using XGBoost
- 🌐 Interactive web interface built with Flask
- 📉 Classification into three productivity levels
- 🎨 Visually appealing UI with styled HTML/CSS
- 📦 Modular and clean project structure

---

## 📁 Dataset

The dataset was sourced from the **Garments Worker Productivity** dataset on Kaggle:  
📎 [Kaggle Dataset Link](https://www.kaggle.com/datasets/rameshreddyranam/garments-worker-productivity)

### Sample Features:
- `quarter`
- `department`
- `day`
- `team`
- `targeted_productivity`
- `smv`
- `over_time`
- `incentive`
- `idle_time`
- `idle_men`
- `no_of_style_change`
- `no_of_workers`
- `month`

---

## ⚙️ Tech Stack

| Layer       | Tools / Libraries                      |
|-------------|----------------------------------------|
| Frontend    | HTML, CSS                              |
| Backend     | Python, Flask                          |
| ML Model    | XGBoost (via scikit-learn)             |
| Utilities   | Pandas, Numpy, Pickle                  |

---

## 🖥️ UI Screenshots

### 🔸 Home Page
![Home](Flask/static/about.png)

### 🔸 Prediction Form
![Form](Flask/static/form.png)

### 🔸 Prediction Result
![Result](Flask/static/result.png)

---

## 📦 Installation

Follow these steps to set up the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Anandmall/Employee-Performance-Prediction.git
cd Employee-Performance-Prediction
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
```

- **Activate the environment:**

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

If a `requirements.txt` file is present:

```bash
pip install -r requirements.txt
```

Or manually install required packages:

```bash
pip install flask numpy pandas xgboost scikit-learn
```

### 4️⃣ Run the application

```bash
python app.py
```

Then open your browser and visit:  
👉 [http://localhost:5000](http://localhost:5000)

---

## 🧠 Model Details

- **Model Type:** XGBoost Regressor
- **Training Target:** `actual_productivity`
- **Classification Thresholds:**

| Prediction Value | Label                    |
|------------------|---------------------------|
| `<= 0.3`         | 🟡 Averagely Productive    |
| `0.3 - 0.8`      | 🔵 Medium Productive       |
| `> 0.8`          | 🟢 Highly Productive       |

- **Model File:** `gwp_xg.pkl`

---

## 📌 Future Improvements

- 📊 Add dashboard charts for visual analytics
- 🧠 Improve prediction logic with classification model
- ☁️ Deploy on Render or Streamlit Cloud
- 🗃️ Integrate database for logging predictions
- 📧 Email PDF reports to managers or HR
- 🗣️ Add voice input/output using Whisper + TTS

---

## 📃 License

This project is licensed under the **MIT License**.  
Feel free to use, share, or contribute.

---

## ⭐ Show Your Support

If you found this project helpful:

- 🌟 Star this repository
- 🍴 Fork and contribute
- 📣 Share with others

---

## 📬 Contact

Made with ❤️ by [Anand Kumar Mall](https://github.com/Anandmall)  
Have questions? Open an [Issue](https://github.com/Anandmall/Employee-Performance-Prediction/issues)
