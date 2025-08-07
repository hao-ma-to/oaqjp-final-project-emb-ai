"""
server.py: Flask application for emotion detection API.
"""
from flask import Flask, request, Response
from requests.exceptions import RequestException
from emotion_detection.emotion_detector import emotion_detector


app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_api():
    """Handle POST /emotionDetector: detect emotion for provided text."""
    data = request.get_json()
    if not data or "text" not in data:
        return Response("Missing 'text' in request", status=400, mimetype='text/plain')

    try:
        result = emotion_detector(data["text"])
    except RequestException as e:
        return Response(f"Error: {e}", status=500, mimetype='text/plain')
    if result["dominant_emotion"] is None:
        return Response("Invalid text! Please try again!", status=200, mimetype='text/plain')
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return Response(response_text, status=200, mimetype='text/plain')

@app.route("/", methods=["GET"])
def home():
    """Health check endpoint."""
    return "Emotion Detection API is running."

if __name__ == "__main__":
    app.run(debug=True)
