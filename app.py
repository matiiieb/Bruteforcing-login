from flask import Flask, render_template, request

app = Flask(__name__,template_folder='Templates')

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == "admin" and password == "secret":
        return "FLAG {!@#!@#!@#!@#!@#!@#!@#!@#!@#!@#!@#!@#!@#!@#!@#}"
    else:
        return "Login Failed"

if __name__ == "__main__":
    app.run()
