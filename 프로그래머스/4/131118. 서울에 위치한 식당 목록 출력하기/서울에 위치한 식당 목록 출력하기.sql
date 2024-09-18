SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO I INNER JOIN REST_REVIEW R
ON I.REST_ID = R.REST_ID
GROUP BY I.REST_ID
HAVING ADDRESS LIKE "서울%"
ORDER BY SCORE DESC, FAVORITES DESC;
