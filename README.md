# Project Title

This is an excersie for testing a webapp with selenium and python.
The project is written in POM achitecture

BaseProject
│
├── pages
│     ├── base_page.py
│     └── carbohydrate_calculator_page.py
│
├── tests
│     └── test_carbohydrate_calculator.py
│
├── conftest.py
├── requirements.txt
└── README.md

## Requirements
- Python 3.10 or higher

## Installation

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pytest -v