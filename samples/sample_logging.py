import logging
from src.woodder import Woodder


if __name__ == '__main__':
    project_name = "my_project"
    log_dir = "my_logs"
    Woodder.configure_logging(project_name, log_dir=log_dir)

    logger = logging.getLogger("my-logger")

    logger.info("some info")
    logger.debug("some debug")
    logger.warning("some debug")
    logger.critical("some critical")
    logger.error("some error")
