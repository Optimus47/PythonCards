import configparser

config = configparser.ConfigParser()
config.read('config.ini')

print(config)
print(config.sections())               # ['DEFAULT', 'database']
print(config['DEFAULT']['debug'])        # "true"
print(config['database']['host'])        # "localhost"
