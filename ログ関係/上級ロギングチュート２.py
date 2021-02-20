import logging
import logging.config

logging.config.fileConfig('ログ関係/logging.conf')

logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')