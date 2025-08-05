# logger.py

import logging

# Configure global logger
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def log(msg, level="info"):
    """
    Logs a message using the specified log level.
    Supported levels: info, warning, error, debug, critical
    """
    level = level.lower()
    if level == "debug":
        logging.debug(msg)
    elif level == "warning":
        logging.warning(msg)
    elif level == "error":
        logging.error(msg)
    elif level == "critical":
        logging.critical(msg)
    else:
        logging.info(msg)