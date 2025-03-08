from setuptools import setup, find_packages
import os
import sys

# Add the project root to the Python path so that packages can be found
sys.path.insert(0, os.path.abspath('.'))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="clearvoice",
    version="0.1.0",
    author="Speech Lab, Institute for Intelligent Computing, Alibaba Group",
    author_email="shengkui.zhao@alibaba-inc.com, zexu.pan@alibaba-inc.com",
    description="An open-source, AI-powered speech processing toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/modelscope/ClearerVoice-Studio",
    packages=find_packages(include=['clearvoice', 'clearvoice.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy==1.26.4",
        "torch>=2.0.1",
        "pesq==0.0.4",
        "pystoi>=0.3.3",
        "scipy>=1.10.1",
        "soundfile>=0.12.1",
        "torchaudio>=2.0.1",
        "yamlargparse>=1.31.1",
        "torchinfo>=1.8.0",
        "tqdm>=4.67.0",
        "pyyaml",
        "pysptk",
        "pymcd",
        "pyworld",
        "fastdtw",
        "museval",
        "resampy",
        "onnxruntime",
        "gammatone",
        "librosa==0.10.2.post1",
        "opencv-python>=4.10.0.84",
        "mir_eval==0.7",
        "numpy>=1.24.3",
        "tensorboard>=2.14.0",
        "torch-complex>=0.4.4",
        "rotary-embedding-torch>=0.8.3",
        "python_speech_features>=0.6",
        "typeguard>=4.3.0",
        "scenedetect",
        "torchvision",
        "huggingface-hub>=0.26.2",
        "gdown>=5.2.0",
        "pydub",
    ],
    include_package_data=True,
)