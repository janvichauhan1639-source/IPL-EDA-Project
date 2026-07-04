USE ipl_eda;

-- ==========================================
-- 1. INNER JOIN
-- ==========================================

SELECT
    m.id,
    m.winner,
    d.batter,
    d.total_runs
FROM matches m
INNER JOIN deliveries d
ON m.id = d.match_id
LIMIT 20;



-- ==========================================
-- 2. LEFT JOIN
-- ==========================================

SELECT
    m.id,
    m.city,
    d.batter
FROM matches m
LEFT JOIN deliveries d
ON m.id = d.match_id
LIMIT 20;



-- ==========================================
-- 3. Match having Maximum Runs
-- ==========================================

SELECT
    match_id,
    SUM(total_runs) AS Runs
FROM deliveries
GROUP BY match_id
ORDER BY Runs DESC
LIMIT 1;



-- ==========================================
-- 4. Top Run Scorer
-- ==========================================

SELECT
    batter,
    SUM(batsman_runs) AS Runs
FROM deliveries
GROUP BY batter
ORDER BY Runs DESC
LIMIT 1;



-- ==========================================
-- 5. Top Wicket Taker
-- ==========================================

SELECT
    bowler,
    COUNT(*) AS Wickets
FROM deliveries
WHERE is_wicket=1
GROUP BY bowler
ORDER BY Wickets DESC
LIMIT 1;



-- ==========================================
-- 6. Highest Team Score
-- ==========================================

SELECT
    match_id,
    inning,
    batting_team,
    SUM(total_runs) AS Score
FROM deliveries
GROUP BY match_id, inning, batting_team
ORDER BY Score DESC
LIMIT 10;



-- ==========================================
-- 7. Lowest Team Score
-- ==========================================

SELECT
    match_id,
    inning,
    batting_team,
    SUM(total_runs) AS Score
FROM deliveries
GROUP BY match_id, inning, batting_team
ORDER BY Score
LIMIT 10;



-- ==========================================
-- 8. Most Sixes
-- ==========================================

SELECT
    batter,
    COUNT(*) AS Sixes
FROM deliveries
WHERE batsman_runs=6
GROUP BY batter
ORDER BY Sixes DESC
LIMIT 10;



-- ==========================================
-- 9. Most Fours
-- ==========================================

SELECT
    batter,
    COUNT(*) AS Fours
FROM deliveries
WHERE batsman_runs=4
GROUP BY batter
ORDER BY Fours DESC
LIMIT 10;



-- ==========================================
-- 10. Economy Rate
-- ==========================================

SELECT
    bowler,
    ROUND(SUM(total_runs)/(COUNT(*)/6),2) AS Economy
FROM deliveries
GROUP BY bowler
HAVING COUNT(*)>120
ORDER BY Economy
LIMIT 10;



-- ==========================================
-- 11. Strike Rate
-- ==========================================

SELECT
    batter,
    ROUND((SUM(batsman_runs)*100)/COUNT(*),2) AS StrikeRate
FROM deliveries
GROUP BY batter
HAVING COUNT(*)>100
ORDER BY StrikeRate DESC
LIMIT 10;



-- ==========================================
-- 12. Orange Cap (Most Runs)
-- ==========================================

SELECT
    batter,
    SUM(batsman_runs) AS Runs
FROM deliveries
GROUP BY batter
ORDER BY Runs DESC
LIMIT 10;



-- ==========================================
-- 13. Purple Cap (Most Wickets)
-- ==========================================

SELECT
    bowler,
    COUNT(*) AS Wickets
FROM deliveries
WHERE is_wicket=1
GROUP BY bowler
ORDER BY Wickets DESC
LIMIT 10;



-- ==========================================
-- 14. Team Winning Percentage
-- ==========================================

SELECT
    winner,
    COUNT(*)*100/(SELECT COUNT(*) FROM matches) AS Win_Percentage
FROM matches
GROUP BY winner
ORDER BY Win_Percentage DESC;



-- ==========================================
-- 15. Average First Innings Score
-- ==========================================

SELECT
    AVG(Score) AS Avg_First_Innings
FROM
(
    SELECT
        match_id,
        SUM(total_runs) AS Score
    FROM deliveries
    WHERE inning=1
    GROUP BY match_id
) t;