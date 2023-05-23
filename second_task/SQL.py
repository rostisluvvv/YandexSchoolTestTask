"""
WITH RECURSIVE r AS (
	SELECT req.request_id, req.parent_request_id, request_id as base_request_id
	FROM requests AS req
	WHERE parent_request_id IS NULL AND req.type = 'RequestReceived'

	UNION

	SELECT req.request_id, req.parent_request_id, r.base_request_id
	FROM requests AS req
	JOIN r
	ON req.parent_request_id = r.request_id
)

SELECT EXTRACT(EPOCH FROM AVG(sum_dt)) AS avg_network_time_ms FROM (
SELECT SUM(dt)*1000 sum_dt FROM (
SELECT sent.*, r.base_request_id, receive.datetime - sent.datetime AS dt
FROM requests AS sent
JOIN r ON sent.request_id = r.request_id
JOIN requests AS receive ON receive.type = 'RequestReceived' AND receive.host = sent.data
JOIN r AS rr ON rr.request_id = receive.request_id  AND rr.base_request_id = r.base_request_id
WHERE sent.type = 'RequestSent'

UNION

SELECT sent.*, r.base_request_id, receive.datetime - sent.datetime AS dt
FROM requests AS sent
JOIN r ON sent.request_id = r.request_id
JOIN requests AS receive ON receive.type = 'ResponseReceived' AND sent.host = split_part(receive.data, '	', 1)
JOIN r AS rr ON rr.request_id = receive.request_id  AND rr.base_request_id = r.base_request_id
WHERE sent.type = 'ResponseSent'
) AS summary_dt
GROUP BY summary_dt.base_request_id
) AS result
"""