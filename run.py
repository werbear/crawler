#!/usr/bin/env python3
#Made by dr0p

import argparse
import requests 
from bs4 import BeautifulSoup as bs
import cssutils as cs

def argsParser():
    pars = argparse.ArgumentParser()
    pars.add_argument("--url","-u", help="url to crawl")
    pars.add_argument("--output","-o", help="Path to output")
    return pars

def get_url_content(url):
    content = requests.get(url).text
    s = bs(content,"html.parser")
    
    for elem in s.findAll("body"):
        ws = cs.parseStyle(elem.find("a").get("style"))
        print(f"Link: {elem.find('a').get('href')}")

def main():
    pars = argsParser()
    args = pars.parse_args()

    get_url_content(args.url)

if __name__ == "__main__":
    main()
