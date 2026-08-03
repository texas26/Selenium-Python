# Selenium Python Testing Project

This is an exercise for testing a webapp with Selenium and Python.
The project is written in POM (Page Object Model) architecture.

```
BaseProject
│
├── pages
│     ├── base_page.py
│     └── carbohydrate_calculator_page.py
│
│── constants
│     └── constants.py
│
├── tests
│     └── test_carbohydrate_calculator.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.9 or higher

## Installation

1. Create and activate virtual environment:
```bash
python3 -m venv .venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest -v
```