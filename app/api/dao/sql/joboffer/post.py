QUERY_POST_JOBOFFER = """

INSERT INTO joboffers  
(author, offer_description, slill_list, title)  
VALUES (%s, %s, %s, %s) ;

"""