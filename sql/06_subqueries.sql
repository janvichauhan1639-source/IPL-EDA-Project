USE ipl_eda;

SELECT *
FROM matches
WHERE id = (
    SELECT match_id
    FROM deliveries
    GROUP BY match_id
    ORDER BY SUM(total_runs) DESC
    LIMIT 1
);
SELECT batter,
       SUM(batsman_runs) AS Runs
FROM deliveries
GROUP BY batter
HAVING SUM(batsman_runs) = (
    SELECT MAX(Total_Runs)
    FROM (
        SELECT SUM(batsman_runs) AS Total_Runs
        FROM deliveries
        GROUP BY batter
    ) AS t
);
SELECT bowler,
       SUM(is_wicket) AS Wickets
FROM deliveries
GROUP BY bowler
HAVING SUM(is_wicket) = (
    SELECT MAX(Total_Wickets)
    FROM (
        SELECT SUM(is_wicket) AS Total_Wickets
        FROM deliveries
        GROUP BY bowler
    ) AS t
);
SELECT winner,
       COUNT(*) AS Wins
FROM matches
GROUP BY winner
HAVING COUNT(*) = (
    SELECT MAX(Total_Wins)
    FROM (
        SELECT COUNT(*) AS Total_Wins
        FROM matches
        GROUP BY winner
    ) AS t
);
SELECT venue,
       SUM(total_runs) AS Runs
FROM matches m
JOIN deliveries d
ON m.id = d.match_id
GROUP BY venue
HAVING SUM(total_runs) = (
    SELECT MAX(Total_Runs)
    FROM (
        SELECT SUM(d.total_runs) AS Total_Runs
        FROM matches m
        JOIN deliveries d
        ON m.id = d.match_id
        GROUP BY venue
    ) AS t
);
SELECT season,
       COUNT(*) AS Matches
FROM matches
GROUP BY season
HAVING COUNT(*) >
(
    SELECT AVG(Total_Matches)
    FROM (
        SELECT COUNT(*) AS Total_Matches
        FROM matches
        GROUP BY season
    ) AS t
);