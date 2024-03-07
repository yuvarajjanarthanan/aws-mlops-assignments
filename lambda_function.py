import boto3
import datetime

asg_client = boto3.client('autoscaling')

def lambda_handler(event, context):
    try:
        if datetime.now().isoweekday()==6:
            asg_client.set_desired_capacity(
                                            AutoScalingGroupName='yuvaraj-db-webserver-asg',
                                            DesiredCapacity=0,
                                            )
        else:
            asg_client.set_desired_capacity(
                                            AutoScalingGroupName='yuvaraj-db-webserver-asg',
                                            DesiredCapacity=1,
                                            )

    except Exception as err:
        print(err)