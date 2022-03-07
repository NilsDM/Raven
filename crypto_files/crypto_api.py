from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json
import pandas as pd
import time
import cfparser as cf


def cmc_pull():

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    # TODO: make this info private? 
    parameters = {
        'start':'1',
        'limit':'200',
        'convert':'USD'
        }

    key = cf.parser('coinmarketcap')

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
        }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        
        data = response.json()

        # TODO: timestamp?
        # export raw request
        today = time.strftime("%m-%d-%Y")
        path = './warehouse/'
        file_name = path + "crypto_raw" + today + ".json"
        with open(file_name, 'w', encoding = 'utf8') as outfile:
            json.dump(data, outfile, indent = 4)
        outfile.close()

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)   

    return data


def pre_process(data):

    column_names = ['symbol',
                    'id',
                    'quote'
                    ]

    df = pd.DataFrame(columns=column_names)

    for entry in data['data']:
        pullout = {'symbol': entry['symbol'],
                    'id' : entry['id'],
                    'quote': entry['quote']['USD']['price'] # note this is the latest average trade price across markets
                    }
        df.loc[len(df)] = pullout

    # TODO: timestamp?
    today = time.strftime("%m-%d-%Y")
    path = './warehouse/'
    file_name = path +  "crypto_pp" + today + ".csv"
    df.to_csv(file_name)   


def main():
    
    raw = cmc_pull()
    pre_process(raw)

    
if __name__ == '__main__':
    main()
