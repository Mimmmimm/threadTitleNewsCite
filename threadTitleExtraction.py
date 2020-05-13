#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
目的: 5ch検索のページから、スレッドのタイトルだけを抽出する
"""
def extraction():
    import requests
    #import pandas as pd
    from bs4 import BeautifulSoup
    
    html = requests.get("https://ff5ch.syoboi.jp/")
    soup=BeautifulSoup(html.content,"html.parser")
    #print(soup)
    
    contents = soup.find_all(class_="thread")
    
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

"""    
textLists = extraction()   
textStrings = reshapeToStrings(textLists)   
print(textStrings)
"""
    