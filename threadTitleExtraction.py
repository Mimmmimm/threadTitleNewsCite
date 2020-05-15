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
    
    # NGワードを含む記事を除外
    textLists_tmp = deleteInappropriateTitles(textLists)
    textLists = textLists_tmp
    
    #print(textLists)
    return textLists

#NG_words = []
NG_words = ["アホ", "阿呆", "バカ", "馬鹿", "在日", "クソサヨ", "ネトウヨ",
            "バヨ", "パヨ", "？", "?", "変なスレ"]
def deleteInappropriateTitles(titles): # 指定したNGワードを含むタイトルを除外する    
    for title in reversed(list(titles)):
        #print(title)
        for NG_word in NG_words:
            #print(NG_word)
            if NG_word in title:
                #print("NGワードが含まれました")
                titles.remove(title)
                break        
        
    return titles
    

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