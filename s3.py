import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_s3_buckets():
    try:
        # Create S3 client
        s3 = boto3.client('s3')

        # Get bucket list
        response = s3.list_buckets()

        buckets = []
        for bucket in response['Buckets']:
            buckets.append(bucket['Name'])

        return buckets

    except NoCredentialsError:
        return "Error: AWS credentials not found."
    except PartialCredentialsError:
        return "Error: Incomplete AWS credentials."
    except Exception as e:
        return f"Error: {e}"


# Run manually
if __name__ == "__main__":
    result = list_s3_buckets()
    
    if isinstance(result, list):
        print("S3 Buckets:")
        for name in result:
            print(f" - {name}")
    else:
        print(result)