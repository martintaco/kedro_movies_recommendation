import boto3
import pandas as pd
import io
from enum import Enum


class UnitSize(Enum):
    KB = 1
    MB = 2
    GB = 3


def df_read_from_s3(bucket, path):
    """
    Read csv file from s3
    :param bucket: bucket name
    :param path: root file in s3
    :return: Data frame
    """
    s3 = get_credentials()
    obj = s3.get_object(Bucket=bucket, Key=path)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))
    return df


def load_to_s3(bucket, path, file_name):
    """
    Load file to s3 bucket
    :param bucket: bucket name
    :param path: root file in s3
    :param file_name: local file name
    :return:
    """
    s3 = get_credentials()

    with open(file_name, 'rb') as file:
        object = file.read()
        s3.put_object(Bucket=bucket, Key=path, Body=object)
    return


def get_file(bucket, path):
    """
    Get file information from s3 bucket
    :param bucket: bucket name
    :param path: root file in s3
    :return: file object
    """
    s3 = get_credentials()

    obj = s3.get_object(Bucket=bucket, Key=path)
    file_content = io.BytesIO(obj['Body'].read())
    return file_content


def get_folders(bucket, path):
    s3 = get_credentials()
    result = s3.list_objects(Bucket=bucket, Prefix=path, Delimiter='/')
    list_folder = [obj.get('Prefix') for obj in result.get('CommonPrefixes')]
    return list_folder


def get_files(bucket, path, unit_size=UnitSize.MB):
    s3 = get_credentials()
    result = s3.list_objects(Bucket=bucket, Prefix=path, Delimiter='/')
    list_files = [(obj.get('Key'), int(obj.get('Size'))/(1024 ** unit_size._value_ )) for obj in result.get('Contents')]
    return list_files


def get_size(bucket, path, unit_size=UnitSize.MB):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    total_size = 0
    for obj in my_bucket.objects.filter(Prefix=path):
        total_size = total_size + obj.size

    result_size = total_size / (1024 ** unit_size._value_ )
    return result_size


def get_credentials():
    """
    credentials
    :return:
    """
    s3 = boto3.client('s3')
    return s3
