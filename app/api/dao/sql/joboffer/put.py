QUERY_PUT_JOBOFFER = """

UPDATE joboffers 
SET author = %s, 
offer_description = %s, 
slill_list = %s, 
title = %s 
WHERE id = %s; 

"""