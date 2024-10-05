# Define a dictionary of exchange rates
exchange_rates = {
    'USD': 1.0,  # US Dollar
    'EUR': 0.84,  # Euro
    'GBP': 0.76,  # British Pound
    'JPY': 109.42,  # Japanese Yen
    'CNY': 6.93,  # Chinese Yuan
    'INR': 74.83,  # Indian Rupee
    # Add more currencies as needed
}

def convert_currency():
    # Get user input for amount and currency
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency (e.g. USD, EUR, GBP, INR): ").upper()

    # Check if the currency is valid
    if from_currency not in exchange_rates:
        print("Invalid currency. Please try again.")
        return

    # Get user input for the currency to convert to
    to_currency = input("Enter the currency to convert to (e.g. USD, EUR, GBP, INR): ").upper()

    # Check if the currency is valid
    if to_currency not in exchange_rates:
        print("Invalid currency. Please try again.")
        return

    # Convert the amount to the desired currency
    converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]

    # Print the result
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    convert_currency()