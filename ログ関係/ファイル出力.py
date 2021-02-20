import logging
import bottle
from bottle_log import LoggingPlugin
from logentries import LogentriesHandler

logging.basicConfig(filename='ログ関係/log/example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')



app = bottle.Bottle()
app.install(LoggingPlugin(app.config))

@app.get('/test')
def test(logger):
    logger.warning('This is only a test')
    return {}


app = bottle.Bottle()
app.install(LoggingPlugin(app.config))
le_handler = LogentriesHandler('logentries-api-token')
logging.getLogger('bottle.exception').addHandler(le_handler)