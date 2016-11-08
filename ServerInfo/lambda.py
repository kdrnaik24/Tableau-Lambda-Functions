from __future__ import print_function

from datetime import datetime
from urllib2 import urlopen
import tableauserverclient as TSC
import boto3



def lambda_handler(event, context):
    SERVER_URL = "http://ec2-35-163-18-44.us-west-2.compute.amazonaws.com"
    SERVER_USER = 'admin'
    SERVER_PASS = 'password'
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[
        {'Name':'tag:serverprimary', 'Values':['true']}
    ])
    url = instances['Reservations'][0]['Instances'][0]['PublicDnsName']
    id = instances['Reservations'][0]['Instances'][0]['InstanceId']
    print(SERVER_URL)
    SERVER_URL = "http://" + url
    print(SERVER_URL)
    sites = []
    workbooks = []
    all_users = []
    unlicensed_users = []
    unlicensed_usernames = []
    print('Retrieving information from {} as {}'.format(SERVER_URL,SERVER_USER))
    try:
        authz = TSC.TableauAuth(SERVER_USER,SERVER_PASS)
        server = TSC.Server(SERVER_URL)
        server.version = '2.4'
        with server.auth.sign_in(authz):
            info  = server.server_info.get()
            sites, _ = server.sites.get()
        
        for site in sites:
            print('Site information: ',site.name,site.id,site.content_url)
            authz.site_id=site.content_url
            print(authz.site_id)
            with server.auth.sign_in(authz):
                site_details(event,context,server,site,sites,workbooks,all_users,unlicensed_users,unlicensed_usernames)

        serverinfo={ 
            'user_count':len(all_users), 
            'unlicensed_count':len(unlicensed_users),
            'unlicensed':unlicensed_usernames, 
                'tableau_version':info.product_version, 
                'rest_api':info.rest_api_version,
                'workbooks':len(workbooks)
                };
        print(info.product_version)
        print(info.rest_api_version)
    except:
        print('  Server information failed!')
        raise
    else:
        print('  Server information passed!')
        print(serverinfo)
        return(serverinfo)
    finally:
        print('  Server complete at {}'.format(str(datetime.now())))


def site_details(event, context, server, site,sites,workbooks,all_users,unlicensed_users,unlicensed_usernames):
    print('Retrieving site information for {} '.format(server.site_id))
    try:
        
        for wb in TSC.Pager(server.workbooks):
            workbooks.append(wb)

        users, _ = server.users.get()
        #for user in TSC.Pager(server.users): (this needs a fix to the tableauserverclient)
        for user in users:
            all_users.append(user)
            if user.site_role == 'Unlicensed':
                unlicensed_users.append(user)
                unlicensed_usernames.append({'name':user.name,'site':site.name,'site_role':user.site_role})
        print(['{},{}'.format(user.site_role,user.name) for user in users])
        for user in unlicensed_users:
            print(user.name)

    except:
        print('  Site information failed!')
        raise
    else:
        print('  Site information passed!')
    finally:
        print('  Site complete at {}'.format(str(datetime.now())))

#lambda_handler([],[])

