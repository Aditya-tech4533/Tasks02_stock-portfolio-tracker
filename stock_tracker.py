stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}

print("===== Stock Portfolio Tracker =====")
print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Take user input
while True:
    stock = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number.")

# Calculate total investment
print("\n===== Your Portfolio =====")

total_investment = 0

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(
        f"{stock}: {quantity} shares x "
        f"${price} = ${investment:,.2f}"
    )

print(f"\nTotal Investment: ${total_investment:,.2f}")

# Optionally save to a text file
save = input("\nSave portfolio to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("=======================\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(
                f"{stock}: {quantity} shares, "
                f"Price: ${price}, Investment: ${investment:.2f}\n"
            )

        file.write(
            f"\nTotal Investment: ${total_investment:.2f}\n"
        )

    print("Portfolio saved to portfolio.txt")

print("\nThank you for using the Stock Portfolio Tracker!")
