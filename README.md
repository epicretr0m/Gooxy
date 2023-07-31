# Gooxy - Fast Proxy Tool

Gooxy is a Python script that allows you to quickly obtain and verify proxies from various sources. It offers flexibility in choosing proxies that specifically support Google searches or HTTP connections. The script's functionality includes fetching proxies from multiple APIs, validating their access to Google, and displaying proxy details for easy selection.

## Features:

    Obtain proxies that meet your requirements for Google and HTTP support.
    Set the number of proxies to fetch (amount) and the connection timeout.
    Verify proxies' validity by checking their access to http://www.google.com.
    Display detailed information about each valid proxy, including type, IP address, port, and country.

## Usage:
```py
python gooxy.py [--google] [--http] [--amount AMOUNT] [--timeout TIMEOUT]
```

## APIs Used:

    http://pubproxy.com/api/proxy?limit=5: Fetch up to 5 proxies from pubproxy.com.
    https://gimmeproxy.com/api/getProxy?post=true&get=true&maxCheckPeriod=3600&anonymityLevel=1: Fetch a random HTTPS proxy from gimmeproxy.com.
    https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterLastChecked=60: Fetch up to 50 HTTPS proxies from proxylist.geonode.com.

## Note:

Use proxies responsibly and in compliance with the terms of service of the websites you access through them.
