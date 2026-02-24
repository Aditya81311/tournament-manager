from main import get_db_connection

conn = get_db_connection()
curr = conn.cursor()


data = curr.execute('''
         SELECT 
                m.match_id,
                t.name,
                m.match_no,
                m.round_no,
                tm1.team_name As team_1,
                tm2.team_name As team_2,
                m.scheduled_at,
                m.status
            FROM matches m
            JOIN tournaments t ON m.tournament_id = t.tournament_id
            JOIN teams tm1  ON m.team_id_1 = tm1.team_id
            JOIN teams tm2  ON m.team_id_2 = tm2.team_id
            ORDER BY scheduled_at DESC
        ''', )

print([dict(row) for row in data])

conn.commit()
conn.close()

# INSERT INTO teams(team_name ,game_id ,team_captain_id) VALUES("zakanzulya2", 2, 1)