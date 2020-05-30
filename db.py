import mysql.connector
from mysql.connector import Error
import sys


def get_db_connection(db_host, db_db, db_id, db_pw):
    try:
        connection = mysql.connector.connect(host=db_host,
                                         database=db_db,
                                         user=db_id,
                                         password=db_pw)
        '''
        cursor = connection.cursor(prepared=True)
        sql_insert_query = """ INSERT INTO Employee
                           (id, Name, Joining_date, salary) VALUES (%s,%s,%s,%s)"""

        insert_tuple_1 = (1, "Json", "2019-03-23", 9000)
        insert_tuple_2 = (2, "Emma", "2019-05-19", 9500)

        cursor.execute(sql_insert_query, insert_tuple_1)
        cursor.execute(sql_insert_query, insert_tuple_2)
        connection.commit()
        print("Data inserted successfully into employee table using the prepared statement")
        '''
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

