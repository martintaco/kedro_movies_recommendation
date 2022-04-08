import boto3 
import botocore
import json, os

class ECSManager:

    def __init__(self, ecs_cluster, task_definition):
        self.client = boto3.client('ecs')
        self.ecs_cluster = ecs_cluster
        self.task_definition = task_definition

    def ecs_run_task(self, body: dict, topic: str):

        try:
            response = self.client.run_task(
                cluster = self.ecs_cluster,
                launchType = 'FARGATE',
                taskDefinition = self.task_definition,
                count = 1,
                platformVersion = 'LATEST',
                networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': [os.environ['SUBNETS']],
                    'assignPublicIp': 'DISABLED',
                    'securityGroups': [os.environ['SECURITY_GROUPS']],
                    },
                },
                overrides = {
                    'containerOverrides': [
                        {
                            'name': 'CatalogAutomation',
                            'environment': [
                                {
                                    'name': 'TOPIC',
                                    'value': topic
                                },
                                {
                                    'name': 'DATA',
                                    'value': json.dumps(body)
                                },
                                {
                                    'name': 'ENV',
                                    'value': os.environ['APP_ENV']
                                },
                                {
                                    'name': 'FILE_CAMPAIGN_CRON',
                                    'value': os.environ['FILE_CAMPAIGN_CRON']
                                }                          
                            ]
                        }
                    ]
                }
            )

            return response

        except botocore.exceptions.ClientError as e: 
            print(f"Exception ocurred: {str(e)}")
