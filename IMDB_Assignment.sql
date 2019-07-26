4. SELECT DISTINCT(NAME) FROM PERSON WHERE PID IN (SELECT PID FROM M_DIRECTOR GROUP BY PID HAVING COUNT(MID) > 10)

5.a SELECT COUNT(MID),YEAR FROM MOVIE WHERE MID IN (SELECT MID FROM M_CAST WHERE PID IN (SELECT PID FROM PERSON WHERE GENDER='Female')) GROUp BY year
5.b SELECT COUNT(MID),YEAR FROM MOVIE WHERE MID IN (SELECT MID FROM M_CAST WHERE PID NOT IN (SELECT PID FROM PERSON WHERE GENDER='Female')) GROUp BY year;
    SELECT COUNT(MID),YEAR FROM MOVIE  GROUp BY year

-- http://www.sqlitetutorial.net/sqlite-max/
-- https://www.guru99.com/group-by.html
6.  SELECT MAX(SCORE),MID FROM (SELECt MID,COUNT(DISTINCT(PID)) as SCORE FROM M_CAST GROUP BY MID)
    SELECT title FROM MOVIE WHERE MID = 'tt5164214'

-- https://stackoverflow.com/questions/51609285/sql-query-for-find-the-decade-with-the-largest-number-of-records
7. select y.year as decade_start, y.year + 9 as decade_end,
       count(*) as num_movies
from (select distinct year from movie) y join
     movie m
     on m.year >= y.year and m.year < y.year + 10
group by y.year
order by count(*) desc
limit 1;