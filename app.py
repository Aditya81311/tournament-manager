from flask import Flask, render_template , request , redirect, url_for, session, flash
from main import Users, Teams,Games,Tournaments,Matches,Fetch_data
import sqlite3
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from functools import wraps
from flask import session, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "your_secret_key_here"  # Needed for sessions

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in first.", "warning")
            return redirect(url_for("login"))
        if session.get("user_role") != "admin":
            flash("You are not authorized to access this page.", "danger")
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated_function

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in first.", "warning")
            return redirect(url_for("login"))
        if session.get("user_role") not in ["user", "admin"]:
            flash("You cannot access this page.", "danger")
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated_function


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE user_email = ?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["user_id"]
            session["user_role"] = user["user_role"]
            session["user_name"] = user["user_name"]
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        role = "user"  # default role for new registrations
        password = request.form["password"]

        # Hash the password
        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO users (user_name, user_email, user_phone, user_role, password) VALUES (?, ?, ?, ?, ?)",
                (name, email, phone, role, password_hash),
            )
            conn.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Email or phone already exists.", "danger")
            return redirect(url_for("register"))
        finally:
            conn.close()

    return render_template("register.html")

@app.route("/create_admin", methods=["GET", "POST"])
def create_admin():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO users (user_name, user_email, user_phone, user_role, password) VALUES (?, ?, ?, ?, ?)",
                (name, email, phone, "admin", password_hash),
            )
            conn.commit()
            flash("Admin created successfully! Please log in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Email or phone already exists.", "danger")
            return redirect(url_for("create_admin"))
        finally:
            conn.close()

    return render_template("create_admin.html")

@app.route("/")
@login_required
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", role=session.get("user_role"), name=session.get("user_name"))

@app.route("/list_games",methods = ["GET","POST"])
@login_required
def list_games():
    if request.method == "GET":
        games = Fetch_data.fetch_games(None)
    return render_template("games.html",games = games)

@app.route("/add_games",methods = ["GET","POST"])
@login_required
@admin_required
def add_games():
    if request.method == "POST":
        game_name = request.form["game_name"] 
        game_genre = request.form["game_genre"]
        game = Games(None,game_name,game_genre)
        game.add_game()
    return render_template("add_games.html")

@app.route("/update_games",methods = ["GET","POST"])
@login_required
@admin_required
def update_games():
    if request.method == "GET":
            games = Fetch_data.fetch_games(None)
            return render_template("update_games.html",games = games)
    if request.method == "POST":
        game_id = request.form["game_id"]
        game_name = request.form["game_name"]
        game_genre = request.form["game_genre"]
        update = Games(game_id,game_name,game_genre)
        update.update_game()
    return render_template("update_games.html")

@app.route("/delete_games",methods = ["GET","POST"])
@login_required
@admin_required
def delete_games():
    games = Fetch_data.fetch_games(None)
    if request.method == "GET":
        return render_template("delete_games.html",games = games)
    if request.method == "POST":
        game_id = request.form["game_id"]
        delete = Games(game_id,None,None)
        delete.delete_game()
    return render_template("delete_games.html",games = games)

@app.route('/create_tournaments', methods=['GET','POST'])
@login_required
@admin_required
def create_tournament():
    if request.method == "GET":
        games = Fetch_data.fetch_games(None)
        return render_template('create_tournaments.html',games = games)
    if request.method == "POST":
        # tournament_id = request.form["tournament_id"]
        name = request.form["name"]
        game_id  = request.form["game_id"]
        start_date  = request.form["start_date"]
        end_date  = request.form["end_date"]
        status  = request.form["status"]
        create = Tournaments(None,name, game_id, start_date, end_date, status)
        create.create_tournament()
    return render_template('create_tournaments.html')
    

@app.route('/list_tournaments', methods=['GET'])
@login_required
def list_tournaments():
    if request.method == "GET":
        # tournament_id = request.form["tournament_id"]
        tournaments = Fetch_data.fetch_tournaments(None)
    return render_template('list_tournaments.html',tournaments = tournaments)
@login_required
@admin_required
@app.route('/update_tournaments', methods=['GET','POST'])
def update_tournaments():
    games = Fetch_data.fetch_games(None)
    tournaments = Fetch_data.fetch_tournaments(None)
    if request.method == "GET":
        return render_template('update_tournaments.html',games = games, tournaments = tournaments)
    if request.method == "POST":
        tournament_id = request.form["tournament_id"]
        name = request.form["name"]
        game_id  = request.form["game_id"]
        start_date  = request.form["start_date"]
        end_date  = request.form["end_date"]
        status  = request.form["status"]
        update = Tournaments(tournament_id,name, game_id, start_date, end_date, status)
        update.update_tournament()
    return render_template('update_tournaments.html',games = games, tournaments = tournaments)

@app.route('/delete_tournaments', methods=['POST'])
@login_required
@admin_required
def delete_tournament():
    if request.method == "GET":
        # tournament_id = request.form["tournament_id"]
        tournaments = Fetch_data.fetch_tournaments(None)
    return render_template('delete_tournaments.html',tournaments = tournaments)
    if request.method == "POST":
        tournament_id = request.form["tournament_id"]
        delete = Tournaments(tournament_id,None, None,None,None,None)
        delete.delete_tournament()
    return render_template('delete_tournaments.html')

@app.route('/create_matches', methods=['GET', 'POST'])
@login_required
def create_match():
    if request.method == "GET":
        tournaments = Fetch_data.fetch_tournaments(None)
        return render_template('create_matches.html',tournaments = tournaments)
    if request.method == "POST":
        # match_id = request.form["match_id"]
        tournament_id = request.form["tournament_id"]
        match_no = request.form["match_no"]
        round_no = request.form["round_no"]
        scheduled_at = request.form["scheduled_at"]
        status = request.form["status"]
        create = Matches(None,tournament_id, match_no, round_no, scheduled_at, status)
        create.add_match()
    return render_template('create_matches.html')
    
@app.route('/list_matches', methods=['GET'])
@login_required
def list_matches():
    if request.method == "GET":
        matches = Fetch_data.fetch_matches(None)
    return render_template('list_matches.html',matches = matches)


@app.route('/update_matches', methods=['GET', 'POST'])
@login_required
@admin_required
def update_match():
    if request.method == "GET":
        tournaments = Fetch_data.fetch_tournaments(None)
        matches = Fetch_data.fetch_matches(None)
        return render_template('update_matches.html',tournaments = tournaments,matches = matches)
    if request.method == "POST":
        # match_id = request.form["match_id"]
        tournament_id = request.form["tournament_id"]
        # match_no = request.form["match_no"]
        round_no = request.form["round_no"]
        scheduled_at = request.form["scheduled_at"]
        status = request.form["status"]
        create = Matches(None,tournament_id,None, round_no, scheduled_at, status)
        create.update_match()
        return render_template('update_matches.html')
    
@app.route('/delete_matches', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_match():
    if request.method  == "GET":
        matches = Fetch_data.fetch_matches(None)
        return render_template('delete_matches.html',matches = matches)
    if request.method == "POST":
        match_id = request.form["match_id"]
        delete = Matches(match_id,None,None,None,None,None)
        delete.delete_match()
        return render_template('delete_matches.html')

@app.route("/leader_board",methods = ["GET","POST"])
@login_required
def leader_board():
    if request.method == "GET":
        leaderboard = Fetch_data.fetch_leader_board(None)
        return render_template("leader_board.html",leaderboard = leaderboard)

if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0",port = 5000)