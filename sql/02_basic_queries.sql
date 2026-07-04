USE ipl_eda;

-- Total Matches
SELECT COUNT(*) AS Total_Matches
FROM matches;

-- Total Deliveries
SELECT COUNT(*) AS Total_Deliveries
FROM deliveries;

-- Total Seasons
SELECT DISTINCT season
FROM matches
ORDER BY season;

-- Total Cities
SELECT DISTINCT city
FROM matches
ORDER BY city;

-- Matches in Mumbai
SELECT COUNT(*) AS Mumbai_Matches
FROM matches
WHERE city='Mumbai';

-- League Matches
SELECT COUNT(*) AS League_Matches
FROM matches
WHERE match_type='League';

-- Chennai Matches
SELECT *
FROM matches
WHERE city='Chennai'
LIMIT 10;

-- Mumbai Indians Toss Wins
SELECT *
FROM matches
WHERE toss_winner='Mumbai Indians'
LIMIT 10;

-- CSK Wins
SELECT *
FROM matches
WHERE winner='Chennai Super Kings'
LIMIT 10;