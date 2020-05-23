#sudo /usr/bin/mysql -u root -p

import config
import constants



if __name__ == '__main__':
    lst = config.read_config(constants.CONFIG_INI_SECTION_INVESTMENT, \
                constants.CONFIG_INI_INVESTMENT_KEY_STOCK_SYMBOLS)
    print(lst)