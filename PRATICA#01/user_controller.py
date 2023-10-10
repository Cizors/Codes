COUNTER = 0

def authenticator(login, password):
    USERS = [
        {
            
            "login": "test",
            "password": "admin"
        },
        {
            "login": "test2",
            "password": "admin2"
        },
        {
            "login": "test3",
            "password": "admin3"
        },
        {
            "login": "test4",
            "password": "admin4"
        }
    ]

    for USER in USERS:
        if USER['login'] == login and USER['password'] == password:
            print(f"Logged with Success.")
            return
            
    print(f"Invalid Login.")

login = input(f"Login: ")
password = input(f"Password: ")

authenticator(login, password)