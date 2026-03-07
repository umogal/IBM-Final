import requests
import json
from requests.exceptions import SSLError

def get_emotion(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Parse the JSON resp into a dict
        response_json = response.json()
        # Return the dic
        return response_json
    except SSLError as e:
        return f"SSL Error: {e}"
    except requests.RequestException as e:
        return str(e)  # Return the exception message as a string

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check if the input is blank or just whitespace
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    # Existing code to process text and determine emotions
    response = get_emotion(text_to_analyze)  # Assuming this is a function call that returns emotion analysis data

    emotion_predictions = response.get("emotionPredictions")
    if emotion_predictions:
        first_prediction_emotions = emotion_predictions[0]['emotion']
        dominant_emotion = max(first_prediction_emotions, key=first_prediction_emotions.get) if first_prediction_emotions else None
        emotions = {key: first_prediction_emotions.get(key, None) for key in first_prediction_emotions}
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    else:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}


    