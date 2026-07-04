USE ipl_eda;

SELECT
    batter,
    SUM(batsman_runs) AS Runs,
    RANK() OVER (
        ORDER BY SUM(batsman_runs) DESC
    ) AS Player_Rank
FROM deliveries
GROUP BY batter;
SELECT
    batter,
    SUM(batsman_runs) AS Runs,
    DENSE_RANK() OVER(
        ORDER BY SUM(batsman_runs) DESC
    ) AS DenseRank
FROM deliveries
GROUP BY batter;
SELECT
    batter,
    SUM(batsman_runs) AS Runs,
    ROW_NUMBER() OVER(
        ORDER BY SUM(batsman_runs) DESC
    ) AS RowNum
FROM deliveries
GROUP BY batter;
SELECT
    winner,
    COUNT(*) AS Wins,
    RANK() OVER(
        ORDER BY COUNT(*) DESC
    ) AS TeamRank
FROM matches
GROUP BY winner;
SELECT
    match_id,
    batter,
    batsman_runs,
    SUM(batsman_runs)
    OVER(
        PARTITION BY match_id
        ORDER BY over_no, ball
    ) AS RunningScore
FROM deliveries;
SELECT
    match_id,
    over_no,
    ball,
    batsman_runs,

    LAG(batsman_runs)
    OVER(
        PARTITION BY match_id
        ORDER BY over_no, ball
    ) AS PreviousBall
FROM deliveries;
SELECT
    match_id,
    over_no,
    ball,
    batsman_runs,

    LEAD(batsman_runs)
    OVER(
        PARTITION BY match_id
        ORDER BY over_no, ball
    ) AS NextBall
FROM deliveries;