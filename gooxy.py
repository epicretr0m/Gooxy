import argparse
import requests
import sys
import urllib.request
import socket
import concurrent.futures

def main():
    print("╔═╗┌─┐┌─┐─┐ ┬┬ ┬")
    print("║ ╦│ ││ │┌┴┬┘└┬┘")
    print("╚═╝└─┘└─┘┴ └─ ┴")
    cmdsParser = argparse.ArgumentParser(description='Gooxy - Tool to quickly fetch and verify proxies.')
    cmdsParser.add_argument("--google", help="Fetch proxies that support Google.", dest='google', action='store_true', default=False)
    cmdsParser.add_argument("--http", help="Fetch HTTP proxies.", dest='http', action='store_true', default=False)
    cmdsParser.add_argument("--amount", help="Number of proxies to fetch (Default: 10)", dest='amount', default=10, type=int)
    cmdsParser.add_argument("--timeout", help="Connection Timeout (Default: 15)", dest='timeout', default=15, type=int)
    cmds = cmdsParser.parse_args()
    getP(cmds.google, cmds.http, cmds.amount, cmds.timeout)

def fetch_proxies(api_url):
    r = requests.get(api_url)
    return r.json()

def getP(google, http, amount, timeout):
    print('\n+ Gooxy started with options:\n\n- Google: {}\n- HTTP: {}\n- Amount: {}\n- Timeout: {}\n\n'.format(google, http, amount, timeout))
    API1 = 'http://pubproxy.com/api/proxy?limit=5'
    API2 = 'https://gimmeproxy.com/api/getProxy?post=true&get=true&maxCheckPeriod=3600&anonymityLevel=1'
    API3 = 'https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterLastChecked=60'

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(fetch_proxies, API1), executor.submit(fetch_proxies, API2), executor.submit(fetch_proxies, API3)]

        all_proxies = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if "data" in result:
                all_proxies.extend(result["data"])

        count = 0
        for proxy in all_proxies:
            isGoogle = proxy.get("support", {}).get("google", 0) == 1
            isHttp = proxy.get("support", {}).get("http", 0) == 1

            if (google and not isGoogle) or (http and not isHttp):
                continue

            if Check(proxy["ip"], proxy["port"], proxy["type"], proxy["country"], isGoogle, isHttp, google, http, amount, timeout):
                count += 1
                if count >= amount:
                    break

def Check(ip, port, type, country, isGoogle, isHttp, google, http, amount, timeout):
    socket.setdefaulttimeout(timeout)
    protocol = "http"
    if isHttp:
        protocol = "http"
    try:
        proxy_handler = urllib.request.ProxyHandler({f'{protocol}': f'{ip}:{port}'})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        sock = urllib.request.urlopen('http://www.google.com')
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as detail:
        return 1

    global countNow
    if countNow >= amount:
        return sys.exit()
    countNow += 1
    return 0

def Printer(ip, port, type, country, isGoogle, isHttp):
    print(f'{type} {ip} {port}\n# Country: {country} Google: {isGoogle} HTTP: {isHttp}')

countNow = 0

if __name__ == "__main__":
    main()
