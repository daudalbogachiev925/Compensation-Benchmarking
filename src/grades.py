GRADE_BANDS = {
    "Junior": (70000, 120000),
    "Middle": (120000, 180000),
    "Senior": (180000, 240000),
    "Lead": (240000, 300000),
    "Principal": (300000, 400000),
}

def in_band(salary, level):
    lo, hi = GRADE_BANDS[level]
    return lo <= salary <= hi

def out_of_band_ratio(df):
    df = df.copy()
    df["in_band"] = df.apply(lambda r: in_band(r["salary"], r["level"]), axis=1)
    return round((~df["in_band"]).mean() * 100, 2)
