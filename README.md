Assignment 2:

- Create a VPC(Virtual Private Connection) in two AZs each with one Private and Public Subnet. Assign a Security Group for the VPC.
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/cf1ead4c-80bf-4594-b071-ad3c8e541469)

- Create a MySQL RDS Database with the default configuration. Use the created VPC and SG created.
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/98c18ae9-b5e2-4d9a-9ef9-bac08804e517)

- Create an EC2 Instance with the Web Server Code(app.py) and Templates(index.html). Give Permissions via IAM role to access DB. Check whether the connection to database is established and works.
- Create an AMI(Amazon Machine Image) from the EC2 instance created above. Create a launch template from the AMI with the user data to invoke the app on startup. Use appropriate instance types and Security Groups.
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/a008d3d1-5b7d-4247-bf25-01c1c0c75c47)

- Use the launch template to set up Auto Scaling Group. Set the desired Size as 2 and configure the VPC created above.
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/b682c8d2-2987-41bf-a60e-b0fff7a2ff2d)
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/52dd8bf9-1042-433f-9b70-53362d3ac59a)

- Since the instances created from ASG do not have a public IPv4, we need to create an Internet facing Application Load Balancer to access these instances.
- Create appropriate Target Groups for instances to be used in the Load Balancer
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/a462a981-adfa-4929-8fc3-f068b7feef37)
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/a9aed429-f9da-4485-b91a-272b6f203c68)

- Access the Web Server with the DNS of the Load Balancer.
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/e14a29cd-cdd3-4896-bf88-f28647165b5b)
  ![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/987ef914-54f2-4231-94a2-c5aaf93b9040)

- Create a Lambda to Scale up the ASG to 0 capacity on Saturdays and scale back up to 1 on Mondays. Give permissions via IAM role to access ASG. Set up event in AWS EventBridge to trigger the Lambda.
