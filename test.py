import logging
from league import logger_init

logger_init()

class CS1:
    def __init__(self):
        self.logger = logging.getLogger('CS1')

    def testLog(self):
        self.logger.debug('debug test')
        self.logger.info('info test')
        self.logger.warning('warn test')
        self.logger.error('error test')
        self.logger.fatal('fatal test')

class CS2:
    def __init__(self):
        self.logger = logging.getLogger('CS2')

    def testLog(self):
        self.logger.debug('debug test')
        self.logger.info('info test')
        self.logger.warning('warn test')
        self.logger.error('error test')
        self.logger.fatal('fatal test')

cs1 = CS1()
cs2 = CS2()

cs1.testLog()
cs2.testLog()