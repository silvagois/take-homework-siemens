Hello everyone, since I was unable to create my AWS account to use the free tier because of a problem with my credit card, I made a model of what the architecture of question 4 would look like, but I cannot guarantee that it is working, but it would be a model of how it would look, the idea would be to create a lambda that would consume data from an SQS topic and process and validate the logs. I know it is a simple model, but I believe it can achieve the expected end result.

```
log-analysis-alert-system/
│
├── infra/
│   ├── app.py
│   ├── log_analysis_stack.py
│
├── src/
│   ├── log_generator.py
│   ├── main.py
│
├── tests/
│   ├── test_logs.json
│
├── README.md
├── requirements.txt
└── cdk.json
```
---

# Log Analysis and Alert System

This project demonstrates a simple log analysis and alert system using AWS services like SQS and Lambda.

## Architecture

1. **Log Generator**: Simulates log entries and sends them to an SQS queue.
2. **main.py**: A Lambda function that processes logs from the SQS queue and triggers alerts if specific error messages are found.

---

## Setup

### 1. Install Dependencies

Before deploying the infrastructure, ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

---

### 2. Deploy Infrastructure

Use AWS CDK to deploy the infrastructure (SQS queue and Lambda function):

```bash
cd infra
cdk deploy
```

After deployment, note the **Queue URL** output by the CDK. You will need it to run the log generator.

---

### 3. Run Log Generator

Simulate log entries and send them to the SQS queue:

```bash
python src/log_generator.py
```

Replace `YOUR_SQS_QUEUE_URL` in the `log_generator.py` script with the actual SQS Queue URL output by the CDK.

---

### 4. Monitor Alerts

Check the CloudWatch Logs for the Lambda function to see alerts being triggered:

1. Go to the **AWS Management Console**.
2. Navigate to **CloudWatch > Log Groups**.
3. Find the log group for the Lambda function (e.g., `/aws/lambda/LogProcessor`).
4. Check the logs for messages like `ALERT: Error detected in log entry`.

---

## Testing

You can use the `tests/test_logs.json` file to simulate different log entries. Modify the `log_generator.py` script to read from this file if needed.

Example of test logs:

```json
[
    {"message": "Application started successfully."},
    {"message": "ERROR_CODE_123: Critical failure in module X."},
    {"message": "User logged in."},
    {"message": "ERROR_CODE_456: Disk space low."},
    {"message": "Data processed successfully."}
]
```

---

## Cleanup

To avoid incurring charges, destroy the stack after testing:

```bash
cd infra
cdk destroy
```

This will delete the SQS queue, Lambda function, and any other resources created by the CDK.

---

## How to Run

### Step-by-Step Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Deploy Infrastructure**:
   ```bash
   cd infra
   cdk deploy
   ```

3. **Run Log Generator**:
   ```bash
   python src/log_generator.py
   ```

4. **Monitor Alerts**:
   - Check the CloudWatch Logs for the Lambda function to see alerts being triggered.

5. **Cleanup**:
   - Destroy the stack after testing to avoid unnecessary charges:
     ```bash
     cd infra
     cdk destroy
     ```

---

## License

This project is licensed under the MIT License.

---

Este `README.md` agora inclui todos os passos necessários para configurar, executar, testar e limpar o projeto de forma clara e organizada.
