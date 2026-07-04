USE ipl_eda;

SELECT winner,
       COUNT(*) AS Total_Wins
FROM matches
GROUP BY winner
HAVING COUNT(*) > 50
ORDER BY Total_Wins DESC;
SELECT city,
       COUNT(*) AS Total_Matches
FROM matches
GROUP BY city
HAVING COUNT(*) > 30
ORDER BY Total_Matches DESC;
SELECT bowler,
       SUM(is_wicket) AS Total_Wickets
FROM deliveries
GROUP BY bowler
ORDER BY Total_Wickets DESC
LIMIT 10;
SELECT batter,
       SUM(batsman_runs) AS Total_Runs
FROM deliveries
GROUP BY batter
ORDER BY Total_Runs DESC
LIMIT 10;
SELECT venue,
       COUNT(*) AS Matches
FROM matches
GROUP BY venue
ORDER BY Matches DESC
LIMIT 10;