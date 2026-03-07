"""
This module provides a Flask application for emotion detection.

It includes routes to handle requests and return emotion analysis based on user input text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """
    Render the main index page from a HTML template.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion_response():
    """
    Handle requests to the emotionDetector endpoint.
    
    Extracts text from user query parameters, processes it through the emotion_detector function,
    and returns formatted emotional analysis or an error message if input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    emotions = ', '.join([f"'{key}': {value}" for key, value in response.items()
                          if key != 'dominant_emotion'])
    dominant_emotion = response.get('dominant_emotion', 'No dominant emotion detected')
    formatted_response = (f"For the given statement, the system response is {emotions}. "
                          f"The dominant emotion is {dominant_emotion}.")

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
