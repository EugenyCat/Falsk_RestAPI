QUERY_PUT_FAVORITES = """

UPDATE favorites 
SET id = %s,
id_author = %s, 
id_offer = %s
WHERE id = %s; 

"""