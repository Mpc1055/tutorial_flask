from flask import Flask, redirect, url_for , render_template
app = Flask(__name__)

# #homepage
# @app.route("/")
# def home():
#     return "Hello! this is the main page <h1>HELLO</h1>"

#homepage wih html template
@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/<usr>")
# def user(usr):
#     return "<h1> {usr} <!h1>"


# #new page
# @app.route("/<name>")
# def user(name):
#     return "Hello %s!" %(name)


# # redirect example
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)