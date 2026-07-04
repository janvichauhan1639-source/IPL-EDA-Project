USE ipl_eda;

-- Season Wise Matches

SELECT season,
       COUNT(*) AS Total_Matches
FROM matches
GROUP BY season
ORDER BY season;
-- City Wise Matches

SELECT city,
       COUNT(*) AS Total_Matches
FROM matches
GROUP BY city
ORDER BY Total_Matches DESC;
-- Match Type Count

SELECT match_type,
       COUNT(*) AS Total
FROM matches
GROUP BY match_type;
-- Toss Decision

SELECT toss_decision,
       COUNT(*) AS Total
FROM matches
GROUP BY toss_decision;
-- Most Successful Teams

SELECT winner,
       COUNT(*) AS Wins
FROM matches
GROUP BY winner
ORDER BY Wins DESC;