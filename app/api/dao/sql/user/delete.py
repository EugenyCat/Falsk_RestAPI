QUERY_DELETE_USER = """

DELETE FROM users 
WHERE email = %s;

"""