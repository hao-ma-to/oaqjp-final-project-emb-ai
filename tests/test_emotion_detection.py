from EmotionDetection.emotion_detection import emotion_detector

def test_detect_emotion():
    assert emotion_detector("I am glad this happened") == "joy"
    assert emotion_detector("I am really mad about this") == "anger"
    assert emotion_detector("I feel disgusted just hearing about this") == "disgust"
    assert emotion_detector("I am so sad about this") == "sadness"
    assert emotion_detector("I am really afraid that this will happen") == "fear"
	
	