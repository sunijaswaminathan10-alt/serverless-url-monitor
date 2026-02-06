# Serverless URL Uptime Monitor using AWS

## Project Overview

This project is a **serverless website uptime monitoring system** built using **AWS Lambda, Amazon EventBridge, Amazon SNS, and Amazon CloudWatch**.

The system periodically checks the availability of a given website URL.  
If the website is **up (HTTP 200)**, it logs the status in CloudWatch.  
If the website is **down, unreachable, or returns an error status**, it sends an **alert notification** using Amazon SNS (Email/SMS).

This solution is **fully serverless**, so there are **no servers to manage**, making it cost-effective, scalable, and easy to maintain.


## Technologies Used

- **AWS Lambda** – Executes the monitoring code
- **Amazon EventBridge** – Triggers Lambda on a schedule (e.g., every 5 minutes)
- **Amazon SNS** – Sends alert notifications on downtime
- **Amazon CloudWatch Logs** – Stores logs and execution details
- **Python (urllib, boto3)** – Used for HTTP checks and AWS integration
- **Amazon S3 (optional)** – Used to host a test website


## Architecture Flow

# Serverless URL Uptime Monitor using AWS

## Project Overview

This project is a **serverless website uptime monitoring system** built using **AWS Lambda, Amazon EventBridge, Amazon SNS, and Amazon CloudWatch**.

The system periodically checks the availability of a given website URL.  
If the website is **up (HTTP 200)**, it logs the status in CloudWatch.  
If the website is **down, unreachable, or returns an error status**, it sends an **alert notification** using Amazon SNS (Email/SMS).

It is **fully serverless**, so there are **no servers to manage**, making it cost-effective, scalable, and easy to maintain.


## Technologies Used

- **AWS Lambda** – Executes the monitoring code
- **Amazon EventBridge** – Triggers Lambda on a schedule (e.g., every 5 minutes)
- **Amazon SNS** – Sends alert notifications on downtime
- **Amazon CloudWatch Logs** – Stores logs and execution details
- **Python (urllib, boto3)** – Used for HTTP checks and AWS integration
- **Amazon S3 (optional)** – Used to host a test website


## Architecture Flow

EventBridge (Schedule: every 5 minutes)
|
v
AWS Lambda
|
v
Check Website URL
|
| |
Status 200 Error / Not Reachable
| |
v v
Log "UP" Send SNS Alert
| |
v v
CloudWatch Logs CloudWatch Logs


## Features

-  Fully serverless architecture
-  Automated scheduled health checks
-  Real-time alerts using Amazon SNS
-  Logs stored in CloudWatch for monitoring and debugging
-  Configurable URL using Environment Variables
-  Low cost and scalable solution


## Configuration

 ## 1. Create an SNS Topic
- Create an SNS topic and subscribe your email/SMS.
- Confirm the subscription.

### 2. Create a Lambda Function
- Runtime: Python
- Add the monitoring code (`lambda_function.py`).

### 3. Set Environment Variables in Lambda

Added the following environment variables:

- `MONITOR_URL` → The website URL to monitor  
- `SNS_TOPIC_ARN` → The ARN of your SNS topic

### 4. Create an EventBridge Rule
- Create a schedule rule (e.g., `rate(5 minutes)`).
- Set the target as your Lambda function.


## How It Works

1. EventBridge triggers the Lambda function on a fixed schedule.
2. Lambda reads the URL from environment variables.
3. Lambda sends an HTTP request to the website.
4. If the response status is **200 (OK)**:
   - Logs "Website is UP" in CloudWatch.
5. If the response is **not 200** or the site is unreachable:
   - Sends an alert using Amazon SNS.
   - Logs the error in CloudWatch.


## Project Structure
serverless-url-monitor/
│
├── lambda_function.py
├── README.md
└── screenshots/
    ├── lambda-logs.png
    |---lambda-logs-1.png
    |---lambda-config.png
    └── sns-alert.png

  
## 📷 Screenshots

### ✅ Lambda Configuration
![Lambda Config](screenshots/lambda-config.png)

### ✅ Lambda Execution Logs (CloudWatch)
![Lambda Logs](screenshots/lambda-logs.png)
![Lambda Logs 2](screenshots/lambda-logs-1.png)

### 🚨 SNS Alert Email Notification
![SNS Alert](screenshots/sns-alert-email.png)


## Learning Outcomes

- Hands-on experience with AWS Lambda and EventBridge
- Understanding of serverless architecture
- Working with CloudWatch Logs for monitoring
- Using Amazon SNS for alerting and notifications
- Building a real-world uptime monitoring system


## Future Improvements

- Monitor multiple URLs
- Track response time (latency)
- Alert only after multiple consecutive failures
- Store history in DynamoDB
- Create a CloudWatch Dashboard for visualization


## Conclusion

This project demonstrates a **practical serverless monitoring solution** using AWS services.  
It is suitable for monitoring websites, APIs, and cloud applications with minimal cost and operational overhead.



