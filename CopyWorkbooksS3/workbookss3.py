from __future__ import print_function
from tableau_tools import *
from tableau_tools.tableau_rest_api import *
import boto3

def workbook(event,context):
    ssm = boto3.client('ssm')
    ec2 = boto3.client('ec2')
    lam = boto3.client('lambda')
    instances = ec2.describe_instances(Filters=[
        {'Name':'tag:serverprimary', 'Values':['true']}
    ])
    url = instances['Reservations'][0]['Instances'][0]['PublicDnsName']
    id = instances['Reservations'][0]['Instances'][0]['InstanceId']
    apiconn = 'http://'+url
    t = TableauRestApiConnection(apiconn, u"admin", u"password", site_content_url=u"")
    t.signin() 
    print('Signed in')
    urls = t.query_all_site_content_urls()
    command = ''

    for url in urls:
        if url == '':
            command = 'tabmigrate -command siteExport -fromSiteUserId admin -fromSiteUserPassword password -exportDirectory C:\Users\Administrator\Backup -fromSiteUrl http://localhost/#/projects -fromSiteIsSystemAdmin true -backgroundKeepAlive false -logVerbose true -downloadInfoFiles true -logFile C:\Users\Administrator\AppData\Roaming\TabMigrate\localhost\siteExport2016-11-07-1600-44\siteExport_log.txt -errorFile C:\Users\Administrator\AppData\Roaming\TabMigrate\localhost\siteExport2016-11-07-1600-44\siteExport_errors.txt -exitWhenDone true'
            print(command)
            ssm.send_command(
                InstanceIds = [
                    id
                ],
                DocumentName = 'AWS-RunPowerShellScript',
                Parameters = {
                    'commands':[command]
                }
            )
        else:
            command = 'tabmigrate -command siteExport -fromSiteUserId admin -fromSiteUserPassword password -exportDirectory C:\Users\Administrator\Backup -fromSiteUrl http://localhost/#/site/'+url+'/projects -fromSiteIsSystemAdmin true -backgroundKeepAlive false -logVerbose true -downloadInfoFiles true -logFile C:\Users\Administrator\AppData\Roaming\TabMigrate\localhost\siteExport2016-11-07-1600-44\siteExport_log.txt -errorFile C:\Users\Administrator\AppData\Roaming\TabMigrate\localhost\siteExport2016-11-07-1600-44\siteExport_errors.txt -exitWhenDone true'
            print(command)
            ssm.send_command(
                InstanceIds = [
                    id
                ],
                DocumentName = 'AWS-RunPowerShellScript',
                Parameters = {
                    'commands':[command]
                }
            )
    
    lam.invoke('archivesync')