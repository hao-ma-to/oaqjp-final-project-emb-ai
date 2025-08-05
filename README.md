# 🧠 EmotionDetection

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-pytest-passing)

A simple Python package that detects the **dominant emotion** in a given text.

---

## 📦 Installation

Clone the repository and install in development mode:

```bash
git clone https://github.com/hao-ma-to/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
pip install -e .

Requires Python 3.8+

# 🧠 EmotionDetection

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-pytest-passing)

A simple Python package that detects the **dominant emotion** in a given text.

---

## 📦 Installation

Clone the repository and install in development mode:

```bash
git clone https://github.com/hao-ma-to/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
pip install -e .

    Requires Python 3.8+

🚀 Usage

from EmotionDetection.emotion_detection import emotion_detector

result = emotion_detector("I am really mad about this")
print(result)

📤 Output:

{
    'emotion': 'anger',
    'confidence': 0.92,
    'message': 'Detected strong negative emotion.'
}

🧪 Running Tests

To run all tests using pytest:

pytest

📁 Project Structure

EmotionDetection/
├── emotion_detection.py     # Main logic
├── __init__.py
tests/
├── test_emotion_detection.py
setup.py
README.md

⚖ License

This project is licensed under the MIT License.

🙋‍♂️ Author

hao-ma-to