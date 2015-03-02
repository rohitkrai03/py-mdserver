
from nose.tools import *
import sys
sys.path.append('D:\Rohit\Projects\MDGen')
from mdgen import utils

def test_troll_directories():
	# given a directory, return all of its contents
    results = grep.troll_directories(".")
    # assert that we have same contents
    assert_true('./tests/grep_tests.py' in results)


    
