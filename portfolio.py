import yfinance as yf

class Portfolio:
    def __init__(self):
        # Initialize an empty dictionary to hold stocks
        self.stocks = {}

    def add_stock(self, ticker, shares):
        # Add shares of a specified stock ticker to the portfolio
      """""""Adding shares of a specified stock ticker to the portfolio"""""""
      if ticker in self.stocks:
          self.stocks[ticker] += shares
      else:
          self.stocks[ticker] = shares
          print(f"Added {shares} shares of {ticker}")

    def remove_stock(self, ticker, shares):
        # Remove shares of a specified stock ticker from the portfolio
        if ticker in self.stocks:
            if self.stocks[ticker] >= shares:
                self.stocks[ticker] -= shares
                print(f"Removed {shares} shares of {ticker}")
                if self.stocks[ticker] == 0:
                    del self.stocks[ticker]
            else:
                print(f"Cannot remove {shares} shares of {ticker}. You only have {self.stocks[ticker]} shares.")
        else:
            print(f"{ticker} not found in portfolio")

    def get_stock_prices(self):
        # Fetch current stock prices for all tickers in the portfolio
        if not self.stocks:
            print("Portfolio is empty")
            return {}

        tickers = list(self.stocks.keys())
        stock_data = yf.download(tickers, period="1d", interval="1d")
        return stock_data['Adj Close'].iloc[-1]

    def calculate_portfolio_value(self):
        # Calculate the total value of the portfolio
        stock_prices = self.get_stock_prices()
        total_value = 0
        for ticker, shares in self.stocks.items():
            if ticker in stock_prices:
                total_value += shares * stock_prices[ticker]
        return total_value

    def show_portfolio(self):
        # Display the current portfolio with stock prices and total value
        if not self.stocks:
            print("Portfolio is empty")
            return

        stock_prices = self.get_stock_prices()
        print("\nCurrent Portfolio:")
        for ticker, shares in self.stocks.items():
            price = stock_prices.get(ticker, 'N/A')
            print(f"{ticker}: {shares} shares @ ${price:.2f} each")

        total_value = self.calculate_portfolio_value()
        print(f"\nTotal portfolio value: ${total_value:.2f}")

