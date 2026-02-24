import sqlite3
from datetime import datetime

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

class Users():
    def __init__(self,user_id,name,email,phone,role):
            self.user_id = user_id
            self.user_name  = name
            self.user_email =  email
            self.user_phone = phone
            self.user_role  = role
            
    def create_user(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
          INSERT INTO users(user_name ,
            user_email, 
            user_phone, 
            user_role) VALUES(
            ?,?,?,?
            ) 
        ''',(self.user_name ,
            self.user_email, 
            self.user_phone, 
            self.user_role ))
        conn.commit()
        conn.close()

    def list_users(self):
        conn = get_db_connection()
        cur = conn.cursor()
        user = cur.execute('''
        SELECT * from users 
            ''')
        result = user.fetchall()
        conn.close()
        return result

    def update_user(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            UPDATE users
            SET user_name = ?,
            user_email = ? , 
            user_phone = ?, 
            user_role = ? 
            WHERE user_id = ?''',(self.user_name ,self.user_email, self.user_phone, self.user_role,self.user_id))
        conn.commit()
        conn.close()

    def delete_user(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        DELETE FROM users WHERE user_id = ?
        ''',(self.user_id,))
        conn.commit()
        conn.close()

class Teams():
    def __init__(self, team_id, team_name, game_id, team_captain_id):
               self.team_id = team_id
               self.team_name = team_name
               self.game_id = game_id
               self.team_captain_id = team_captain_id

    def create_team(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO teams(team_name, game_id, team_captain_id) 
            VALUES(?,?,?)
        ''', (self.team_name, self.game_id, self.team_captain_id))
        conn.commit()
        conn.close()
    
    def list_teams(self):
        conn = get_db_connection()
        cur = conn.cursor()
        # Use old column names: game (text) and team_captain (text)
        teams = cur.execute('''
            SELECT 
                team_id,
                team_name,
                game_id,
                team_captain_id
            FROM teams
            ORDER BY team_id DESC
        ''')
        result = teams.fetchall()
        conn.close()
        return result

    def update_team(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            UPDATE teams 
            SET team_name = ?, game_id = ?, team_captain_id = ? 
            WHERE team_id = ?
        ''', (self.team_name, self.game_id, self.team_captain_id, self.team_id))
        conn.commit()
        conn.close()

    def delete_team(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        DELETE FROM teams WHERE team_id = ?
        ''', (self.team_id,))
        conn.commit()
        conn.close()

def Join_Teams(team_id,user_id):
    conn = get_db_connection()
    curr = conn.cursor()
    curr.execute('''
    INSERT INTO team_members(team_id, user_id)
    VALUES(?,?)
    ''',(team_id,user_id))
    conn.commit()
    conn.close()

def User_teams(user_id):
    conn = get_db_connection()
    curr = conn.cursor()
    user_teams = curr.execute('''
        SELECT t.team_id , t.team_name , g.game_name , u.user_name  FROM team_members tm
        JOIN teams t ON tm.team_id = t.team_id
        JOIN users u ON t.team_captain_id = u.user_id
        JOIN games g ON t.game_id = g.game_id
        WHERE tm.user_id = ?
        ''',(str(user_id))).fetchall()
    conn.commit()
    conn.close()
    return [dict(row) for row in user_teams]

