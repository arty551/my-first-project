import yfinance as yf

tickers = ["IVV", "SCHD", "GOOG", "MSFT", "AAPL", "AAXJ", "ITA", "SLV"]

for ticker in tickers:
    stock = yf.Ticker(ticker)
    price = stock.info.get("regularMarketPrice", "N/A")
    name = stock.info.get("shortName", ticker)
    print(f"{ticker:6} {name:30} ${price}")

