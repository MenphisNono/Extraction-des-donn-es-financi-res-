import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv('data/stock_data.csv')  # Sauvegarde des données
    return data

def plot_closing_price(data, ticker):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=data.index, y="Close", label="Close")
    plt.title(f'Prix de clôture pour {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Prix')
    plt.legend()
    plt.savefig('visuals/closing_price.png')
    plt.show()

def main():
    ticker = 'AAPL'  # Exemple pour Apple
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()

    # Extraction des données
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # Visualisation du prix de clôture
    plot_closing_price(stock_data, ticker)

if __name__ == "__main__":
    main()