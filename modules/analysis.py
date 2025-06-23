import random

def analyze_gold():
    # 시뮬레이션된 지표 수치
    rsi = round(random.uniform(30, 70), 2)
    macd = round(random.uniform(-4, 4), 2)
    signal = round(macd + random.uniform(-1.5, 1.5), 2)
    support = round(random.uniform(2300, 2350), 2)
    resistance = round(random.uniform(2380, 2430), 2)
    price = round(random.uniform(support + 5, resistance - 5), 2)

    # RSI 해석
    if rsi >= 70:
        rsi_trend = "🔴 과매수 구간 – 조정 가능성 있음"
    elif rsi >= 55:
        rsi_trend = "🟢 중기 강세 흐름 – 추세 유지"
    elif rsi >= 45:
        rsi_trend = "⚪ 중립권 – 방향 모색 중"
    elif rsi >= 30:
        rsi_trend = "🔵 약세 흐름 – 반등 준비 가능성"
    else:
        rsi_trend = "🔻 과매도 – 단기 반등 가능"

    # MACD 해석
    if macd > signal:
        macd_trend = "🟢 MACD > Signal → 단기 상승 모멘텀"
    elif macd < signal:
        macd_trend = "🔻 MACD < Signal → 하락 지속 경계"
    else:
        macd_trend = "⚪ MACD = Signal → 횡보 가능성"

    # 추세 판단
    if macd > signal and rsi > 55:
        trend = "📈 상승 흐름 유력"
        entry = "🟩 진입 전략: 눌림목 매수 or 저항 돌파 매수 유효"
    elif macd < signal and rsi < 45:
        trend = "📉 하락 흐름 우세"
        entry = "🟥 진입 전략: 반등 저항매도 or 지지 이탈 매도"
    else:
        trend = "📊 혼조세 (단기 방향성 불확실)"
        entry = "⏸ 전략: 방향 확인 후 단타 또는 관망"

    return f'''
📘 **GOLD 실시간 분석 리포트**

📌 **현재가**: {price:,.2f} USD  
📊 **RSI**: {rsi} → {rsi_trend}  
📊 **MACD**: {macd}, Signal: {signal} → {macd_trend}  
🧱 **지지선**: {support:,.2f}  
🔺 **저항선**: {resistance:,.2f}  

{trend}  
{entry}
'''
