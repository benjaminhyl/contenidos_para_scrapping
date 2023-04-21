import configparser

config = configparser.ConfigParser()
config.read('db.ini')

users_dir = config['info']['users_dir']
name = config['info']['name']
home_dir = config['info']['home_dir']

print(f'Users directory: {users_dir}')
print(f'Name: {name}')
print(f'Home directory: {home_dir}')