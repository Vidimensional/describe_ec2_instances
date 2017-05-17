#!/usr/bin/env python3

import argparse
import re
import boto3

parser = argparse.ArgumentParser(description="Get information of an EC2 instance given its instance id or hostname.")
parser.add_argument("identificator", help="Instance id or hostname from where retreive the info.")
args = parser.parse_args()

def print_tag(key, tags, tag_name=None):
    if not tag_name:
        tag_name = key
    space = 30 - len(tag_name)
    try:
        tag = tags[key]
    except KeyError:
        tag = '*None*'
    print("%s:%s%s" % (tag_name, ' '*space, tag))

ec2 = boto3.client('ec2', region_name='us-east-1')

old_instance_id_regexp = '^i-[0-9]{8}'
new_instance_id_regexp = '^i-[a-z0-9]{17}'
if re.match(old_instance_id_regexp, args.identificator) or re.match(new_instance_id_regexp, args.identificator):
    instances = ec2.describe_instances(InstanceIds=[args.identificator])['Reservations'][0]['Instances']
else:
    instances = ec2.describe_instances(Filters=[{'Name':'private-dns-name', 'Values':[args.identificator+'.ec2.internal']}])['Reservations'][0]['Instances']

for instance in instances:
    print_tag('InstanceId', instance)
    print_tag('Name', instance['State'], tag_name='State')
    print_tag('PrivateIpAddress', instance)
    print_tag('PrivateDnsName', instance)
    print_tag('PublicIpAddress', instance)
    print_tag('PublicDnsName', instance)
    print_tag('InstanceType', instance)
    print_tag('AvailabilityZone', instance['Placement'])
    tags = { 'tag_'+tag['Key']: tag['Value'] for tag in instance['Tags'] }
    for key in tags:
        print_tag(key, tags)
