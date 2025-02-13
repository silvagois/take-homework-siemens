import boto3
import json
import random
import time

def generate_log():
    messages = [
        {"message": "Application started successfully."},
        {"message": "ERROR_CODE_123: Critical failure in module X."},
        {"message": "User logged in."},
        {"message": "ERROR_CODE_456: Disk space low."},
        {"message": "Data processed successfully."}
    ]
    return random.choice(messages)

def send_log_to_sqs(queue_url):
    sqs = boto3.client('sqs')
    while True:
        log_entry = generate_log()
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(log_entry)
        )
        print(f"Sent log: {log_entry}")
        time.sleep(5)

if __name__ == "__main__":
    queue_url = "YOUR_SQS_QUEUE_URL"  # Replace with your SQS Queue URL
    send_log_to_sqs(queue_url)