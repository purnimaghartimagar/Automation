import configparser
import os

def read_config_data(section, key):
    config = configparser.ConfigParser()
    
    # This line finds exactly where this script is located
    current_dir = os.path.dirname(__file__)
    
    # This line points to the config file relative to this script
    # Adjust "../Config.ini" to match where your file actually is
    file_path = os.path.join(current_dir, '../Configuration/Config.ini')
    
    config.read(file_path)
    return config.get(section, key)
