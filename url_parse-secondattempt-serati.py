
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


#   global variable used for parsing test
#   original test
the_url = "http://www.vandyhacks.org/dostuff/now"


#   testing with other urls
urltest1 = "https://github.com/Wintersina/urlparse"
urltest2 = "file://wmpt.eventbrite.com/d/tn--franklin/events/?cr=80034795249&gclid=CjwKEAiAws20BRCs-P-ssLbSlg4SJABbVcDp-Bop8X0-FR5ErTluXMzD9QfB06JzwCoCn01WaIWxFBoCM6Pw_wcB&kw=eventbrite+ex&mkwid=s%5Buniq_id%5D_dc&pcrid=80034795249&pkw=eventbrite&plc=&pmt=e&ref=sem0brd0ggl0usa0ppca0brand0mobile"
#   test with no path
urltest3 = "https://www.yourprimer.io"
#   test with no scheme
urltest4 = "www.google.com/mail"
urltest5 = "www.stackoverflow.net"
urltest6 = "bogusdogusScheme://www.yourwebpage.com/path"

#   Sina Serati
#   1/13/2016
#   Using Python 2.7.1
#   Writing a parse function to split(not using split)
#       the http:// into scheme www.domain.com into host
#       and the rest into path
#   leaving all original comments.
#   adding some more test code above
#   This second attempt will have helper methods, better, readable code.

# this helper fuction just determines if there is a scheme entered or not
def s_schemeCheck(url):
    if "://" in url:
        return True
    else:
        return False
#this helper fucntion parses the scheme and returns the resutls to a variable
def s_parseScheme(url, check):
    if check:
        pos = url.index("://")  #getting pos
        scheme = url[0:pos]
        return scheme
    else:
        return "There is no Scheme"
#this function just parses out the URL
def s_parseHost(url):
    if "://" in url:
        pos = url.index(":")
        host = url[pos+3:]
        if "/" in host:
            pos = host.index("/")
            host = host[:pos]
        return host
    else:
        if "/" in url:
            pos = url.index("/")
        else:
            pos = len(url)
        host = url[0:pos]
        return host
#this function just parses out the path
def s_parsePath(url):
    if url.count("/")>=3:
        pos = url.index(".")
        path = url[pos:]
        pos = path.index("/")
        path = path[pos+1:]
    else:
        if "://" in url:
            pos = url.index(".")
            path = url[pos:]
            if "/" in path:
                pos = path.index("/")
                path = path[pos:0]
            else:
                path = ''
        else:
            if "/" in url:
                pos = url.index("/")
                path = url[pos+1:]
            else:
                path = ''
    
    return path

def parse_url(url):

    checker = s_schemeCheck(url)        #will check if a scheme is exsistant returns true or false
    sch = s_parseScheme(url, checker)   #will parse only the scheme and return the remaining url
    hos = s_parseHost(url)              #will parse only the host
    pth = s_parsePath(url)              #will parse only the path

    # dictionary is created being returned
    data = {'scheme': sch,'host': hos,'path' : pth}
    return data


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

# main code
parsed_url = parse_url(the_url)
test_parse_url(parsed_url)
