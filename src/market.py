def market_position(salary, p25, p50, p75):
    if salary < p25: return "Below P25"
    if salary < p50: return "P25-P50"
    if salary < p75: return "P50-P75"
    return "Above P75"

def compare_to_market(employees, market):
    merged = employees.merge(market, on=["role", "level"], how="left")
    merged["position"] = merged.apply(
        lambda r: market_position(r["salary"], r["p25"], r["p50"], r["p75"]), axis=1)
    merged["compa_ratio"] = merged["salary"] / merged["p50"]
    return merged
