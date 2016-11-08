from __future__ import print_function
import boto3

def cleanup_function(event,context):
    ssm = boto3.client('ssm')
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[
        {'Name':'tag:serverprimary', 'Values':['true']}
    ])
    url = instances['Reservations'][0]['Instances'][0]['PublicDnsName']
    id = instances['Reservations'][0]['Instances'][0]['InstanceId']

    ssm.send_command(
        InstanceIds = [
            id
        ],
        DocumentName = 'AWS-RunPowerShellScript',
        Parameters = {
            'commands':[
                'tabadmin stop"&&"tabadmin cleanup"&&"tabadmin start'
            ]
        }
    )
