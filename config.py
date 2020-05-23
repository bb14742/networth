import configparser
import constants

def convert_comma_delim_string_to_list(st):
    return_list = []
    comma_loc = st.find(',')
    start_pos = 0
    while comma_loc > -1:
        return_list.append(st[start_pos:start_pos + comma_loc])
        start_pos = start_pos + comma_loc + 2
        comma_loc = st[start_pos:].find(',')
    return_list.append(st[start_pos:])
    return return_list


def read_config(section, key):
    config = configparser.ConfigParser()
    config.read('./config/invest.ini')
    return convert_comma_delim_string_to_list(config[section][key])


if __name__ == '__main__':
    read_config(constants.CONFIG_INI_SECTION_INVESTMENT, \
                constants.CONFIG_INI_INVESTMENT_KEY_STOCK_SYMBOLS)
