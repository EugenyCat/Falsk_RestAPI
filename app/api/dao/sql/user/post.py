QUERY_POST_USER = """

INSERT INTO users 
(name, email, password, account_type, role) 
VALUES (%s, %s, %s, %s, %s)

"""