#sudo /usr/bin/mysql -u root -p

import config
import constants
import db
import sys

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
        print("A database connection was created.")
    except:
        print("Unexpected error in update_stock_symbols():", sys.exc_info()[0])
        return -1
    return db_connection


if __name__ == '__main__':
    db_creds = get_db_creds()

