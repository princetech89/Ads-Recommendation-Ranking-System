SELECT ad_id,
       SUM(clicked)*1.0 / COUNT(*) AS ctr
FROM interactions
GROUP BY ad_id;
