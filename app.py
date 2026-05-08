from flask import Flask, request, redirect, url_for, jsonify, render_template

#create an instance of Flask class
app = Flask(__name__)

@app.route("/")

def index():

    return"<h1>Hello</h1>"

@app.route("/home", methods = ["GET"])

def home():

    return "<h1>Home</h1><p>Welcome to the home page Ajay !</p>"

@app.route("/json")

def json():

    return {"mykey":"JSON Data","mylist":[1,2,3,4,5]}

@app.route("/dynamic/<user_input>")
def dynamic(user_input):

    return f"<h1> The user entered : {user_input}</h1>"

@app.route("/query")
def query():

    hello = request.args.get("hello")

    world = request.args.get("world")

    return f"<h1> The query string contains : {hello} and {world}</h1>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if username :
            return redirect(url_for("home")) 

    return """
    <h1> Login Page</h1>
    <form method="post">
                  <input type="text" name="username" placeholder="Username">
                  <input type="submit" value="Login">
              </form>"""

if __name__ == '__main__':
    app.run(debug=True)

    
    # password = request.form.get("password")
    # if password:
    #     # Here you would typically check the username and password
    #     return redirect(url_for("home"))
    # return render_template("login.html", title="Login")