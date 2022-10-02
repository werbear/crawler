#!/usr/bin/env python3
#Made by dr0p

import argparse
import requests 
from bs4 import BeautifulSoup as bs
import cssutils as cs

def argsParser():
    pars = argparse.ArgumentParser()
    pars.add_argument("--url","-u", help="url to crawl")
    pars.add_argument("--list","-l", help="list of urls to crawl")
    return pars

def get_url_content(url):
    content = requests.get(url).text
    s = bs(content,"html.parser")
    
    for elem in s.findAll("body"):
        ws = cs.parseStyle(elem.find("a").get("style"))
        print(f"Link: {elem.find('a').get('href')}")

def ifFile(urllist):
    with open(urllist,"r") as f:
        for elem in f:
            get_url_content(elem)
        
def main():
    pars = argsParser()
    args = pars.parse_args()
    
    if args.url == None and args.list:
        ifFile(args.list)
    else:
        get_url_content(args.url)

if __name__ == "__main__":
    main()
