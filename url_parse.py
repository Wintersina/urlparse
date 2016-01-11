
# -----------------------------------------------
# This project should be completed using the
# Python programming language.
#
# Problem:
#----------
# Please parse the following URL into parts:
#     http://www.vandyhacks.org/dostuff/now
#
# While you've been given a specific URL
# Your solution should work for any valid
# URL.  Below is a skeleton and some test
# code.  You're job is to fill in the
# implmentation of the parse_url() function.
#
# parse_url() should return a python
# dictionary with the following keys
#
#    * scheme
#    * host
#    * path
#
# NOTE: there are a number of solutions to
# this problem including pre-built modules
# like urlparse.
#
# Your solution should display your ability
# to create efficient readable code that
# solves the problem without using pre-built
# libraries directly related to parsing URLs
#
# If you provide multiple ways to solve the
# problem that isn't a bad thing.
# -----------------------------------------------
the_url = "http://www.vandyhacks.org/dostuff/now"

def parse_url(url):
    #  make sure your solution is valid
    #  for NOT JUST the test URL. I will
    #  be testing with others.
    
    # your code goes here.

    # do not solve using split()

    # unitl you add code execution will fail with
    #  an 'IndentationError' until you start to fill
    #  in this function.










# -----------------------------------------------
#  TEST CODE AND MAIN
# -----------------------------------------------
def test_parse_url(url_dict):
    if type(url_dict) != dict:
        print "FAIL: you need to return a Dictionary from parse_url()"
        return

    the_keys = url_dict.keys()
    if not 'scheme' in the_keys:
        print "FAIL: your dictionary is missing the key 'scheme'"
        return

    if not 'host' in the_keys:
        print "FAIL: your dictionary is missing the key 'host'"
        return

    if not 'path' in the_keys:
        print "FAIL: your dictionary is missing the key 'path'"
        return

    if url_dict.get('scheme') != "http":
        print "FAIL: key: 'scheme' should be 'http'"
        return

    if url_dict.get('host') != "www.vandyhacks.org":
        print "FAIL: key: 'host' should be 'www.vandyhacks.org'"
        return

    if url_dict.get('path') != "dostuff/now":
        print "FAIL: key: 'path' should be 'dostuff/now'"
        return

    print "WELL DONE YOU PASSED -- !!"


parsed_url = parse_url(the_url)
test_parse_url(parsed_url)
