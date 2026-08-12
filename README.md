# Expense Tracker

Implementation of Project idea https://roadmap.sh/projects/expense-tracker on Roadmap.sh

A small command-line expense tracker written in Python. It provides a minimal interface for adding, validating, and listing expenses stored in a CSV file.

## What it does

- Stores expenses in `expenses.csv`.
- Provides simple commands to add and view expenses via `main.py`.
- Includes modules for parsing and validating input (`parsers.py`, `validators.py`).

## Features

- Add an expense with a description and amount.
- Validate input values and formats.
- Persist expenses to CSV for simple record-keeping.

## Installation

1. Create and activate a Python virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\Activate.ps1
```

2. Install dependencies (if any) listed in `req.txt`:

```bash
pip install -r req.txt
```

## Usage

- Add an expense (example):

```bash
python main.py add --description "Dinner" --amount 534
```

- List expenses (if the CLI supports it):

```bash
python main.py list
```

