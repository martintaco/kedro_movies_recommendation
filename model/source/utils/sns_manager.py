import boto3
import json
import time


class SNSManager:
    def __init__(self):
        self.sns_client = boto3.client("sns")

    def publish_message(self, topic_arn, message_json, event_type):
        response = self.sns_client.publish(
            TargetArn=topic_arn,
            Message=json.dumps(message_json),
            Subject="auto-generated subject {}".format(round(time.time() * 1000)),
            MessageStructure='String',
            MessageAttributes={
                "message_type": {
                    "DataType": "String",
                    "StringValue": event_type
                }
            }
        )
        return response['ResponseMetadata']['HTTPStatusCode']