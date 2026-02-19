import sqlite3

conn = sqlite3.connect("database.db")

cur = conn.cursor()

class Data_base():
    def user_table(self):
        cur.execute('''
         CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY ,
            user_name VARCHAR(100) NOT NULL,
            user_email VARCHAR(100) UNIQUE NOT NULL,
            user_phone VARCHAR(12) UNIQUE,
            user_role VARCHAR(50) NOT NULL
          )
        ''')
        print("User Table Crated ")
    def team_table(self):
        cur.execute(''' 
          
        CREATE TABLE IF NOT EXISTS teams (
            team_id INTEGER PRIMARY KEY ,
            team_name VARCHAR(100) UNIQUE NOT NULL,
            game_id INTEGER NOT NULL,
            team_captain_id INTEGER NOT NULL,
            FOREIGN KEY (game_id) REFERENCES games(game_id),
            FOREIGN KEY (team_captain_id) REFERENCES users(user_id)
        )
            ''')
        print("Team Table Crated ")
    def team_member(sef):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS team_members (
            member_id INTEGER PRIMARY KEY ,
            team_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            join_date DATE NOT NULL,
            is_captain BOOLEAN NOT NULL DEFAULT FALSE,
            FOREIGN KEY (team_id) REFERENCES teams(team_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            UNIQUE (team_id, user_id)
        )
        ''')
        print("Team Members Table Created")
    def games_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS games (
            game_id INTEGER PRIMARY KEY ,
            game_name VARCHAR(100) NOT NULL,
            game_genre VARCHAR(50) NOT NULL
        )

        ''')
        print("Games Table Crated ")
    def tournament_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS tournaments (
            tournament_id INTEGER PRIMARY KEY ,
            name VARCHAR(100) NOT NULL,
            game_id INTEGER NOT NULL,
            FOREIGN KEY (game_id) REFERENCES games(game_id)
        )
        ''')
        print("Taurnament Table Created")
    def matches_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            match_id INTEGER PRIMARY KEY ,
            tournament_id INTEGER NOT NULL,
            match_no INTEGER NOT NULL,
            round_no INTEGER NOT NULL,
            scheduled_at DATE NOT NULL,
            status VARCHAR(20) NOT NULL,
            FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id)
        )
        ''')
        print("Matches Table Crated ")

    def leader_board_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS leader_board (
            leaderboard_id INTEGER PRIMARY KEY ,
            tournament_id INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            match_id INTEGER NOT NULL,
            played INTEGER NOT NULL,
            wins INTEGER NOT NULL,
            score_for INTEGER NOT NULL,
            score_against INTEGER NOT NULL,
            updated DATE NOT NULL,
            FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id),
            FOREIGN KEY (team_id) REFERENCES teams(team_id),
            FOREIGN KEY (match_id) REFERENCES matches(match_id),
            UNIQUE (tournament_id, team_id, match_id)
            )

        ''')
        print("Leader Board Table Created")
if __name__ == "__main__":
    create_tables = Data_base()
    create_tables.user_table()
    create_tables.team_table()
    create_tables.team_member()
    create_tables.games_table()
    create_tables.tournament_table()
    create_tables.matches_table()
    create_tables.leader_board_table()
    