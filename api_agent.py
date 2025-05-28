import yfinance as yf

def get_asia_tech_allocation(tickers):
    data = {}
    for t in tickers:
        stock = yf.Ticker(t)
        hist = stock.history(period="2d")
        data[t] = hist['Close'].tolist()
    return data
