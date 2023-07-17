QUERY_PUT_USER = """

UPDATE users 
SET name = %s,
second_name = %s,
country = %s,
city = %s,
birthday = %s,
gender = %s,
phone_number = %s
WHERE email = %s;

"""