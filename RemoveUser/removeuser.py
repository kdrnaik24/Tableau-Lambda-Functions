from __future__ import print_function
from tableau_tools import *
from tableau_tools.tableau_rest_api import *

def remove_user(event, context):
    t = TableauRestApiConnection(u"http://ec2-35-163-18-44.us-west-2.compute.amazonaws.com", u"admin", u"password", site_content_url=u"")
    t.signin() 
    print('Signed in')
    urls = t.query_all_site_content_urls()
    t.signout()
    print(urls)

    for url in urls:
        t = TableauRestApiConnection(u"http://ec2-35-163-18-44.us-west-2.compute.amazonaws.com", u"admin", u"password", site_content_url=url)
        t.signin()
        print('Signed in to ' + url)
        unlicensed = []
        users = t.query_users()
        for user in users:
            if user.attrib['siteRole']=='Unlicensed':
                unlicensed.append(user.attrib['id'])
        print(len(unlicensed))

        for u in unlicensed:
            t.remove_users_from_site_by_luid(u)

        t.signout()
        print('Signed out of ' + url)