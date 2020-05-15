from flask import Flask, request, render_template
app = Flask(__name__)
import threadTitleExtraction
import yahooNewsTopicExtraction
import random

def makeNewsList():
    # スレッドタイトルを抜きだしてくる
    textLists_5ch = threadTitleExtraction.extraction()
    
    # yahooニュースのタイトルを抜き出してくる
    textLists_yahoo = yahooNewsTopicExtraction.extraction()
    
    # 抜き出してきたリストを統合して、順番をランダムで入れ替える
    textLists = textLists_5ch + textLists_yahoo
    random.shuffle(textLists)
    
    return textLists

@app.route("/")
def show():
    message = "Hello World"
    textLists = makeNewsList()
    
    # 表示する形の一つの文字列に変形する
    textStrings = threadTitleExtraction.reshapeToStrings(textLists)
    return render_template("scrollNews.html", textStrings = textStrings)

@app.route("/result", methods=["GET", "POST"])
def result():
    textLists = makeNewsList()
    
    # 表示する形の一つの文字列に変形する
    textStringsUpdate = threadTitleExtraction.reshapeToStrings(textLists)
    return render_template("scrollNews.html", textStrings = textStringsUpdate)

"""
textLists = makeNewsList()
print(textLists)
textStrings = threadTitleExtraction.reshapeToStrings(textLists)
print(textStrings)
"""
