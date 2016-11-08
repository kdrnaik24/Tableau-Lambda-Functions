from __future__ import print_function
import boto3

def backup_func(event,context):
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
                '$object = Get-S3Object -BucketName hackathon-tableaubackup -Key backups | Sort-Object LastModified -Descending | Select-Object -First 1 | select Key `n Read-S3Object -BucketName hackathon-tableaubackup -Key $object.key -File C:\Users\Administrator\Backup\Server\backup.tsbak `n tabadmin restore C:\Users\Administrator\Backup\Server\backup.tsbak'
            ]
        }
    )