def practice(message = None):
    message = 'no message' if message is None else message
    print(message)

def practice(message = None):
    if message is None: message = 'no message'
    print(message)

'''
class hoge(object):
  message = 'no message'

  def practice(message = None):
    if message is None: message = self.message
'''

def practice(message = None):
    print(message or 'No message')