# setup.py
from setuptools import setup, find_packages

setup(
    name="docx2md",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "mammoth",
        "markdownify",
    ],
    entry_points={
        "console_scripts": [
            "docx2md = docx2md.__main__:main",
        ],
    },
    author="ChatCRM Co.",
    author_email="ali.zareshahi@bizgpt.info",
    description="A tool to convert DOCX files to Markdown",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ChatCRM/docx2md",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
