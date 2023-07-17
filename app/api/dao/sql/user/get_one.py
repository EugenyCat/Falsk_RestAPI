QUERY_GET_USER_BY_EMAIL = """

SELECT * FROM users u where u.email = %s

"""