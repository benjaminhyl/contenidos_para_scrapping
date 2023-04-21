import configparser


cfg_data = '''
[mysql]
host = localhost
user = user7
passwd = s$cret
db = ydb
'''

config = configparser.ConfigParser()
config.read_string(cfg_data)

print(config["mysql"]["host"])