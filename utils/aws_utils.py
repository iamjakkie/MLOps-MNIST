import boto3
import os 
import h5py


def get_model(bucket, item):
    s3 = boto3.client('s3')
    s3.download_file(bucket, item, 'mnist_model')
    return 'mnist_model'

def test(bucket):
    s3 = boto3.client('s3')
    return ('Regions: ', s3.list_objects(Bucket=bucket))