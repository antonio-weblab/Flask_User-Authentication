from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
USERNAME = "admin"
PASSWORD = "admin"
app.secret_key = b'_!"5"FGH/'
@app.get("/admin")
def admin():
    if "username" in session: 
        username = session["username"]
        
        return render_template("admin_page.html", username=username)
    else:
        
        return redirect(url_for("login")) 
@app.post("/logout")
def logout():
    
    session.pop("username", None)
    return redirect(url_for("login"))
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == USERNAME and password == PASSWORD:
            session["username"] = username
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("login"))
@app.route("/")
def index():
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)
