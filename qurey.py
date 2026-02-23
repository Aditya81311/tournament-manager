from main import get_db_connection

conn = get_db_connection()
curr = conn.cursor()


data = curr.execute('''
UPDATE teams 
            SET team_name = ?, game_id = ?, team_captain_id = ? 
            WHERE team_id = ?
        ''', ("zakanzulya",2 ,1 ,1))

# print([dict(row) for row in data])

conn.commit()
conn.close()

# INSERT INTO teams(team_name ,game_id ,team_captain_id) VALUES("zakanzulya2", 2, 1)