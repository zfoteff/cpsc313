""" Main file for testing the HW1 implementation
"""

__version__ = '0.1'
__author__ = 'Zac Foteff'

import io
from Loggers import TestLogger

logger = TestLogger("hw1")

def test_assert_true():
    logger.log("True assertion test")
    assert(True) == True

def test_assert_false():
    logger.log("False assertion test")
    assert(False) == False