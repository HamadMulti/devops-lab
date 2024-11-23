from setuptools import setup, find_packages

setup(
    name="pipmanager",
    version="1.0.0",
    description="A Python library and CLI for managing pip packages.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Hamad",
    author_email="informhammadahmad@gmail.com",
    url="https://github.com/HamadMulti/devops-lab/pipmanager",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pipmanager=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
