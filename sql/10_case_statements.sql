USE ipl_eda;

-- Query 1
SELECT
    toss_winner,
    toss_decision,
    CASE
        WHEN toss_decision = 'bat' THEN 'Bat First'
        WHEN toss_decision = 'field' THEN 'Field First'
        ELSE 'Unknown'
    END AS Decision_Type
FROM matches
LIMIT 10;

-- Query 2
SELECT
    winner,
    result_margin,
    CASE
        WHEN result_margin >= 50 THEN 'Big Win'
        WHEN result_margin BETWEEN 10 AND 49 THEN 'Medium Win'
        WHEN result_margin < 10 THEN 'Close Match'
        ELSE 'No Result'
    END AS Match_Category
FROM matches
LIMIT 20;

-- Query 3
SELECT
    batter,
    batsman_runs,
    CASE
        WHEN batsman_runs = 6 THEN 'Six'
        WHEN batsman_runs = 4 THEN 'Four'
        WHEN batsman_runs = 0 THEN 'Dot Ball'
        ELSE 'Normal Run'
    END AS Shot_Type
FROM deliveries
LIMIT 20;