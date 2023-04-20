import configparser

parser = configparser.ConfigParser()
parser.read("logging.conf")
for sect in parser.sections():
   print('Section:', sect)
   for k,v in parser.items(sect):
      print(' {} = {}'.format(k,v))
   print()
