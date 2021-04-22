import json
import os
import sys

from src.Logger import logMethod as logger

log = logger()
log.error("This is error message")
log.critical("This is critical")
log.info("This is info")
log.warning("This is warning")

cfg_file = os.path.join(sys.path[0], 'Config.json')
with open(cfg_file) as f:
    config = json.load(f)
f.close()
id = config['id']
log.info(f"{id}")
log.error(f"{config['name ']}")
