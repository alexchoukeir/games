import boto3
import json
from config import ConfigSettings

def _get_sqs_client():
    """
    Creates an SQS client. In development, it uses the ElasticMQ endpoint. In production, it uses the AWS SQS service.

    """
    kwargs = {
        'region_name': config.aws_region
    }
    if config.sqs_endpoint:
        kwargs['endpoint_url'] = config.sqs_endpoint
    return boto3.client('sqs', **kwargs)
