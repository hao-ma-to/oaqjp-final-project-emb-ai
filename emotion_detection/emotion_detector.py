"""
emotion_detector.py: Calls Watson Emotion API and returns emotion scores with blank-input handling.
"""

#import json
import requests

def emotion_detector(text_to_analyse):
    """
    Sends text to Watson EmotionPredict API and returns a dict 
    of emotion probabilities with the dominant emotion. 
    Returns None values for blank inputs.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers_to_use = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=payload, headers=headers_to_use, timeout=5)
    #process an empty line
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
         }
    response.raise_for_status() #automatically catch API errors after code 400
    result = response.json()
    emotions = result['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
