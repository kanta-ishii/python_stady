from logging import getLogger
from logging import StreamHandler
from logging import DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

logger.debug('hello')
