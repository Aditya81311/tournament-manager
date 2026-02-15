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
    def __init__(self, team_id, team_name, number_members, game, team_captain):
               self.team_id = team_id
               self.team_name = team_name
               self.number_members = number_members
               self.game = game
               self.team_captain = team_captain
               
    def create_team(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO teams(team_name, number_members, game, team_captain) 
            VALUES(?,?,?,?)
        ''', (self.team_name, self.number_members, self.game, self.team_captain))
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
                number_members,
                game,
                team_captain,
                game,
                team_captain
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
            SET team_name = ?, number_members = ?, game = ?, team_captain = ? 
            WHERE team_id = ?
        ''', (self.team_name, self.number_members, self.game, self.team_captain, self.team_id))
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
  
class Games():
    def __init__(self,game_id,game_name,game_gener):
        self.game_id = game_id
        self.game_name = game_name
        self.game_gener = game_gener
    
    def add_game(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        INSERT INTO games(game_name,game_gener)
        VALUES(?,?)
        ''',(self.game_name,self.game_gener))
        conn.commit()
        conn.close()
    
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
        UPDATE games SET game_name = ?,game_gener = ? 
         WHERE game_id = ?
        ''',(self.game_name,self.game_gener,self.game_id))
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
    def __init__(self, match_id, tournament_id, match_no, round_no, scheduled_at, status):
        self.match_id = match_id
        self.tournament_id = tournament_id
        self.match_no = match_no
        self.round_no = round_no 
        self.scheduled_at = scheduled_at
        self.status = status
        
    def add_match(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        INSERT INTO matches(tournament_id, match_no, round_no, scheduled_at, status)
        VALUES(?,?,?,?,?)
        ''', (self.tournament_id, self.match_no, self.round_no, self.scheduled_at, self.status))
        conn.commit()
        conn.close()

    def list_matches(self):
        conn = get_db_connection()
        cur = conn.cursor()
        matches = cur.execute('''
            SELECT 
                match_id,
                tournament_id,
                match_no,
                round_no,
                scheduled_at,
                status
            FROM matches
            ORDER BY scheduled_at DESC
        ''').fetchall()
        conn.close()
        return matches
        
    def update_match(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
        UPDATE matches 
        SET round_no = ?, scheduled_at = ?, status = ?
        WHERE match_id = ?
        ''', (self.round_no, self.scheduled_at, self.status, self.match_id))
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