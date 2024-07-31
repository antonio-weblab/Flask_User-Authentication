from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Definiamo 2 costanti 
USERNAME = "admin"
PASSWORD = "admin"

app.secret_key = b'_!"5"FGH/'

# Creo la rotta per la root
@app.route("/")
def index():
    return "<p>Flask_User-Authentication</p>"

# Creo un redirect alla pagina/rotta /admin
@app.get("/admin")
def admin():
    if "username" in session: # se username corrisponde al controllo e si trova in session (vedi def login() ) return Hello username
        username = session["username"]
        return f"<p>Hello {username}</p>" # aggiungo f per poter usare {username}
    else:
        return redirect(url_for("login")) # se username non corrisponde ritorna a login

# creo la rotta per la pagina di login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form["username"]
        password = request.form["password"]
        if username == USERNAME and password == PASSWORD:
            session["username"] = username # passa a session username che p stato verificato
            return redirect(url_for("admin")) #reindirizza alla rotta admin
        else:
            return "<p>Wrong username or password</p>"

# per avviare "name" deve essere == a "main"
if __name__ == "__main__":
    app.run(debug=True)

# avvia la app con python app.py

# Per controllare se è online usa LiveServer e controlla che la porta sia la stessa porta del messaggio Running on "https://127...""


