import streamlit as st
from modules.chart_embed import get_tradingview_iframe
from modules.analysis import analyze_gold

st.set_page_config(page_title="📊 해외선물 골드 실시간 분석", layout="wide")
st.title("📊 해외선물 골드 실시간 분석")

st.subheader("📉 실시간 골드 차트")
st.components.v1.html(get_tradingview_iframe("TVC:GOLD"), height=800)

if st.button("🔍 현재 시점 분석하기"):
    result = analyze_gold()
    st.markdown("### 📘 분석 결과")
    st.markdown(result, unsafe_allow_html=True)
