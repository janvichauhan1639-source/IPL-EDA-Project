USE ipl_eda;

-- ==========================================
-- 1. Which team has won the most IPL matches?
-- ==========================================

SELECT
    winner,
    COUNT(*) AS Total_Wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY Total_Wins DESC;



-- ==========================================
-- 2. Top 10 Player of the Match winners
-- ==========================================

SELECT
    player_of_match,
    COUNT(*) AS Awards
FROM matches
WHERE player_of_match IS NOT NULL
GROUP BY player_of_match
ORDER BY Awards DESC
LIMIT 10;



-- ==========================================
-- 3. Which venue hosted the most matches?
-- ==========================================

SELECT
    venue,
    COUNT(*) AS Matches_Played
FROM matches
GROUP BY venue
ORDER BY Matches_Played DESC;



-- ==========================================
-- 4. Toss Decision Analysis
-- ==========================================

SELECT
    toss_decision,
    COUNT(*) AS Total
FROM matches
GROUP BY toss_decision;



-- ==========================================
-- 5. Toss Winners
-- ==========================================

SELECT
    toss_winner,
    COUNT(*) AS Toss_Wins
FROM matches
GROUP BY toss_winner
ORDER BY Toss_Wins DESC;



-- ==========================================
-- 6. Total Runs by Batting Team
-- ==========================================

SELECT
    batting_team,
    SUM(total_runs) AS Total_Runs
FROM deliveries
GROUP BY batting_team
ORDER BY Total_Runs DESC;



-- ==========================================
-- 7. Top 10 Run Scorers
-- ==========================================

SELECT
    batter,
    SUM(batsman_runs) AS Runs
FROM deliveries
GROUP BY batter
ORDER BY Runs DESC
LIMIT 10;



-- ==========================================
-- 8. Top 10 Wicket Takers
-- ==========================================

SELECT
    bowler,
    COUNT(*) AS Wickets
FROM deliveries
WHERE is_wicket = 1
GROUP BY bowler
ORDER BY Wickets DESC
LIMIT 10;



-- ==========================================
-- 9. Most Successful City
-- ==========================================

SELECT
    city,
    COUNT(*) AS Matches
FROM matches
GROUP BY city
ORDER BY Matches DESC;



-- ==========================================
-- 10. Super Over Matches
-- ==========================================

SELECT
    COUNT(*) AS Super_Over_Matches
FROM matches
WHERE super_over='Y';