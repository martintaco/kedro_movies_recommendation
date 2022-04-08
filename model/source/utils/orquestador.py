import boto3
import time
from utils.configvariables import env_orchestrator_arn
import json


class OrquestadorIntegration:

    def __init__(self):
        self.sns_client = boto3.client("sns", region_name="us-east-1")

    def topic_publish_message(self, topic_arn, message_json, event_type):
        response = self.sns_client.publish(
            TargetArn=topic_arn,
            Message=json.dumps(message_json),
            Subject="auto-generated subject {}".format(
                round(time.time() * 1000)),
            MessageStructure='String',
            MessageAttributes={
                "message_type": {
                    "DataType": "String",
                    "StringValue": event_type
                }
            }
        )
        return response['ResponseMetadata']['HTTPStatusCode']

    def publish_update_msg_orquestador(self, ref_uuid, process_status, failure_reason="NONE"):
        pub_response = None

        if len(ref_uuid.split('-')) > 2:
            json_msg = {
                "uuid": ref_uuid,
                "timestamp": int(time.time() * 1000),
                "stage": "ETL",
                "status": process_status,
                "failure_reason": failure_reason
            }

            pub_response = self.topic_publish_message(
                env_orchestrator_arn, json_msg, 'updates')

        return pub_response