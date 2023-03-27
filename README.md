# ProxyPokerListMaker
A simple Python script using Google Search's API to create a time-relevant list of public facing targets based on your queries. Ideally used with [ProxyPoker](https://github.com/Vulcanun/ProxyPoker).

## Usage
As simple as it gets, run the script providing a list of queries as its only argument.

```
ProxyPokerListMaker.py googleQueries.txt
Got status code [200] while querying for site:azurewebsites.net
Got status code [200] while querying for site:s3.amazonaws.com
Got status code [200] while querying for site:us-east-2.amazonaws.com
[+] We're all done, check your results on 'targetsList.csv'.
```

Just make sure you fill the script with your "SEARCH_ENGINE_ID" and "API_KEY". If you don't have a key yet, quickly generate one for free at [this link](https://developers.google.com/webmaster-tools/search-console-api/v1/configure).
