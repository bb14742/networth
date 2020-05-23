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
        print("mysql db connection failed {}".format(error))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    '''
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection closed gracefully")
    '''


