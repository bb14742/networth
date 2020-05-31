import config
import constants
import db
import sys
import stockquotes
from datetime import datetime


def get_db_creds():
    try:
        with open(constants.INVEST_DB_CREDS_FILE) as f:
            db_creds = f.readlines()
            db_creds = [x.strip() for x in db_creds]
    except Exception as error:
        print(f'Unexpected error in get_db_creds(): {error}')
        return []
    return db_creds


def get_db_connection(host, database, user, password):
    try:
        db_connection = db.get_db_connection(host, database, user, password)
    except:
        print("Unexpected error in update_stock_symbols():", sys.exc_info()[0])
        return -1
    return db_connection


def get_quotes(symbol):
    stock_quotes = stockquotes.Stock(symbol)
    quotes = []
    for s_quote_iter in range(0,len(stock_quotes.historical)):
        quote = []
        quote.append(stock_quotes.historical[s_quote_iter]["close"])
        quote.append(stock_quotes.historical[s_quote_iter]["date"].date().isoformat())
        quotes.append(quote)
    return quotes


def update_quotes():
    db_creds = get_db_creds()
    db_connection = get_db_connection(db_creds[0],db_creds[1],db_creds[2],db_creds[3])
    db_symbols_list = db.get_symbols_db(db_connection)
    for symbol in db_symbols_list:
        api_quotes = get_quotes(symbol)
        db_quotes = db.get_db_quotes(db_connection, symbol)
        db_quote_iter = 0
        for api_q in api_quotes:
            if db_quote_iter < len(db_quotes):
                if datetime.strptime(api_q[1], '%Y-%m-%d').date() > datetime.strptime(db_quotes[db_quote_iter][1], '%Y-%m-%d').date():
                    perform_api_insert = True
                else:
                    perform_api_insert = False
            else:
                perform_api_insert = True
            if perform_api_insert:
                db.insert_quote(db_connection, symbol, api_q[1], api_q[0])
            else:    
                db_quote_iter += 1
    db_connection.close()

if __name__ == '__main__':
    update_quotes()
