'''
logging ライブラリはモジュール方式のアプローチを取り、いくつかのカテゴリの部品を提供します。ロガー、ハンドラ、フィルタ、フォーマッタです。
    ・ロガーは、アプリケーションコードが直接使うインターフェースを公開します。
    ・ハンドラは、(ロガーによって生成された) ログ記録を適切な送信先に送ります。
    ・フィルタは、どのログ記録を出力するかを決定する、きめ細かい機能を提供します。
    ・フォーマッタは、ログ記録が最終的に出力されるレイアウトを指定します。
'''
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')