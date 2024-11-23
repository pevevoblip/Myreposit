from doctest import debug
from logging import *
from logging import DEBUG

from django.db.backends.base.schema import logger

from logger import Logger
logger = Logger('filelog.log', 10)
logger.log('debug message')
logger.log('info message')
logger.log('warning message')
logger.log('error message')
logger.log('critical message')