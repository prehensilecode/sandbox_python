#!/usr/bin/env python3.5
import sys
import os
import logging

def getLogFileHandles(logger):
    """ Get a list of filehandle numbers from logger
        to be handed to DaemonContext.files_preserve
    """
    handles = []
    for handler in logger.handlers:
        handles.append(handler.stream.fileno())
    if logger.parent:
        handles += getLogFileHandles(logger.parent)
    return handles

def main():
    logger = logging.getLogger('foobar')
    logger.setLevel(logging.INFO)

    #handler = logging.FileHandler('/local/scratch/dwc62/hellboy/hellboy.log')
    handler = logging.FileHandler('/local/scratch/dwc62/hellboy/foobar.log')
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    print("handler.stream.fileno() = {}".format(handler.stream.fileno()))

    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

    handles = getLogFileHandles(logger)
    print("handles = ...")
    print(handles)


if __name__ == '__main__':
    main()

