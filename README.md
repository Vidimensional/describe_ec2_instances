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

## Usage
```
$ describe_ec2_instance <instance_id>
InstanceId:          i-12345678901234567
Role:                instance_role
Env:                 instance_environment
PrivateIpAddress:    1.2.3.4
PublicIpAddress:     9.8.7.6
InstanceType:        c3.large
```

## Docker
Maybe you prefer to run it using a container (so you don't have to install Python and/or its libraries).

```
$ docker run -it -e AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>" -e "AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>" vidimensional/describe_ec2_instances ${INSTANCE_ID}
```
May be you want to create an alias in your shell for this 😉.

```
# For Bash.
$ alias lol='docker run -it -e AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY" -e "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID" vidimensional/describe_ec2_instances'
```
