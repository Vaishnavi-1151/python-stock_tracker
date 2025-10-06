# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 320}

portfolio = {}
total_value = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("❌ Stock not available!")

# Calculate total value
for stock, qty in portfolio.items():
    total_value += stock_prices[stock] * qty

print("\n📈 Your Portfolio:", portfolio)
print("💰 Total Investment Value = $", total_value)

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Portfolio: {portfolio}\n")
    f.write(f"Total Investment Value = ${total_value}")

print("✅ Portfolio saved to portfolio.txt")
