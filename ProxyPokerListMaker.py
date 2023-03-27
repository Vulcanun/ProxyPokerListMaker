#!/usr/bin/python3

import csv
import sys
from pprint import pprint
import requests

SEARCH_ENGINE_ID = "REPLACE_THIS"
API_KEY = "REPLACE_THIS_TOO"

FIELDNAMES = ["query", "result_url"]

def main():
    if len(sys.argv) != 2:
        print("Did not receive the correct number of parameters, please provide an input file with the queries to be made.")
        return
    in_f = open(sys.argv[1], "r", encoding="utf-8")
    out_f = open("targetsList.csv", "w", encoding="utf-8")

    csv_writer = csv.DictWriter(out_f, fieldnames=FIELDNAMES ,lineterminator="\n")

    for query in in_f:
        query = query.strip()

        params = {
            "cx": SEARCH_ENGINE_ID,
            "key": API_KEY,
            "q": query,
        }

        resp = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
        print("Got status code [" + str(resp.status_code) + "] while querying for " + query)

        json_dict = resp.json()

        for item_dict in json_dict.get("items", []):
            row = {
                "query": query,
                "result_url": item_dict.get("link"),
            }

            csv_writer.writerow(row)

    out_f.close()
    in_f.close()
    print("[+] We're all done, check your results on 'targetsList.csv'.")

if __name__ == "__main__":
    main()