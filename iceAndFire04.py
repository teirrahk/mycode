#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def name_lookup(thrones_list):
    name = []
    for person in thrones_list:
        info = requests.get(person)
        decodedjson = info.json()
        name.append(decodedjson.get("name"))

    return name


def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        print("This character belongs to the following houses:")
        for person in name_lookup(got_dj.get("allegiances")):
            print (person)

        print("This character appears in the following books:")
        for person in name_lookup(got_dj.get("books")):
            print (person)

if __name__ == "__main__":
        main()

