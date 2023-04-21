import configparser

config = configparser.ConfigParser()

config.add_section('mysql')

config['mysql']['host'] = 'localhost'
config['mysql']['user'] = 'user7'
config['mysql']['passwd'] = 's$cret'
config['mysql']['db'] = 'ydb'

with open('db3.ini', 'w') as configfile:
    config.write(configfile)
