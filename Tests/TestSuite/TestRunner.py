# https://docs.python.org/3/library/unittest.html#classes-and-functions
# Refer https://testtools.readthedocs.io/en/latest/api.html for more information\

# Note to self, I put chromedriver here: C:\Windows

from unittest import TestLoader, TestSuite, TextTestRunner
import sys
import os

# getting the name of the directory where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to the sys.path.
sys.path.append(parent)

from Scripts.test_Home_Page import DemoHomePage
from Scripts.test_Contact_Us_Page import DemoContactPage

load1 = TestLoader().loadTestsFromTestCase(DemoHomePage)
load2 = TestLoader().loadTestsFromTestCase(DemoContactPage)

# Test Suite is used since there are multiple test cases
# Passing in tuple because TestSuite argument has to be one
test_suite = TestSuite((load1,load2))
test_runner = TextTestRunner(verbosity=2)
test_runner.run(test_suite)
