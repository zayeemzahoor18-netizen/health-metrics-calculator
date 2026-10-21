# health-metrics-calculator
# 🩺 Health Metrics Calculator

A simple web-based **Health Metrics Calculator** developed using Python and Flask. This project helps users understand their basic health metrics by calculating Body Mass Index (BMI), estimating daily calorie requirements, and generating a daily diet plan with suggested food quantities.

## 📌 About the Project

Maintaining a healthy lifestyle requires understanding basic health measurements, daily calorie requirements, and food intake. Calculating these values manually can be confusing for beginners.

The Health Metrics Calculator provides a simple web interface where users can enter their details and receive calculated health metrics and diet suggestions.

## 🎯 Objectives

- Calculate Body Mass Index (BMI).
- Estimate daily calorie requirements.
- Provide calorie targets based on user details.
- Generate a daily diet plan with suggested food quantities.
- Present results through a simple and user-friendly web interface.
- Demonstrate Python programming and web development concepts.

## 🚀 Key Features

### ⚖️ 1. BMI Calculator
- Accepts relevant user measurements.
- Calculates BMI using height and weight.
- Displays the calculated result.

### 🔥 2. Calorie Calculator
- Estimates daily calorie requirements.
- Provides calorie targets based on the implemented calculation logic.

### 🥗 3. Daily Diet Plan
- Generates a suggested daily diet plan.
- Displays food items and recommended quantities.
- Helps users understand how a daily eating plan can be structured.

### 🌐 4. Web Interface
- User input form.
- Results page displaying calculated metrics.
- Flask-powered backend processing.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | Styling and layout |
| Jinja2 | Dynamic HTML templates through Flask |
| Git | Version control |
| GitHub | Source code hosting |

## 📂 Project Structure

```text
health-metrics-calculator/
│
├── app.py
├── web_app.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
https://github.com/zayeemzahoor18-netizen/health-metrics-calculator.git
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Navigate to the Project Folder

```bash
cd health-metrics-calculator
```

### 3. Install Dependencies

Make sure Python is installed, then run:

```bash
py -m pip install flask
```

### 4. Run the Application

If `web_app.py` is your main Flask application, run:

```bash
py web_app.py
```

### 5. Open in Your Browser

Visit:

```text
http://127.0.0.1:5000
```

Enter the required information and view your calculated health metrics and diet plan.

## 💡 How It Works

1. The user opens the web application.
2. The user enters the required personal measurements and other requested details.
3. Flask processes the submitted information using Python.
4. The application calculates BMI and estimated calorie requirements.
5. The results page displays the calculated metrics and diet suggestions.

## 🔮 Future Enhancements

- Save previous calculation results.
- Add user accounts and personalized profiles.
- Include more diet plan customization options.
- Add graphical health metrics visualization.
- Improve mobile responsiveness.
- Add downloadable health reports.

## 🎓 Project Information

- **Project Name:** Health Metrics Calculator
- **Project Type:** Python Web Development Project
- **Backend:** Python and Flask
- **Frontend:** HTML and CSS

## ❤️ Developed With

Made by zayeem zahoor

---

**Disclaimer:** This application provides estimated health metrics and general dietary suggestions for educational purposes. It is not a substitute for professional medical or nutritional advice.
