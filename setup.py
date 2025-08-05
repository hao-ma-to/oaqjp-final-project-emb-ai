from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1.0",
    packages=find_packages(),   # to find the package automatically 
    install_requires=["requests"],        # to add dependences, if any
    author="AP",
    description="Emotion Detection using IBM Watson",
)