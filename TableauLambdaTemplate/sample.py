# You need these - do not delete them
from __future__ import print_function
from tableau_tools import *
from tableau_tools.tableau_rest_api import *
# If you have other libraries you need, import them here
# from foo import bar

# This is your function
# If you don't want to or can't use AWS, comment the next line and fix the indents for the function (meaning push them all back)
def function_handlier(event, context):
    # Sign in
    t = TableauRestApiConnection(u"http://ec2-35-161-7-194.us-west-2.compute.amazonaws.com", u"user", u"password", site_content_url=u"")
    t.signin() 
    # Do Stuff
    # Sign out