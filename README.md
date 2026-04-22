# 🎭 Sentiment Analysis Web Application

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask Version](https://img.shields.io/badge/Flask-3.0.0-lightgrey)
![TextBlob](https://img.shields.io/badge/NLP-TextBlob-success)

## 📌 Description
A full-stack Natural Language Processing (NLP) web application built with Python and Flask. This interactive tool allows users to input text (such as reviews, tweets, or general paragraphs) and instantly analyzes its emotional tone. It leverages the **TextBlob** library to calculate sentiment metrics, making it a great showcase of integrating machine learning concepts into a functional web interface.

## 🚀 Features
- **Real-Time Analysis:** Instantly processes and evaluates user text upon submission.
- **Detailed NLP Metrics:** - **Polarity:** Measures emotion on a scale of `-1.0` (Highly Negative) to `+1.0` (Highly Positive).
  - **Subjectivity:** Measures factual vs. opinionated text on a scale of `0.0` (Pure Fact) to `1.0` (Pure Opinion).
- **Dynamic User Interface:** Provides visual feedback, color-coded results, and dynamic emojis (😊 😐 😞) based on the detected sentiment.
- **Multi-Sentence Support:** Capable of analyzing complex paragraphs and averaging the sentiment scores automatically.
- **Responsive Design:** Clean, modern, and accessible CSS UI.

## 🛠️ Technologies Used
- **Backend:** Python, Flask
- **Machine Learning / NLP:** TextBlob
- **Frontend:** HTML5, CSS3, Jinja2 Templating
- **Environment Management:** Python `venv`

## 📁 Project Structure
```text
sentiment-analysis-app/
│
├── app.py                  # Main Flask application logic
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── static/                 
│   └── style.css           # UI Styling
│
└── templates/              
    └── index.html          # Frontend HTML and Jinja2 template
```

## 📸 Screenshots

### Dashboard
<img src="./screenshots/app_dashboard.png" width="700"/>

### Output
<img src="./screenshots/output.png" width="700"/>

## 💻 How to Run Locally
Follow these steps to set up and run the project on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2. Create a Virtual Environment
Keeping dependencies isolated is a Python best practice.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Browser
Navigate to http://127.0.0.1:5000/ in your web browser to use the app.

## 📊 Usage Example

**Input Text:**
```text
"I absolutely love the new Batman movie! The cinematography was stunning, though the runtime was a bit too long."
```

**App Output:**
```text
Sentiment: Positive 😊
Polarity: 0.35
Subjectivity: 0.58
```

## 🔮 Future Improvements
- **Advanced NLP Models:** Replace TextBlob with a Transformer-based model like VADER or HuggingFace BERT for highly nuanced context analysis (e.g., detecting sarcasm).
- **RESTful API:** Create an `/api/analyze` endpoint so other applications or mobile apps can consume the sentiment engine as a service.
- **Database Integration:** Implement SQLite or PostgreSQL to save historical user inputs and visualize sentiment trends over time using charts (e.g., Chart.js).
- **File Uploads:** Allow users to upload `.txt` or `.csv` files for bulk sentiment analysis.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License
This project is open-source and available under the MIT License.
