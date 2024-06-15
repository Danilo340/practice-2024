import re

def validate_email(email):
    email_struckture = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-]+$'
    if re.match(email_struckture, email):
        return True
    else:
        return False



# Тест-кейс 1
print(validate_email("example@gmail.com"))

# Тест-кейс 2
print(validate_email("invalid-email"))

# Тест-кейс 3
print(validate_email("test.email@domain.com"))

# Тест-кейс 4
print(validate_email("user@12"))