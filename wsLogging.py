import logging

def logger_create(mod_name):

    # Create Logger
    logger = logging.getLogger(mod_name)

    # Logging file handler
    fh = logging.FileHandler(mod_name)

    # Format create/Format set
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add handler to logger object
    logger.addHandler(fh)

    # Returns logger to Error or Audits
    return logger


def error_logging(mod_name, error):

    #Create Error logger for the mod
    logger = logger_create(mod_name)

    # Sets Logger's level
    logger.setLevel(logging.ERROR)

    # Record ERROR message
    logger.error(error)


def audit_logging(mod_name, info):

    #Create Audit logger for the mod
    logger = logger_create(mod_name)

    # Sets Logger's level
    logger.setLevel(logging.INFO)

    # Record ERROR message
    logger.info(info)


