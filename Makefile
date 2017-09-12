installation_path ?= /usr/local/bin

install:
	pip3 install -r requirements.txt
	mkdir -p $(installation_path)
	cp src/describe_ec2_instances.py $(installation_path)/describe_ec2_instances

uninstall:
	rm $(installation_path)/describe_ec2_instances

container:
	docker build -t vidimensional/describe_ec2_instances .
