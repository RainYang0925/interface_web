import logging.config

from interface_platform.datalayer.log import set_log_filename

filename = 'new_log.txt'
set_log_filename(filename)
logger = logging.getLogger('file_log')
logger.info('hello-logger')


