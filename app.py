import streamlit as st
import plotly.express as px
from src.data import generate_market_data, generate_employees
from src.market import compare_to_market
from src.equity import pay_gap_by_gender, adjusted_pay_gap
from src.grades import out_of_band_ratio

st.title("💰 Compensation Benchmarking")

market = generate_market_data()
employees = generate_employees()

merged = compare_to_market(employees, market)

c1, c2, c3 = st.columns(3)
c1.metric("Pay Gap (raw)", f"{pay_gap_by_gender(employees)}%")
c2.metric("Pay Gap (adjusted)", f"{adjusted_pay_gap(employees)}%")
c3.metric("Out of Band", f"{out_of_band_ratio(employees)}%")

st.subheader("Позиционирование относительно рынка")
fig = px.histogram(merged, x="compa_ratio", color="level", nbins=30)
fig.add_vline(x=1.0, line_dash="dash", line_color="red")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Market Position Distribution")
st.bar_chart(merged["position"].value_counts())

st.subheader("Median salary по role/level")
pivot = merged.pivot_table(index="role", columns="level", values="salary", aggfunc="median")
st.dataframe(pivot.round(0))
