from configparser import ConfigParser

def parser(vendor):
    config = ConfigParser()
    config.read('api_keys.cfg')

    API_KEY = config.get(vendor, 'api_key')

    return API_KEY

def main():
    key = parser()

if __name__ == "__main__":
    main()