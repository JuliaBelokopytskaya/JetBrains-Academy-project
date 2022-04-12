import argparse
import os
import shutil
import re
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

# write your code here
def inp_url(Web_pages):
    user = input()
    if re.findall(r"\w+\.\w+", user):
        r = requests.get('https://' + user)
        soup = BeautifulSoup(r.text, 'html.parser').body.descendants
        page = ""
        tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        for descendant in soup:
            if descendant.name in tags:
                if descendant.name == 'a':
                    page += Fore.BLUE + descendant.get_text().strip()
                else:
                    page += Style.RESET_ALL + descendant.get_text().strip()
        site = user.rsplit(".", 1)
        write_file_dir(site[0], page)
        Web_pages.append(site[0])
        print_pages(site[0])

    elif user == "exit":
        sys.exit()
    elif user == "back":
        Web_pages.pop()
        page = Web_pages.pop()
        print_pages(page)
    else:
        print("Incorrect URL")


def print_pages(name_site):
    with open(name_site, 'r') as file:
        print(file.read())

def write_file_dir(name_site, site):
    with open(name_site, 'w', encoding='UTF-8') as file:
        file.write(site)
    shutil.copy(name_site, os.path.join(args.directory, name_site))

parser = argparse.ArgumentParser(description="Accept a command-line argument which is a directory for saved tabs")
parser.add_argument("directory", type=str)
args = parser.parse_args()
if not os.access(args.directory, os.F_OK):
    os.mkdir(args.directory)
Web_pages = []
while True:
    inp_url(Web_pages)
