from main import get_db_connection

conn = get_db_connection()
curr = conn.cursor()


data = curr.execute('''
    SELECT t.team_id , t.team_name , g.game_name , u.user_name  FROM team_members tm
        JOIN teams t ON tm.team_id = t.team_id
        JOIN users u ON t.team_captain_id = u.user_id
        JOIN games g ON t.game_id = g.game_id
        ''', )

print([dict(row) for row in data])

conn.commit()
conn.close()

# INSERT INTO teams(team_name ,game_id ,team_captain_id) VALUES("zakanzulya2", 2, 1)