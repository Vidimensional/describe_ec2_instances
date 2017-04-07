# describe_ec2_instance
Get information of an EC2 instance given its `instance_id`.

## Installing
```
$ make install
```

## Uninstalling
```
$ make uninstall
```

## Configuration
The only configuration it needs is specify the AWS credentials. You can take a look at [boto3 documentation](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials) in order to configure them.

TL;DR: You can just export the following variables `AWS_SECRET_ACCESS_KEY` & `AWS_ACCESS_KEY_ID`.

## Usage
```
$ describe_ec2_instance <instance_id>
InstanceId:          i-12345678901234567
PrivateIpAddress:    1.2.3.4
PrivateDnsName:      ip-1-2-3-4.ec2.internal
PublicIpAddress:     9.8.7.6
PublicDnsName:       ec2-9-8-7-6.compute-1.amazonaws.com
InstanceType:        c3.large
tag_NameTag1:        valueTag1
tag_nameTagN:        valueTagN
```

## Docker
If you prefer to run it using a container (so you don't have to install Python and/or its libraries).

You can find it on 
```
$ docker run -it -e AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>" -e "AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>" vidimensional/describe_ec2_instances ${INSTANCE_ID}
```
May be you want to create an alias in your shell for this 😉.

```
# For Bash.
$ alias lol='docker run -it -e AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY" -e "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID" vidimensional/describe_ec2_instances'
```
