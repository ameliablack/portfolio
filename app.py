from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/template")
def template():
    return render_template("template.html") 

@app.route("/aboutme")
def index():
    return render_template("index.html") 

@app.route("/hobby")
def hobby():
    return render_template("hobby.html") 



if __name__ =='__main__':
    app.run(debug=True)
