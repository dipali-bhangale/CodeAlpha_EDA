# Exploratory Data Analysis (EDA) – Student Performance Factors

## Project Overview
This project performs Exploratory Data Analysis (EDA) on a student performance dataset to understand the relationship between students' study habits, attendance, and examination scores.

## Objective
- Understand the dataset and its structure.
- Identify and handle missing values.
- Analyze numerical variables using descriptive statistics.
- Examine correlations between student factors and exam scores.
- Create visualizations to identify patterns and relationships.
- Perform Pearson correlation tests.

## Dataset
- **Dataset name:** Student Performance Factors
- **Source:** Kaggle
- **Number of records:** 6,607
- **Number of columns:** 20
- **Target variable for analysis:** Exam_Score

## Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Visual Studio Code

## Analysis Performed
1. Dataset loading and inspection.
2. Missing-value analysis.
3. Duplicate-record detection.
4. Descriptive statistical analysis.
5. Study hours versus exam score analysis.
6. Attendance versus exam score analysis.
7. Correlation analysis.
8. Pearson correlation hypothesis testing.
9. Missing-value handling and data validation.
10. Exporting summary reports and visualizations.

## Key Findings
- The average exam score was approximately 67.24.
- Attendance had a positive correlation of approximately 0.581 with exam scores.
- Study hours had a positive correlation of approximately 0.445 with exam scores.
- The Pearson correlation tests indicated statistically significant relationships.
- The dataset initially contained 235 missing values, which were handled during cleaning.
- One record had an exam score of 101 and requires verification against the dataset documentation.

Correlation does not necessarily imply causation.

## Project Outputs
The `visualizations` folder contains:
- Exam score distribution chart
- Study hours versus exam scores chart
- Attendance versus exam scores chart
- Correlation heatmap
- Cleaned dataset
- `exam_score_correlations.csv`
- `missing_values_report.csv`

## How to Run the Project
1. Install Python.
2. Install the required libraries:

   `pip install pandas numpy matplotlib seaborn scipy`

3. Place the dataset in the expected `data` folder.
4. Run the script:

   `python eda_analysis.py`

## Conclusion
The analysis identified positive relationships between attendance, study hours, and examination performance. The visualizations and statistical results help summarize these patterns. Further analysis could investigate how other educational and personal factors relate to exam scores.