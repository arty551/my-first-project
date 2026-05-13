import yfinance as yf
from datetime import datetime

# Your actual holdings
portfolio = ["IVV", "SCHD", "GOOG", "MSFT", "AAPL", "AAXJ", "ITA", "SLV"]

print(f"=== Portfolio Report: {datetime.now().strftime('%Y-%m-%d %H:%M')} ===\n")

for ticker in portfolio:
    stock = yf.Ticker(ticker)
    info = stock.info
    
    price = info.get("regularMarketPrice", 0)
    change_pct = info.get("regularMarketChangePercent", 0)
    
    # Arrow based on direction
    arrow = "▲" if change_pct > 0 else "▼"
    
    print(f"{ticker:6} ${price:>8.2f}  {arrow} {change_pct:+.2f}%")
    
    # Top headline for each
    news = stock.news
    if news:
        headline = news[0].get("content", {}).get("title", "")
        print(f"       └─ {headline[:70]}\n")
