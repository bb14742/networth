import mysql.connector
from mysql.connector import Error
import sys


def get_db_connection(db_host, db_db, db_id, db_pw):
    try:
        connection = mysql.connector.connect(host=db_host,
                                         database=db_db,
                                         user=db_id,
                                         password=db_pw)
        return connection

    except mysql.connector.Error as error:
        print(f'mysql db connection failed {error}')
        raise Exception
    except Exception as error:
        print(f'Unexpected error: {error}')
        raise
    

def get_symbols_db(db_connection):
    try:
        cursor = db_connection.cursor(prepared=True)
        sql_select_query = """SELECT symbol_nm from invest.symbols"""
        cursor.execute(sql_select_query)
        db_result = cursor.fetchall()
        cursor.close()
    except Exception as error:
        print(f'Unexpected error in get_symbols_db(): {error}')
        raise Exception
    symbols_list = []
    for symbol in db_result:
        symbols_list.append(symbol[0])
    return symbols_list


def get_db_quotes(db_connection, symbol):
    cursor = db_connection.cursor(prepared=True)
    sql_select_query = """ select q.symbol_id, q.price, q.stock_dt from invest.quotes q join invest.symbols s on (s.id = q.symbol_id) where s.symbol_nm = %s order by q.stock_dt desc"""
    query_tuple = (symbol,)
    cursor.execute(sql_select_query, query_tuple)
    db_result = cursor.fetchall()
    cursor.close()
    symbols_list = []
    for symbol in db_result:
        symbol_row = []
        symbol_row.append(symbol[1])
        symbol_row.append(symbol[2].isoformat())
        symbols_list.append(symbol_row)
    return symbols_list


def insert_quote(db_connection, symbol, quote_dt, quote_price):
    try:
        cursor = db_connection.cursor(prepared=True)
        sql_insert_query = """INSERT INTO invest.quotes
                       (symbol_id, price, stock_dt, created_dt) VALUES ((select id from invest.symbols where symbol_nm=%s),%s,%s,current_date())"""
        insert_tuple_1 = (symbol, quote_price, quote_dt)
        db_result = cursor.execute(sql_insert_query, insert_tuple_1)
        db_connection.commit()
        cursor.close()
    except Exception as error:
        print(f'Error in insert_quote(db_connection, symbol, quote_dt, quote_price): {error}')
        raise
    return