def get_tradingview_iframe(symbol):
    return f'''
    <iframe src="https://s.tradingview.com/embed-widget/advanced-chart/?symbol={symbol}&interval=1&theme=dark&style=1&timezone=Asia/Seoul&studies=BB@tv-basicstudies,RSI@tv-basicstudies,MACD@tv-basicstudies,Volume@tv-basicstudies"
    width="100%" height="800" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
    '''
