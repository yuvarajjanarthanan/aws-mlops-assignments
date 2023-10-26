Assignment 1:

- Create an EC2 Instance with S3FullAccess Role attached so that it can access the files in S3 buckets
- Upload the Flask App code and templates to the EC2 instance and configure it to run the app(Configured in User Data so that it runs at start).

EC2 Instance Tags:
owner: yuvaraj.janartha@tigeranalytics.com
project: aws-training
name: yuvaraj-ec2-mlops-training

Flask App:
Link: http://http://3.91.242.51:8085/get-files (Will change as Public IP is not dedicated)

Page to specify the folder
![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/0ea64e66-ec5f-4f7d-9c75-26948af36c20)


Page where files are listed
![image](https://github.com/yuvarajjanarthanan/aws-mlops-assignments/assets/94606324/02a8f392-5320-4e0d-99d8-695f6dd2665b)

Unable to configure Security Group to allow incoming traffic only through port 8085 as it is blocked at Organizational Level.
