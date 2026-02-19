from flask import Flask, render_template , request 
from main import Users, Teams,Games,Tournaments,Matches,Fetch_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list_games",methods = ["GET","POST"])
def list_games():
    if request.method == "GET":
        games = Fetch_data.fetch_games(None)
    return render_template("games.html",games = games)

@app.route("/add_games",methods = ["GET","POST"])
def add_games():
    if request.method == "POST":
        game_name = request.form["game_name"] 
        game_genre = request.form["game_genre"]
        game = Games(None,game_name,game_genre)
        game.add_game()
    return render_template("add_games.html")

@app.route("/update_games",methods = ["GET","POST"])
def update_games():
    if request.method == "POST":
        game_id = request.form["game_id"]
        game_name = request.form["game_name"]
        game_genre = request.form["game_genre"]
        update = Games(game_id,game_name,game_genre)
        update.update_game()
    return render_template("update_games.html")

@app.route("/delete_games",methods = ["GET"])
def show_delete_games():
    if request.method == "GET":
        games = Fetch_data.fetch_games(None)
    return render_template("delete_games.html",games = games)

@app.route("/delete_games",methods = ["POST"])
def delete_games():
    if request.method == "POST":
        game_id = request.form["game_id"]
        delete = Games(game_id,None,None)
        delete.delete_game()
    return "Success"

@app.route('/create_tournaments', methods=['GET'])
def list_games_to_tournament():
    if request.method == "GET":
        games = Fetch_data.fetch_games(None)
    return render_template('create_tournaments.html',games = games)
@app.route('/create_tournaments', methods=['POST'])
def create_tournament():
    if request.method == "POST":
        # tournament_id = request.form["tournament_id"]
        name = request.form["name"]
        game_id  = request.form["game_id"]
        start_date  = request.form["start_date"]
        end_date  = request.form["end_date"]
        status  = request.form["status"]
        create = Tournaments(None,name, game_id, start_date, end_date, status)
        create.create_tournament()
    return "success"
    

@app.route('/list_tournaments', methods=['GET'])
def list_tournaments():
    if request.method == "GET":
        # tournament_id = request.form["tournament_id"]
        tournaments = Fetch_data.fetch_tournaments(None)
    return render_template('list_tournaments.html',tournaments = tournaments)

@app.route('/update_tournaments', methods=['GET'])
def show_update_page():
    if request.method == "GET":
        games = Fetch_data.fetch_games(None)
        tournaments = Fetch_data.fetch_tournaments(None)
    return render_template('update_tournaments.html',games = games, tournaments = tournaments)
@app.route('/update_tournaments', methods=['POST'])
def update_tournaments():
    if request.method == "POST":
        tournament_id = request.form["tournament_id"]
        name = request.form["name"]
        game_id  = request.form["game_id"]
        start_date  = request.form["start_date"]
        end_date  = request.form["end_date"]
        status  = request.form["status"]
        update = Tournaments(tournament_id,name, game_id, start_date, end_date, status)
        update.update_tournament()
    return "success"

@app.route('/delete_tournaments', methods=['GET'])
def show_delete_tournaments():
    if request.method == "GET":
        # tournament_id = request.form["tournament_id"]
        tournaments = Fetch_data.fetch_tournaments(None)
    return render_template('delete_tournaments.html',tournaments = tournaments)
@app.route('/delete_tournaments', methods=['POST'])
def delete_tournament():
    if request.method == "POST":
        tournament_id = request.form["tournament_id"]
        delete = Tournaments(tournament_id,None, None,None,None,None)
        delete.delete_tournament()
    return "success"

@app.route('/create_matches', methods=['GET', 'POST'])
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
        return "success"
    
@app.route('/list_matches', methods=['GET'])
def list_matches():
    if request.method == "GET":
        matches = Fetch_data.fetch_matches(None)
    return render_template('list_matches.html',matches = matches)


@app.route('/update_matches', methods=['GET', 'POST'])
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
        return "success"
    


@app.route('/delete_matches', methods=['GET', 'POST'])
def delete_match():
    if request.method  == "GET":
        matches = Fetch_data.fetch_matches(None)
        return render_template('delete_matches.html',matches = matches)
    if request.method == "POST":
        match_id = request.form["match_id"]
        delete = Matches(match_id,None,None,None,None,None)
        delete.delete_match()
        return "success"


if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0",port = 5000)