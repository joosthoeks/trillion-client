#!/usr/bin/env python


import trillion-client
import json


def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    pub_key = ''
    sec_key = ''
    api = TrillionClient()
    api.set_credential(pub_key, sec_key)
    d(api.analytics_data_analytics_list(city='Eindhoven'))

if __name__ == '__main__':
    main()

