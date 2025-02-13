import json

def lambda_handler(event, context):
    for record in event['Records']:
        log_entry = json.loads(record['body'])
        message = log_entry.get('message', '')

        if "ERROR_CODE_123" in message:
            print(f"ALERT: Error detected in log entry: {log_entry}")
        else:
            print(f"Processed log entry: {log_entry}")