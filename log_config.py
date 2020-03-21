import logging

def set_log_level(loglevel):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(
        level=numeric_level, format='%(asctime)s :: %(name)s :: %(levelname)s :: %(funcName)s :: %(message)s', datefmt='[%d/%m/%Y %H:%M:%S]')
