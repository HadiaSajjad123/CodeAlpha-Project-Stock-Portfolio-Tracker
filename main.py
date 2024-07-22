
from portfolio import Portfolio


def main():
    portfolio = Portfolio()
    valid_tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN']
    user_choice=True
    while user_choice:
        print("\nMenu:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Show portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            print("Exiting the program...")
            user_choice=False
        else:
            print("Invalid choice. Please try again.")

main()
