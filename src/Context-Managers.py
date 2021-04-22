# Read file in classical way
from src.Logger import logMethod

log = logMethod()
file = open("Config.json", mode='r')
log.info(file.read())
file.close()

with open('Config.json', mode='r') as file:
    log.info(file.read())
