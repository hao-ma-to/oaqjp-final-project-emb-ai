from flask import Flask, request, jsonify, Response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_api():
    data = request.get_json()
    
    if not data or "text" not in data:
        return Response("Missing 'text' in request", status=400, mimetype='text/plain')

    try:
        result = emotion_detector(data["text"])

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

    except Exception as e:
        return Response(f"Error: {str(e)}", status=500, mimetype='text/plain')

@app.route("/", methods=["GET"])
def home():
    return "Emotion Detection API is running."

if __name__ == "__main__":
    app.run(debug=True)
