# 🎓 Student Placement Predictor

A Machine Learning-powered web application that predicts student placement outcomes based on **CGPA** and **IQ** using a trained classification model.

The project integrates a Python-based machine learning model with a Flask REST API and an interactive web interface.

## 🚀 Features

- Predict student placement outcomes using CGPA and IQ.
- Interactive and responsive web interface.
- Real-time predictions through a Flask REST API.
- Integration of a serialized machine learning model (`model.pkl`).
- Simple and lightweight application architecture.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn, NumPy |
| Backend | Flask, Flask-CORS |
| Frontend | HTML, CSS, JavaScript |
| Model Serialization | Pickle |
| Version Control | Git, GitHub |

## 📁 Project Structure

```text
placement-predictor/
├── app.py
├── index.html
├── model.pkl
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Zylor07/placement-predictor.git
cd placement-predictor
```

### 2. Create a Virtual Environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask flask-cors numpy scikit-learn
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Visit:

`http://127.0.0.1:5000/`

## 🧠 How It Works

1. The user enters their CGPA and IQ.
2. JavaScript sends the input to the Flask backend.
3. Flask processes the input and passes it to the trained machine learning model.
4. The model generates a binary prediction.
5. The application displays the predicted placement outcome.

## 🔌 API Endpoint

**POST `/predict`**

Example request:

```json
{
  "cgpa": 8.5,
  "iq": 110
}
```

Example response:

```json
{
  "prediction": 1
}
```

**Prediction labels:**

- `1` — Predicted placement
- `0` — Predicted non-placement

## ⚠️ Limitations

The model uses only CGPA and IQ as input features. Real-world placement outcomes depend on additional factors, including technical skills, communication, interview performance, and job-market conditions.

Predictions should be treated as educational demonstrations rather than reliable assessments of an individual's employability.

## 🔮 Future Improvements

- Incorporate additional student features.
- Add model evaluation metrics and visualizations.
- Compare multiple classification algorithms.
- Deploy the application to a cloud platform.
- Improve error handling and input validation.

## 👨‍💻 Author

**Pritam Chakraborty**

GitHub: [@Zylor07](https://github.com/Zylor07)

---

⭐ If you find this project useful, consider starring the repository!
