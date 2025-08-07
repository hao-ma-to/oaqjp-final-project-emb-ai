"""
setup.py: Configuration script for packaging the emotion_detection library.
"""

from setuptools import setup, find_packages

setup(
    name="emotion-detection",
    version="0.1.0",
    packages=find_packages(), # to find the package automatically
    install_requires=["requests"], # to add dependences, if any
    author="hao-ma-to",
    description="Emotion Detection using IBM Watson",
)
