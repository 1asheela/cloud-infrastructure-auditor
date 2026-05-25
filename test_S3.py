import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_s3_buckets():
    try:
        # Create S3 client
        s3 = boto3.client('s3')

        # Get bucket list
        response = s3.list_buckets()

        print("S3 Buckets:")
        for bucket in response['Buckets']:
            print(f" - {bucket['Name']}")

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_s3_buckets()s