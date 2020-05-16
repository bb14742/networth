
import stockquotes

if __name__ == '__main__':
    stock_quote = stockquotes.Stock('KR')
    print(f'stock_quote.current_price: {stock_quote.current_price}')

    print(f'len(stock_quote.historical): {len(stock_quote.historical)}, {type(len(stock_quote.historical))}')

    print(f'stock_quote.historical[0]: {stock_quote.historical[0]}')

    print(f'stock_quote.historical[0]["date"]: {stock_quote.historical[0]["date"]}')

    print(f'stock_quote.historical[0]["close"]: {stock_quote.historical[0]["close"]}')

    print(f'stock_quote.historical[97]["date"]: {stock_quote.historical[97]["date"]}')

    print(f'stock_quote.historical[97]["close"]: {stock_quote.historical[97]["close"]}')

    for i in range(0,len(stock_quote.historical)):
        stock_date = stock_quote.historical[i]["date"]
        stock_price_close = stock_quote.historical[i]["close"]
        print(f'{stock_date}, {stock_price_close}')