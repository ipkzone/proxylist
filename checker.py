import requests
import threading

Yellow = "\033[33m"
Green = "\033[92m"
White = "\033[0m"
Red = "\033[31m"

def check_proxy(proxy, i):
    try:
        response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=10)
        httpcode = response.status_code
        if httpcode == 200:
            print(f" {Red}[{White}{i}{Red}]{White} Connected proxy {Green}{proxy}{White} to Google with HTTP {httpcode} OK")
            save_active_proxy(proxy)
        else:
            print(f" {Red}[{White}{i}{Red}]{White} Error connecting to Google via proxy {Red}{proxy}{White}. HTTP code: {Red}{httpcode}{White}")
    except Exception as e:
        print(f" {Red}[{White}{i}{Red}]{White} Error: {str(e)}")

def save_active_proxy(proxy):
    with open('proxy_aktif.txt', 'a') as file:
        file.write(proxy + '\n')

def main():
    proxies = []
    with open('proxy_live.txt', 'r') as file:
        proxies = file.read().splitlines()

    threads = []
    i = 1
    for proxy in proxies:
        thread = threading.Thread(target=check_proxy, args=(proxy, i))
        threads.append(thread)
        thread.start()
        i += 1

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
