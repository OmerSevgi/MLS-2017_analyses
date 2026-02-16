# MLS Salaries Analysis

This project analyzes Major League Soccer (MLS) player salary data for the 2017 season. It reads salary information from a CSV file, performs calculations to identify highest and lowest paid players, and generates a detailed report for each team including total salary, average salary, and top/bottom earners.

## Features

- Reads MLS player salary data from `mls-salaries-2017.csv`.
- Identifies the highest and lowest paid players across the entire league.
- Calculates total and average salaries for each team.
- Identifies the highest and lowest paid players within each team.
- Generates a comprehensive text-based report (`mls-salaries.txt`) with all analysis results.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd mls_analys
    ```
2.  **Install dependencies:**
    This project requires `pandas` and `numpy`. You can install them using pip:
    ```bash
    pip install pandas numpy
    ```

## Usage

To run the analysis and generate the report, simply execute the `main.py` script:

```bash
python main.py
```

## Output

After running `main.py`, a file named `mls-salaries.txt` will be created or updated in the project directory. This file contains the full analysis report, including league-wide statistics and a detailed breakdown for each team.

## Data Source

The salary data is sourced from `mls-salaries-2017.csv`, which contains player information such as club, name, position, base salary, and guaranteed compensation for the 2017 MLS season.
