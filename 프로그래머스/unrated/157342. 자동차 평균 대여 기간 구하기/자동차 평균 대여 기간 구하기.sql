-- 코드를 입력하세요
SELECT CAR_ID, ROUND(AVG(TIMESTAMPDIFF(DAY,START_DATE,END_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS T1
JOIN (SELECT CAR_ID, TIMESTAMPDIFF(DAY,START_DATE,END_DATE) FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY)
    AS T2 USING (CAR_ID)
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC
;