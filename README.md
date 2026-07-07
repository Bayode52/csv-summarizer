csv-summarizer

A Python script that reads any CSV file and prints a statistical summary of its numeric columns.

## What It Does
A Python script that reads any CSV file and prints: column names, total row count, and for every numeric column—sum, average, min, and max.

## Why I Built It
I wanted a quick way to understand the shape and numbers in a CSV without opening Excel or writing custom code each time.

## How to Run It
1. Clone this repo or download `csv_summarizer.py`
2. Replace `file_path` with the path to your CSV
3. Run: `python csv_summarizer.py`
4. Read the printed summary

## What I Learned
- **The csv module:** Python has built-in tools for structured data. No external libraries needed.
- **try/except:** Graceful error handling. Not every column is numeric, and that's okay.
- **enumerate():** Getting both index and value in a loop is clean and powerful.
- **Built-in functions:** `sum()`, `max()`, `min()`, `len()`—Python's toolbox is deep.
- **Automatic detection:** Writing logic that figures out which columns are numeric makes the script reusable on any CSV.