class Games():
    def __init__(self,game_id,game_name,game_genre):
        self.game_id = game_id
        self.game_name = game_name
        self.game_genre = game_genre
    
    def add_game(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        INSERT INTO games(game_name,game_genre)
        VALUES(?,?)
        ''',(self.game_name,self.game_genre))
        conn.commit()
        conn.close()
        return "Game Added"
    
    def list_games(self):
        conn = get_db_connection()
        cur = conn.cursor()
        game = cur.execute(''' 
        SELECT * FROM games
        ''')
        result = game.fetchall()
        conn.close()
        return result
  
    def update_game(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        UPDATE games SET game_name = ?,game_genre = ? 
         WHERE game_id = ?
        ''',(self.game_name,self.game_genre,self.game_id))
        conn.commit()
        conn.close()

    def delete_game(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        DELETE FROM games WHERE game_id = ?
        ''',(self.game_id,))
        conn.commit()
        conn.close()
        
class Tournaments():
    def __init__(self, tournament_id, name, game_id, start_date=None, end_date=None, status='Upcoming'):
        self.tournament_id = tournament_id
        self.name = name
        self.game_id = game_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        
    def create_tournament(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO tournaments(name, game_id, start_date, end_date, status)
            VALUES(?,?,?,?,?)
        ''', (self.name, self.game_id, self.start_date, self.end_date, self.status))
        conn.commit()
        conn.close()
        
    def list_tournaments(self):
        conn = get_db_connection()
        cur = conn.cursor()
        tournaments = cur.execute('''
            SELECT 
                t.tournament_id,
                t.name,
                g.game_name,
                t.start_date,
                t.end_date,
                t.status,
                t.game_id
            FROM tournaments t
            LEFT JOIN games g ON t.game_id = g.game_id
            ORDER BY t.tournament_id DESC
        ''')
        result = tournaments.fetchall()
        conn.close()
        return result
        
    def update_tournament(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            UPDATE tournaments 
            SET name = ?, game_id = ?, start_date = ?, end_date = ?, status = ?
            WHERE tournament_id = ?
        ''', (self.name, self.game_id, self.start_date, self.end_date, self.status, self.tournament_id))
        conn.commit()
        conn.close()
        
    def delete_tournament(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM tournaments WHERE tournament_id = ?
        ''', (self.tournament_id,))
        conn.commit()
        conn.close()

