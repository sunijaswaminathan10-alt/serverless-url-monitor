import os
import urllib.request
import boto3

def lambda_handler(event, context):
    print("Lambda function started - URL Monitor")
    url = os.getenv('MONITOR_URL')
    sns_topic_arn = os.getenv('SNS_TOPIC_ARN')

    print("Checking URL:", url)

    try:
        response = urllib.request.urlopen(url, timeout=5)
        status = response.getcode()
        print("Received status code:", status)

        if status == 200:
            print("Website is UP")
            return {"statusCode": 200, "body": "Website is Up"}
        else:
            message = f"Website {url} is DOWN. Status Code: {status}"
            print("Sending alert:", message)
            send_alert(sns_topic_arn, message)
            return {"statusCode": status, "body": "Website is Down"}

    except Exception as e:
        message = f"Website {url} is NOT REACHABLE. Error: {str(e)}"
        print("Exception occurred:", message)
        send_alert(sns_topic_arn, message)
        return {"statusCode": 500, "body": "Website is Not Reachable"}

def send_alert(topic_arn, message):
    if not topic_arn:
        print("SNS_TOPIC_ARN not set")
        return

    sns_client = boto3.client("sns")
    sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="Website Downtime Alert"
    )
