#!/usr/bin/env python3

import argparse
import boto3

parser = argparse.ArgumentParser(description="Get information of an EC2 instance given its instance_id.")
parser.add_argument("instance_id", help="Insance ID from where retreive the info.")
args = parser.parse_args()

def print_tag(key, tags):
    space = 30 - len(key)
    try:
        tag = tags[key]
    except KeyError:
        tag = '*None*'
    print("%s:%s%s" % (key, ' '*space, tag))

ec2 = boto3.client('ec2', region_name='us-east-1')
instances = ec2.describe_instances(InstanceIds=[args.instance_id])['Reservations'][0]['Instances']
for instance in instances:
    print_tag('InstanceId', instance)
    print_tag('PrivateIpAddress', instance)
    print_tag('PrivateDnsName', instance)
    print_tag('PublicIpAddress', instance)
    print_tag('PublicDnsName', instance)
    print_tag('InstanceType', instance)
    print_tag('AvailabilityZone', instance['Placement'])
    tags = { 'tag_'+tag['Key']: tag['Value'] for tag in instance['Tags'] }
    for key in tags:
        print_tag(key, tags)
