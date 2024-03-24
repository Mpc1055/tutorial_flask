from flask import Flask, redirect, url_for , render_template
app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")



#name page pass ref  variable
# @app.route("/<name>")
# def home(name):
#     return render_template("index.html", content=name)

@app.route("/")
def home():
    return render_template("index.html", content=["mike", "Joe", "steve"])



if __name__ == "__main__":
    app.run(debug=True)