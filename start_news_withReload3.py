from flask import Flask, request, render_template
app = Flask(__name__)
import threadTitleExtraction

@app.route("/")
def show():
    message = "Hello World"
    # スレッドタイトルを抜きしてくる
    textLists = threadTitleExtraction.extraction()
    
    # 表示する形の一つの文字列に変形する
    textStrings = threadTitleExtraction.reshapeToStrings(textLists)
    return render_template("form.html", textStrings = textStrings)

@app.route("/result", methods=["GET", "POST"])
def result():
    # スレッドタイトルを抜きだしてくる
    textLists = threadTitleExtraction.extraction()
    
    # 表示する形の一つの文字列に変形する
    textStringsUpdate = threadTitleExtraction.reshapeToStrings(textLists)
    """
    if request.method == "POST":
        article = request.form["article"]
        name = request.form["name"]
    else:
        article = request.args.get("article")
        name = request.args.get("name")
    """
    return render_template("scrollNews.html", textStrings = textStringsUpdate)
