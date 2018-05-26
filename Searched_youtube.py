# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:39:29 2018

@author: Ismail
"""
import urllib
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


def Search(text_to_search):
    file_for_link = open("link_list.txt", "a")
    file_for_link.write("\n")
    file_for_link.write("Top link for "+text_to_search+" : \n")
    query = urllib.parse.quote(text_to_search)
    url =  "https://www.youtube.com/results?search_query=" + query
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    print()
    print("Top link for "+text_to_search+" : \n")
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        file_for_link.write("https://www.youtube.com" + vid['href']+"\n")
        print( 'https://www.youtube.com' + vid['href'])
    file_for_link.write("\n")
    file_for_link.close()


def Take_query():
    total = int(input("How many query do you like to make: "))
    
    for num in range(0,total):
        query_str = input("Enter a line to be searched: ")
        Search(query_str)
    
Take_query()


        
    