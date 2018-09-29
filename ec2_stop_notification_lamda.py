import json
import boto3
sns_client=boto3.client('sns')

def lambda_handler(event, context):
    sns_arn = 'arn:aws:sns:us-west-2:071705998066:ec2_alerts'
    sns_msg = 'Ec2 instance stopped !!!!'
    sns_subject = 'Ec2 stopped alert'
    sns_client.publish(
    TopicArn = sns_arn,
    Message = sns_msg,
    Subject = sns_subject
    )