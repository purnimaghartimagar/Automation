import os
from configparser import ConfigParser

# Get the path of the directory where ConfigReader.py is located
base_path = os.path.dirname(__file__)
# Go up one level or point to the exact location of your config file
config_file_path = os.path.join(base_path, '..', 'Configuration', 'config.ini') 

config = ConfigParser()
config.read(config_file_path)
