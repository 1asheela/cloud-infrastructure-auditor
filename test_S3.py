from moto import mock_aws
import boto3
from s3 import list_s3_buckets

@mock_aws
def test_list_s3_buckets():
    s3 = boto3.client("s3", region_name="us-east-1")
    
    s3.create_bucket(Bucket="test-bucket-1")
    s3.create_bucket(Bucket="test-bucket-2")

    result = list_s3_buckets()

    assert "test-bucket-1" in result
    assert "test-bucket-2" in result