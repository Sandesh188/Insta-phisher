import sys
import time
import pyshorteners
from urllib.parse import urlparse
import re

def mask_url(domain, keyword, url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

# Initialize only clck.ru shortener
s = pyshorteners.Shortener()

try:
    while True:
        web_url = input("Enter the original link (ex: https://www.ngrok.com): ")
        if re.match(r'^(https?://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d{1,5})?(/.*)?$', web_url):
            break
        print("Invalid URL format. Please provide a valid web URL.")

    while True:
        custom_domain = input("Enter your custom domain (ex: gmail.com): ")
        if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', custom_domain):
            break
        print("Invalid custom domain. Please provide a valid domain name.")

    while True:
        phish = input("Enter phishing keyword (ex: account, login): ")
        if " " not in phish and len(phish) <= 15:
            break
        print("Phishing keyword should not contain spaces and must be under 15 characters.")

    print("\nProcessing...\n")
    try:
        short_url = s.clckru.short(web_url)
        masked_url = mask_url(custom_domain, phish, short_url)
        print("\n========== Final Masked URL ==========\n")
        print(masked_url)
        print("\n=====================================\n")
    except pyshorteners.exceptions.ShorteningErrorException as e:
        print("Error shortening URL:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))

except Exception as e:
    print("An error occurred:", str(e))