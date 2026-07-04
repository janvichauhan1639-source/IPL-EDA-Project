USE ipl_eda;

SELECT
    m.season,
    SUM(d.total_runs) AS Total_Runs
FROM matches m
JOIN deliveries d
ON m.id = d.match_id
GROUP BY m.season
ORDER BY m.season;
SELECT
    d.batting_team,
    SUM(d.total_runs) AS Runs
FROM deliveries d
GROUP BY d.batting_team
ORDER BY Runs DESC;
SELECT
    batter,
    SUM(batsman_runs) AS Runs
FROM deliveries
GROUP BY batter
ORDER BY Runs DESC
LIMIT 10;
SELECT
    bowler,
    SUM(is_wicket) AS Wickets
FROM deliveries
GROUP BY bowler
ORDER BY Wickets DESC
LIMIT 10;
SELECT
    m.season,
    COUNT(*) AS Sixes
FROM matches m
JOIN deliveries d
ON m.id = d.match_id
WHERE d.batsman_runs = 6
GROUP BY m.season
ORDER BY m.season;
SELECT
    m.season,
    COUNT(*) AS Fours
FROM matches m
JOIN deliveries d
ON m.id = d.match_id
WHERE d.batsman_runs = 4
GROUP BY m.season
ORDER BY m.season;
SELECT
    m.venue,
    SUM(d.total_runs) AS Total_Runs
FROM matches m
JOIN deliveries d
ON m.id = d.match_id
GROUP BY m.venue
ORDER BY Total_Runs DESC
LIMIT 10;
SELECT
    winner,
    COUNT(*) AS Wins
FROM matches
GROUP BY winner
ORDER BY Wins DESC;