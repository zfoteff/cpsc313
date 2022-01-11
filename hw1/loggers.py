""" Logging helper class
Options
- MapReduceLogger | Logging object for handling all logging 
"""

import os
import logging as log

LOG_DIR = str(os.getcwd())+"\\logs\\"

def log_setup(logger_name, log_file, mode='w'):
        """
        Logging setup and initialization
        """
        #   Initialize handlers
        new_log = log.getLogger(logger_name)
        formatter = log.Formatter("[%(asctime)s] | %(message)s")
        file_handler = log.FileHandler(log_file, mode=mode)
        file_handler.setFormatter(formatter)
        stream_handler = log.StreamHandler()

        #   Create logging object with handlers
        new_log.setLevel(log.DEBUG)
        new_log.addHandler(file_handler)
        new_log.addHandler(stream_handler)
        return new_log

class DefaultLogger():
    def __init__(self, log="debug", assignment="none"):
        self.log_obj = log_setup(f"{assignment}", LOG_DIR+f"{assignment}"+f"{log}.log")
        
    def log(self, logStr):
        self.log_obj.info(logStr)

class MapReduceLogger(DefaultLogger):
    def __init__(self):
        super().__init__("MapReduceLogger", assignment="hw1")
        
class TestLogger(DefaultLogger):
    def __init__(self, assignment="none"):
        super().__init__("testing", assignment)