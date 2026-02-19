from flask import Flask, render_template , request 
from main import Users, Teams,Games,Tournaments

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list_games",methods = ["GET","POST"])
def list_games():
    if request.method == "GET":
        games = Games(None,None,None)
        listgames = games.list_games()
    return render_template("games.html",games = listgames)

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
        games = Games(None,None,None)
        listgames = games.list_games()
    return render_template("delete_games.html",games = listgames)

@app.route("/delete_games",methods = ["POST"])
def delete_games():
    if request.method == "POST":
        game_id = request.form["game_id"]
        delete = Games(game_id,None,None)
        delete.delete_game()
    return "Success"
@app.route('/create_tournament', methods=['GET'])
def list_games_to_tournament():
    if request.method == "GET":
        games = Games(None,None,None)
        listgames = games.list_games()
    return render_template('create_tournaments.html',games = listgames)
@app.route('/create_tournament', methods=['POST'])
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
        lists = Tournaments(None,None, None,None,None,None)
        tournaments = lists.list_tournaments()
    return render_template('list_tournaments.html',tournaments = tournaments)

@app.route('/update_tournaments', methods=['GET'])
def show_update_page():
    if request.method == "GET":
        games = Games(None,None,None)
        listgames = games.list_games()
        lists = Tournaments(None,None, None,None,None,None)
        tournaments = lists.list_tournaments()
    return render_template('update_tournaments.html',games = listgames, tournaments = tournaments)
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


@app.route('/delete_tournament', methods=['GET', 'POST'])
def delete_tournament():
    return render_template('delete_tournament.html')


if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0",port = 5000)