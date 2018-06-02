#!/usr/bin/env python


import trillion_client as tc
import json


def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    bearer_token = ''
    api = tc.TrillionClient()
    api.set_credential(bearer_token)
    d(api.analytics_data_analytics_list(city='Eindhoven'))

if __name__ == '__main__':
    main()

