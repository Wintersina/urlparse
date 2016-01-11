
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
urltest2 = "https://www.eventbrite.com/d/tn--franklin/events/?cr=80034795249&gclid=CjwKEAiAws20BRCs-P-ssLbSlg4SJABbVcDp-Bop8X0-FR5ErTluXMzD9QfB06JzwCoCn01WaIWxFBoCM6Pw_wcB&kw=eventbrite+ex&mkwid=s%5Buniq_id%5D_dc&pcrid=80034795249&pkw=eventbrite&plc=&pmt=e&ref=sem0brd0ggl0usa0ppca0brand0mobile"
#   test with no path
urltest3 = "https://www.yourprimer.com"
#   test with no scheme
urltest4 = "www.google.com/mail"


#   Sina Serati
#   1/13/2016
#   Using Python 2.7.1
#   Writing a parse function to split(not using split)
#       the http:// into scheme www.domain.com into host
#       and the rest into path
#   leaving all original comments.
#   adding some more test code above

def parse_url(url):

    # your code goes here.

    #----- Test Code --- #
    #sch = "http"
    #hos = "www.vandyhacks.org"
    #pth = "dostuff/now"
    # ---------------------

    #defining end position
    end = len(url)
    #local variables
    i = 0
    sch =""         #scheme variable
    hos =""         #host variable
    pth =""         #path variable
    ch =''          #used for traversing
    flag = False    #used for incase there is no scheme

    #getting scheme
    while ch != ':' and i != end-1:
        ch=url[i+1]
        sch+=url[i]
        i= i+1

    #check to make sure there was no scheme
    if "http" not in sch:
        sch=""
        flag = True
        print "There is no scheme for this url."

    #getting host
    if flag:
         i = len(sch)
    else:
        i = len(sch)+3
    ch =''

    while ch != '/' and i < end:
        ch=url[i]
        hos+=url[i]
        i= i+1

    #removing the first diractory path '/'
    hosend = len(hos)-1
    if hos[hosend] == '/':
        hos= hos[:hosend]

    #getting the rest of the URL
    if flag:
        i = len(sch)+len(hos)
    else:
         i = len(sch)+3+len(hos)
    ch =''
    while i < end:
        ch=url[i]
        pth+=url[i]
        i= i+1

    #removing the first diractory path '/'
    pth = pth[:0]+pth[1:]
    if len(pth) == 0:
        print "There is no Path for this URL."

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
