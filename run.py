#!/usr/bin/env python3
#Made by dr0p

import argparse
import requests 

def argsParser():
    pars = argparse.ArgumentParser()
    pars.add_argument("--url","-u", help="url to crawl")
    pars.add_argument("--list","-l", help="list of urls to crawl")
    return pars

def get_url_content(url):
    content = requests.get(url).text.split('"')
    
    for elem in content:
        if "http" in elem:
            print(f"Link: {elem}")
    
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
