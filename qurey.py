from main import get_db_connection

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

        ''',(tournament_id,))

print([dict(row) for row in data])

conn.commit()
conn.close()

# INSERT INTO teams(team_name ,game_id ,team_captain_id) VALUES("zakanzulya2", 2, 1)