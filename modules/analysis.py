import random

def analyze_gold():
    # 시뮬레이션된 지표 수치
    rsi = round(random.uniform(30, 70), 2)
    macd = round(random.uniform(-4, 4), 2)
    signal = round(macd + random.uniform(-1.5, 1.5), 2)
    support = round(random.uniform(2300, 2350), 2)
    resistance = round(random.uniform(2380, 2430), 2)
    price = round(random.uniform(support + 5, resistance - 5), 2)

    # MACD 해석 및 예측
    if macd > signal and rsi > 55:
        trend = "🔵 **강세 흐름 예상** (MACD > Signal, RSI > 55)"
        entry = "🟢 **진입 전략**: 눌림목 매수 또는 저항 돌파 매수 전략 유효"
    elif macd < signal and rsi < 45:
        trend = "🔴 **약세 흐름 예상** (MACD < Signal, RSI < 45)"
        entry = "🔻 **진입 전략**: 지지 이탈 시 공략하거나 반등 저항매도 접근"
    else:
        trend = "⚪ **중립 흐름** (지표 혼조)"
        entry = "⏸ **전략**: 방향성 확인 후 진입, 단타/관망 병행"

    return f'''
📘 **GOLD 실시간 분석 리포트**

📌 **현재가**: {price:,.2f} USD  
📊 RSI: {rsi}  
📊 MACD: {macd}, Signal: {signal}  
🧱 **지지선**: {support:,.2f}  
🔺 **저항선**: {resistance:,.2f}  

{trend}  
{entry}
'''
