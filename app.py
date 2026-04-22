# Step 1: Import Libraries
from flask import Flask, render_template, request
from textblob import TextBlob

# Step 2: Initialize Flask App
app = Flask(__name__)

# Step 3: Create Routes
# Home route -> displays the initial form
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Predict route -> processes the input from the form
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        # Get the text entered by the user in the HTML form
        user_text = request.form.get('user_text', '')

        # Basic validation: If user submits empty text
        if not user_text.strip():
            return render_template('index.html', error="Please enter some text to analyze!")

        # Step 4: Sentiment Analysis Logic using TextBlob
        # TextBlob automatically handles multiple sentences and averages the scores
        blob = TextBlob(user_text)
        
        # Extract polarity and subjectivity, rounded to 2 decimal places for clean UI
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Step 5: Classification Logic & Bonus (Emojis)
        if polarity > 0:
            sentiment = "Positive"
            emoji = "😊"
        elif polarity < 0:
            sentiment = "Negative"
            emoji = "😞"
        else:
            sentiment = "Neutral"
            emoji = "😐"

        # Pass all calculated data back to the frontend
        return render_template('index.html', 
                               original_text=user_text,
                               sentiment=sentiment,
                               emoji=emoji,
                               polarity=polarity,
                               subjectivity=subjectivity)

if __name__ == '__main__':
    # debug=True automatically restarts the server when you make code changes
    app.run(debug=True)