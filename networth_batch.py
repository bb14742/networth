#sudo /usr/bin/mysql -u root -p

import config
import constants
import db
import sys

def update_stock_symbols(host, database, user, password):
    lst = config.read_config(constants.CONFIG_INI_SECTION_INVESTMENT, \
                constants.CONFIG_INI_INVESTMENT_KEY_STOCK_SYMBOLS)
    print(lst)

    try:
        db_connection = db.get_db_connection(host, database, user, password)
        print("A database connection was created.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return

    symbols_list=db.get_symbols(db_connection)
    print(f'symbols: {symbols_list}')
    if ('db_connection' in locals()) and (db_connection.is_connected()):
        #if ('cursor' in locals()):
            #cursor.close()
        db_connection.close()
        print("MySQL connection closed gracefully")
    
    return

if __name__ == '__main__':
    with open('./db_creds.txt') as f:
        db_creds = f.readlines()
        db_creds = [x.strip() for x in db_creds]
    update_stock_symbols(db_creds[0],db_creds[1],db_creds[2],db_creds[3])

