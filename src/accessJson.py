import json
import os
import sys

from src.Logger import logMethod

log = logMethod()
# slurp credentials
cfg_file = os.path.join(sys.path[0], "Config.json")
with open(cfg_file, 'r') as f:
    config = json.load(f)
f.close()

id = config['id']
print(id)

name = config['name']
log.info("Hello")
log.error("This error message")

