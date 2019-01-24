from flask import Flask
from flask import render_template, request
from database import get_all_ideas
from database import get_idea_by_id
from database import create_idea

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/brainstorm')
def brainstorm():
    ideas=get_all_ideas()
    return render_template("brainstorm.html", ideas=ideas)

@app.route('/add', methods=['GET', 'POST'])
def add_idea():
    if request.method == "GET":
        return render_template('add.html')
    else:
        name = request.form['yourname']
        content = request.form['content']
        links = request.form['links']
        posx = request.form['posx']
        posy = request.form['posy']
        create_idea(name=name, content=content, links=links, posx=posx, posy=posy)
        ideas=get_all_ideas()
        return render_template("brainstorm.html", ideas=ideas)
        
@app.route('/browse')
def browse():
    return render_template("browse.html")

if __name__ == '__main__':
   app.run(debug = True)