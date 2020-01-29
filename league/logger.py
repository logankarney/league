import logging

def logger_init():
    logging.basicConfig(
      filename='game.log',
      format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s',
      datefmt='%H:%M:%S',
      level=logging.DEBUG
    )
    