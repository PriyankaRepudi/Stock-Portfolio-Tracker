import csv

# Example prices in USD; these are fixed sample values, not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 160.00,
    "AMZN": 190.00,
}


def get_positive_quantity():
    while True:
        raw_value = input("Enter quantity: ").strip()
        try:
            quantity = int(raw_value)
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
            return quantity
        except ValueError:
            print("Please enter a whole number, such as 3.")


def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and sample prices (USD):")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")

    portfolio = {}
    while True:
        symbol = input("\nEnter stock symbol (or DONE to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown symbol. Please choose one from the list.")
            continue

        quantity = get_positive_quantity()
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("No stocks were added.")
        return

    total_value = 0.0
    rows = []
    print("\n=== Portfolio Summary ===")
    print(f"{'Symbol':<10}{'Quantity':>10}{'Price':>14}{'Value':>14}")
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = quantity * price
        total_value += value
        rows.append([symbol, quantity, f"{price:.2f}", f"{value:.2f}"])
        print(f"{symbol:<10}{quantity:>10}{price:>14.2f}{value:>14.2f}")

    print("-" * 48)
    print(f"{'Total investment value:':<24} ${total_value:.2f}")

    save = input("\nSave summary to portfolio.csv? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Symbol", "Quantity", "Price_USD", "Value_USD"])
            writer.writerows(rows)
            writer.writerow(["TOTAL", "", "", f"{total_value:.2f}"])
        print("Saved portfolio.csv in the current folder.")


if __name__ == "__main__":
    main()
