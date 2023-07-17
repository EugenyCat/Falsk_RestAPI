QUERY_POST_FAVORITES = """

INSERT INTO favorites  
(id, id_author, id_offer)  
VALUES (%s, %s, %s) ;

"""