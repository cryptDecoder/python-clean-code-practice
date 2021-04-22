from src.Logger import logMethod

log = logMethod()


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User:{self.name}'

    def __gt__(self, other_user):
        if self.age > other_user.age:
            log.info(f'{self.name} is older than {other_user.name}')
        else:
            log.info(f"{self.name} is younger than {other_user.name}")


john = User("John", 34)
ana = User("ana", 23)
log.info(john)

john > ana

john < ana
