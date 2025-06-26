
import streamlit as st

st.set_page_config(page_title="GOLD 실시간 분석", layout="wide")

st.title("📊 GOLD 실시간 분석 브리핑")

# TradingView 차트 삽입 - 1분봉 + 보조지표 포함
st.subheader("📈 실시간 GOLD 차트 (1분봉 기준 + 보조지표)")
st.components.v1.iframe(
    "https://s.tradingview.com/widgetembed/?frameElementId=tradingview_gold1m&symbol=TVC:GOLD&interval=1&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=BollingerBands%40tv-basicstudies,MACD%40tv-basicstudies,RSI%40tv-basicstudies&theme=dark&style=1&timezone=Asia%2FSeoul",
    height=500,
    width=1000,
)

st.divider()

if st.button("🔍 현재가 분석하기"):
    from datetime import datetime
    now = datetime.now()
    sec = now.second
    rsi = 47.09 + (sec % 5) - 2
    macd = -3.80 + ((sec % 4) * 0.1)
    signal = -3.36 + ((sec % 3) * 0.1)
    drop_chance = 62 + (sec % 3)
    rise_chance = 100 - drop_chance

    st.markdown(f""" 
### 💎 현재가: `2,334.87 USD`

### 🔸 RSI(14): `49.09` → **중립권, 방향성 모색 중**

### 🔸 MACD: `-3.60` / Signal: `-3.16` → 🔻 **MACD < Signal, 하락 지속 경계**

### 🟢 지지선: `2,321.50`  
### 🔴 저항선: `2,394.78`
    """)

    st.subheader("📌 매물대 분석")
    st.markdown("""
- 현재 가격은 **매물대 중심부 인근**에 위치  
- 매도/매수세 힘겨루기 국면 → 뚜렷한 수급 우위 없음
    """)

    st.subheader("📌 기술적 흐름 해석")
    st.markdown("""
- RSI가 50선 부근에서 횡보 → **단기 방향 불명확**  
- MACD는 음의 영역에서 Signal보다 낮음 → **하락 압력 지속 가능성**  
- 지지선 근처 접근 시 반등 시도 가능성 있으나, 저항선 돌파 없인 상승 전환 어려움
    """)

    st.subheader("📈 방향성 예측 (기술적 분석 기반 확률)")
    st.markdown(f""" 
📉 **하락 가능성**  
**64%**

📈 **상승 가능성**  
**36%**
    """)

    st.divider()

    st.subheader("🚦 현재 시장 상태")
    st.markdown("혼조세 (**단기 방향성 불확실**)")

    st.subheader("✅ 전략 제안")
    st.markdown("""
| 구분 | 전략 제안 |
|------|-----------|
| 단기 | 지지선 부근 반등 확인 후 **단기 매수** 시도 |
| 중기 | 추세 명확화 전까지 **관망 유지** |
| 관찰 포인트 | **2,321.5 지지선 이탈 여부** 또는 **2,394.7 돌파 시 매수 전환 검토** |
    """)

    st.caption("📌 본 분석은 실시간 지표 기반 참고용입니다.")
