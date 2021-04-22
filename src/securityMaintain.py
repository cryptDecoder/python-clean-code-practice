from src.Logger import logMethod

log = logMethod()
log.info("Welcome")
# String formatting

CONFIG = {
    "API_KEY": "secret_key"
}


class User:
    name = ""
    email = ""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name, self.email


name = "Tony"
email = "Tony@s.com"

user = User(name, email)
log.info(f"{CONFIG['API_KEY']}")
