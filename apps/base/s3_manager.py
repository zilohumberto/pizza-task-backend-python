import boto3
from django.conf import settings

session = boto3.Session(
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)

s3 = session.resource('s3', endpoint_url=settings.AWS_S3_ENDPOINT_URL)

s3_client = boto3.client(
    's3', endpoint_url=settings.AWS_S3_ENDPOINT_URL,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)


def upload_file(bucket_name, file_path, key_name):
    data = open(file_path, 'rb')
    return s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
