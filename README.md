# challengesolution
# Metadatsolution--please follow these steps before executing the metadata scripts
# if we want to access metadata from a running EC2 instance it is possible either using IMDSv1 and IMDSv2
# please launch an AWS Linux 2 AMI ec2 instance.
# while launching ec2 instance in configure instance details page under advanced details we need to choose options such as Metadata accessable - Enabled and Metadata version - v2(token required). and metadata token response hop limit as 1.
# Once your EC2 is up and running then connect to the ec2 instance and open the instance terninal.
# Execute the metadata scripts from the ec2-instance terminal.
