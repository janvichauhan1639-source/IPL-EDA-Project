USE ipl_eda;

WITH BatterRuns AS
(
    SELECT
        batter,
        SUM(batsman_runs) AS Total_Runs
    FROM deliveries
    GROUP BY batter
)

SELECT *
FROM BatterRuns
ORDER BY Total_Runs DESC
LIMIT 5;
WITH BowlerWickets AS
(
    SELECT
        bowler,
        SUM(is_wicket) AS Wickets
    FROM deliveries
    GROUP BY bowler
)

SELECT *
FROM BowlerWickets
ORDER BY Wickets DESC
LIMIT 5;
WITH TeamWins AS
(
    SELECT
        winner,
        COUNT(*) AS Wins
    FROM matches
    GROUP BY winner
)

SELECT *
FROM TeamWins
WHERE Wins > 100
ORDER BY Wins DESC;
WITH SeasonRuns AS
(
    SELECT
        m.season,
        SUM(d.total_runs) AS Runs
    FROM matches m
    JOIN deliveries d
        ON m.id = d.match_id
    GROUP BY m.season
)

SELECT *
FROM SeasonRuns
ORDER BY Runs DESC
LIMIT 1;
WITH VenueStats AS
(
    SELECT
        venue,
        COUNT(*) AS Matches
    FROM matches
    GROUP BY venue
)

SELECT *
FROM VenueStats
ORDER BY Matches DESC
LIMIT 10;