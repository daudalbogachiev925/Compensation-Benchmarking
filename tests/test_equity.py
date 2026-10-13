import pandas as pd
from src.equity import pay_gap_by_gender

def test_no_gap_when_equal():
    df = pd.DataFrame({
        "gender": ["M", "F", "M", "F"],
        "salary": [100, 100, 100, 100],
        "role": ["A"] * 4,
        "level": ["Junior"] * 4,
    })
    assert pay_gap_by_gender(df) == 0
