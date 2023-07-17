QUERY_GET_JOBOFFER = """

SELECT *
FROM joboffers jo 
WHERE jo.id = %s

"""