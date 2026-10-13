import pandas as pd

def pay_gap_by_gender(df):
    medians = df.groupby("gender")["salary"].median()
    if len(medians) < 2:
        return 0
    max_sal = medians.max()
    min_sal = medians.min()
    return round((max_sal - min_sal) / max_sal * 100, 2)

def adjusted_pay_gap(df):
    """Одинаковые role+level — сравниваем gender."""
    grouped = df.groupby(["role", "level", "gender"])["salary"].median().reset_index()
    pivoted = grouped.pivot_table(index=["role","level"], columns="gender",
                                   values="salary").dropna()
    if "M" not in pivoted or "F" not in pivoted:
        return 0
    pivoted["gap"] = (pivoted["M"] - pivoted["F"]) / pivoted["M"]
    return round(pivoted["gap"].mean() * 100, 2)