class Matches():
    def __init__(self, match_id, tournament_id, match_no, round_no, team_id_1,team_id_2,scheduled_at, status):
        self.match_id = match_id
        self.tournament_id = tournament_id
        self.match_no = match_no
        self.round_no = round_no 
        self.team_id_1 = team_id_1
        self.team_id_2 = team_id_2
        self.scheduled_at = scheduled_at
        self.status = status
        
    def add_match(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        INSERT INTO matches(tournament_id, match_no, round_no,team_id_1,team_id_2, scheduled_at, status)
        VALUES(?,?,?,?,?,?,?)
        ''', (self.tournament_id, self.match_no, self.round_no,self.team_id_1,self.team_id_2, self.scheduled_at, self.status))
        conn.commit()
        conn.close()

    def list_matches(self):
        conn = get_db_connection()
        cur = conn.cursor()
        matches = cur.execute('''
            SELECT 
                m.match_id,
                t.name,
                m.match_no,
                m.round_no,
                tm1.team_name AS team_1,
                tm2.team_name AS team_2,
                m.scheduled_at,
                m.status
            FROM matches m
            JOIN tournaments t ON m.tournament_id = t.tournament_id
            JOIN teams tm1  ON m.team_id_1 = tm1.team_id
            JOIN teams tm2 ON m.team_id_2 = tm2.team_id
            ORDER BY scheduled_at DESC
        ''').fetchall()
        conn.close()
        return matches
        
    def update_match(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        UPDATE matches 
        SET tournament_id = ? , match_no = ? , round_no = ? ,team_id_1 = ? ,team_id_2 = ? , scheduled_at = ? , status = ? 
        WHERE match_id = ?
        ''', (self.tournament_id, self.match_no, self.round_no,self.team_id_1,self.team_id_2, self.scheduled_at, self.status,self.match_id))
        conn.commit()
        conn.close()

    def delete_match(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        DELETE FROM matches WHERE match_id = ?
        ''', (self.match_id,))
        conn.commit()
        conn.close()
    
class Scores:
    def __init__(self,match_id,tournament_id,team1_score, team2_score, winner_id):
        self.match_id = match_id
        self.tournament_id = tournament_id
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.winner_id = winner_id

    def add_score(self):
        conn = get_db_connection()
        curr = conn.cursor()
        curr.execute('''
        INSERT INTO scores(match_id,tournament_id,team_score_1, team_score_2, winner)
        VALUES(?,?,?,?,?)
        ''',(self.match_id,self.tournament_id,self.team1_score, self.team2_score, self.winner_id))
        conn.commit()
        conn.close()

class Fetch_data():
    def __init__(self,user_id,tournament_id):
        self.user_id = user_id
        self.tournament_id = tournament_id

    def fetch_users(self):
        conn = get_db_connection()
        cur = conn.cursor()
        user = cur.execute('''
        SELECT * FROM users
        ''').fetchall()
        conn.close()
        return [dict(row) for row in user]

    def fetch_user_info(self):
        conn = get_db_connection()
        cur = conn.cursor()
        user_info = cur.execute('''
        SELECT * FROM users WHERE user_id = ?
        ''',(self.user_id,)).fetchall()
        conn.close()
        return [dict(row) for row in user_info]

    def fetch_captain(self):
        conn = get_db_connection()
        cur = conn.cursor()
        captains = cur.execute('''
        SELECT u.user_name FROM team_members tm JOIN users u ON tm.user_id = u.user_id WHERE tm.is_captain = TRUE
        ''').fetchall()
        conn.close()
        return [dict(row) for row in captains]

    def fetch_leader_board(self):
        conn = get_db_connection()
        curr = conn.cursor()
        data = curr.execute('''
        SELECT 
            t.tournament_id,
            t.name AS tournament_name,
            tm.team_id,
            tm.team_name,
            g.game_name,
            COUNT(m.match_id) AS played,
            SUM(
                CASE WHEN s.winner = tm.team_id THEN 1 ELSE 0 END
            ) AS wins,
            SUM(
                CASE WHEN s.winner IS NOT NULL AND s.winner != tm.team_id THEN 1 ELSE 0 END
            ) AS losses,
            SUM(
                CASE WHEN tm.team_id = m.team_id_1 THEN s.team_score_1
                     WHEN tm.team_id = m.team_id_2 THEN s.team_score_2
                     ELSE 0 END
            ) AS score_for,
            SUM(
                CASE WHEN tm.team_id = m.team_id_1 THEN s.team_score_2
                     WHEN tm.team_id = m.team_id_2 THEN s.team_score_1
                     ELSE 0 END
            ) AS score_against,
            SUM(
                CASE WHEN s.winner = tm.team_id THEN 3 ELSE 0 END
            ) AS points,   -- classic 3 points per win system
            SUM(
                CASE WHEN tm.team_id = m.team_id_1 THEN s.team_score_1
                     WHEN tm.team_id = m.team_id_2 THEN s.team_score_2
                     ELSE 0 END
            ) -
            SUM(
                CASE WHEN tm.team_id = m.team_id_1 THEN s.team_score_2
                     WHEN tm.team_id = m.team_id_2 THEN s.team_score_1
                     ELSE 0 END
            ) AS score_diff
        FROM tournaments t
            JOIN matches m ON t.tournament_id = m.tournament_id
            JOIN scores s ON m.match_id = s.match_id
            JOIN teams tm ON tm.team_id IN (m.team_id_1, m.team_id_2)
            JOIN games g ON tm.game_id  = g.game_id
            WHERE t.tournament_id = ?
            GROUP BY t.tournament_id, t.name, tm.team_id, tm.team_name
            ORDER BY points DESC, score_diff DESC;
            ''',(self.tournament_id,)).fetchall()
        conn.commit()
        conn.close()
        return [dict(row) for row in data]
    def fetch_games(self):
        games = Games(None,None,None)
        listgames = games.list_games()
        return [dict(row) for row in listgames]
    
    def fetch_tournaments(self):
        lists = Tournaments(None,None, None,None,None,None)
        tournaments = lists.list_tournaments()
        return [dict(row) for row in tournaments]
    
    def fetch_matches(self):
        matches = Matches.list_matches(None)
        return matches

    def fetch_teams(self):
        conn = get_db_connection()
        cur = conn.cursor()
        teams = cur.execute('''
        SELECT t.team_id , t.team_name ,t.game_id,g.game_name, u.user_name FROM teams t 
            JOIN users u ON t.team_captain_id = u.user_id
            JOIN games g ON t.game_id = g.game_id
        ''').fetchall()
        conn.close()
        return [dict(row) for row in teams]


if __name__=="__main__":
    data = Fetch_data(None)
    print(data.fetch_users())
    print(data.fetch_user_info())
    print(data.fetch_captain())
    print(data.fetch_games())
    print(data.fetch_teams())
    print(data.fetch_leader_board())
