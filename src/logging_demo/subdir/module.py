import logging

logger = logging.getLogger(__name__)


def hi_from_module():
    logger.info('Hi from subdir')
