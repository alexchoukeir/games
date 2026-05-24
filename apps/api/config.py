import boto3
import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

def get_parameters(parameter_name: str) -> str:
    """
    Fetches a parameter value from AWS Systems Manager Parameter Store.

    Args:
        parameter_name (str): The name of the parameter to retrieve.

    Returns:
        str: The value of the parameter.
    """
    ssm = boto3.client('ssm')
    response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    return response['Parameter']['Value']

class ConfigSettings:
    def __init__(self):
        self.db_host = get_parameters('/games/host')
        self.db_password = get_parameters('/games/db-password')
        self.db_name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.llm_key = get_parameters('/games/llm-key')
        self.sync_key = get_parameters('/games/sync-key')
        self.aws_region = os.getenv('AWS_REGION')
        self.sqs_queue = os.getenv('SQS_QUEUE')
        self.s3_bucket = os.getenv('S3_BUCKET')

    @property
    def database_url(self) -> str:
        """
        Creates the postgres database URL from the config settings.

        Returns:
            str: The database URL.
        """
        return f"postgresql://{self.user}:{self.db_password}@{self.db_host}/{self.db_name}"

@lru_cache()
def get_config_settings() -> ConfigSettings:
    """
    Retrieves the config settings.

    Returns:
        ConfigSettings: ConfigSettings object containing all config values.
    """
    return ConfigSettings()

config_settings = get_config_settings()
