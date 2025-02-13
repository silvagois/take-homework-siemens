from aws_cdk import (
    core,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as event_sources,
)

class LogAnalysisStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # SQS Queue
        queue = sqs.Queue(self, "LogQueue")

        # Lambda Function
        log_processor = _lambda.Function(self, "LogProcessor",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="main.lambda_handler",
            code=_lambda.Code.from_asset("../src")
        )

        # Trigger Lambda with SQS
        log_processor.add_event_source(event_sources.SqsEventSource(queue))

        # Output the Queue URL
        core.CfnOutput(self, "QueueURL", value=queue.queue_url)