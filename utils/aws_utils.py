"""Helper script to interact with AWS
"""
import boto3
import os 
import h5py
import psycopg2
import sys

ENDPOINT="postgresmydb.123456789012.us-east-1.rds.amazonaws.com"
PORT="5432"
USER="app_user"
REGION="eu-west-2"
DBNAME="MLOps"

def get_model(bucket: str, item: str) -> str:
    """Gets the most up-to-date version of model for predictions and saves it locally

    Args:
        bucket (str): name of the aws bucket
        item (str): name of the model

    Returns:
        (str): name of the local file
    """
    s3 = boto3.client('s3')
    s3.download_file(bucket, item, 'mnist_model')
    return 'mnist_model'

def connect_to_rds():
    """Starting point for RDS interaction

    Returns:
        psycopg2 connection: active connection to given RDS instance
    """
    session = boto3.Session()
    client = boto3.client('rds')
    token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)
    return psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=token)

def get_password_hashed(login:str) -> str:
    """Gets hashed password for user

    Args:
        login (str): login for user

    Returns:
        (str): hashed password
    """
    conn = connect_to_rds() 
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT password 
                    FROM mnist.users 
                    WHERE login = %s""", (login))
        return cur.fetchone()[0]

def get_user_history(login:str) -> list:
    """Gets historical predictions for user

    Args:
        login (str): login for user

    Returns:
        (list): list of image paths and predicted values
    """
    conn = connect_to_rds()
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT p.imagePath, p.predictedValue 
                    FROM mnist.predictions p
                    JOIN mnist.users u
                    ON(p.userID = u.userID)
                    WHERE u.login = %s 
                    ORDER BY p.createdDate DESC""", (login))
        return cur.fetchall()

def get_image(path:str):
    """Get image for s3 path

    Args:
        path (str): path to the s3 file
    """

def test(bucket):
    s3 = boto3.client('s3')
    return ('Regions: ', s3.list_objects(Bucket=bucket))

def test_db():
    """[summary]
    """
    session = boto3.Session()
    client = boto3.client('rds')
    