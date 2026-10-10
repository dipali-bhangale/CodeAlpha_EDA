from pathlib import Path
import pandas as pd

# Project folders
BASE_DIR = Path("C:\\Users\\rbhan\\Desktop\\CodeAlpha_EDA\\data\\StudentPerformanceFactors.csv").resolve().parent
DATA_PATH = BASE_DIR / "StudentPerformanceFactors.csv"

# Load the dataset
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()


# 1. Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())
print("Total missing values:", df.isnull().sum().sum())

# 2. Check duplicate rows
print("\n--- Duplicate Rows ---")
print("Number of duplicate rows:", df.duplicated().sum())

# 3. Summary statistics
print("\n--- Numerical Summary ---")
print(df.describe())

# 4. Exam score distribution
print("\n--- Exam Score Analysis ---")
print(df["Exam_Score"].describe())
print("Average exam score:", df["Exam_Score"].mean())
print("Median exam score:", df["Exam_Score"].median())

# 5. Study hours and exam scores
print("\n--- Study Hours vs Exam Score ---")
print(
    df.groupby("Hours_Studied")["Exam_Score"]
    .mean()
    .round(2)
)

# 6. Attendance and exam scores
print("\n--- Attendance vs Exam Score ---")
print(
    df.groupby("Attendance")["Exam_Score"]
    .mean()
    .round(2)
)

# 7. Correlation between numerical variables
print("\n--- Correlation with Exam Score ---")
print(
    df.select_dtypes(include="number")
    .corr()["Exam_Score"]
    .sort_values(ascending=False)
)


import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create folder for graphs
OUTPUT_DIR = Path(__file__).resolve().parent / "visualizations"
OUTPUT_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Distribution of Exam Scores
plt.figure(figsize=(8, 5))
sns.histplot(df["Exam_Score"], bins=25, kde=True)
plt.title("Distribution of Student Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "exam_score_distribution.png")
plt.show()
plt.close()

# 2. Study Hours vs Exam Scores
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    scatter_kws={"alpha": 0.3}
)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "study_hours_vs_scores.png")
plt.show()
plt.close()

# 3. Attendance vs Exam Scores
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x="Attendance",
    y="Exam_Score",
    scatter_kws={"alpha": 0.3}
)
plt.title("Attendance vs Exam Scores")
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "attendance_vs_scores.png")
plt.show()
plt.close()

# 4. Correlation Heatmap
numeric_df = df.select_dtypes(include="number")
plt.figure(figsize=(10, 7))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap of Numerical Variables")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png")
plt.show()
plt.close()

print("\nAll visualizations saved in:", OUTPUT_DIR)


from scipy.stats import pearsonr

print("\n--- Hypothesis Testing ---")

tests = [
    ("Study Hours vs Exam Score", "Hours_Studied"),
    ("Attendance vs Exam Score", "Attendance")
]

for test_name, column in tests:
    r, p_value = pearsonr(df[column], df["Exam_Score"])

    print(f"\n{test_name}")
    print(f"Correlation coefficient: {r:.4f}")
    print(f"P-value: {p_value:.6g}")

    if p_value < 0.05:
        print("Result: Statistically significant relationship.")
    else:
        print("Result: Not statistically significant.")


# --- Data Cleaning and Validation ---

clean_df = df.copy()

print("\n--- Missing Values Before Cleaning ---")
print(clean_df.isnull().sum())

# Fill missing categorical values with each column's mode
categorical_columns = clean_df.select_dtypes(
    include=["object", "str", "category"]
).columns

for column in categorical_columns:
    if clean_df[column].isnull().any():
        mode_values = clean_df[column].mode()
        if not mode_values.empty:
            clean_df[column] = clean_df[column].fillna(
                mode_values.iloc[0]
            )

print("\n--- Missing Values After Cleaning ---")
print(clean_df.isnull().sum())
print("Total missing values:", clean_df.isnull().sum().sum())

# Investigate scores outside the expected 0–100 range
print("\n--- Exam Score Validation ---")
print("Scores below 0:", (clean_df["Exam_Score"] < 0).sum())
print("Scores above 100:", (clean_df["Exam_Score"] > 100).sum())

# Save the cleaned dataset
clean_df.to_csv(OUTPUT_DIR / "cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully.")


# Inspect the record with an exam score above 100
print("\n--- Record with Exam Score Above 100 ---")
print(df[df["Exam_Score"] > 100])

print("\n--- Record with Exam Score Above 100 ---")
print(df.loc[df["Exam_Score"] > 100].to_string())

print("\n--- Check Column Names ---")
print(df.columns.tolist())

print("\n--- Inspect the Record ---")
print(df.loc[1525].to_dict())

print("\n--- Check Score Above 100 ---")
print(df.loc[df["Exam_Score"] > 100, ["Gender", "Exam_Score"]])


# Save analysis summary tables
OUTPUT_DIR.mkdir(exist_ok=True)

correlation_table = (
    df.select_dtypes(include="number")
    .corr()["Exam_Score"]
    .sort_values(ascending=False)
    .rename("Correlation_with_Exam_Score")
)

correlation_table.to_csv(
    OUTPUT_DIR / "exam_score_correlations.csv"
)

missing_report = df.isnull().sum().rename("Missing_Values")
missing_report.to_csv(
    OUTPUT_DIR / "missing_values_report.csv"
)

print("\nCorrelation table and missing-value report saved.")
