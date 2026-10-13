import pandas as pd
import numpy as np

def generate_market_data(seed=42):
    np.random.seed(seed)
    levels = ["Junior", "Middle", "Senior", "Lead", "Principal"]
    roles = ["Backend", "Frontend", "Data", "DevOps", "QA", "Product"]
    market = []
    for r in roles:
        for l in levels:
            base = {"Junior": 80000, "Middle": 140000, "Senior": 200000,
                    "Lead": 260000, "Principal": 320000}[l]
            market.append({
                "role": r, "level": l,
                "p25": base * 0.9,
                "p50": base,
                "p75": base * 1.15,
                "p90": base * 1.3,
            })
    return pd.DataFrame(market)

def generate_employees(n=300, seed=42):
    np.random.seed(seed)
    return pd.DataFrame({
        "employee_id": [f"E{i:04d}" for i in range(n)],
        "role": np.random.choice(["Backend","Frontend","Data","DevOps","QA","Product"], n),
        "level": np.random.choice(["Junior","Middle","Senior","Lead","Principal"], n),
        "gender": np.random.choice(["M","F"], n, p=[0.6, 0.4]),
        "salary": np.random.normal(160000, 50000, n).round(0),
        "tenure_years": np.random.exponential(3, n).round(1),
    })
