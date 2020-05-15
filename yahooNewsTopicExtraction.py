#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def extraction():
    import requests
    #import pandas as pd
    from bs4 import BeautifulSoup
    
    html = requests.get("https://news.yahoo.co.jp/")
    soup=BeautifulSoup(html.content,"html.parser")
    #print(soup)
    
    contents = soup.find_all(class_="topicsListItem")
    
    textLists = []
    for i in range(len(contents)):
        textLists.append(contents[i].text)
    
    #print(textLists)
    
    # 不要な文字列を消す
    
    #print(textLists[0].split("[")[0] )
    
    for i in range(len(textLists)):
        textLists[i] = textLists[i].split("[")[0]
        textLists[i] = textLists[i].split("★")[0]
        textLists[i] = textLists[i].replace("\u3000"," ")
    
    
    #print(textLists)
    return textLists

def reshapeToStrings(List):
    textStrings = ""
    for i in range(len(List)):
        textStrings += (List[i] + "　　　　　　")
    
    return textStrings

extraction()