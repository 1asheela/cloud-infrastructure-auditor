from moto import mock_aws
import boto3

@mock_aws
def test_ec2_instances():
    ec2 = boto3.client("ec2", region_name="us-east-1")

    # Create fake EC2 instance
    ec2.run_instances(
        ImageId="ami-12345678",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )

    # Get instances
    response = ec2.describe_instances()

    # Check if instance exists
    reservations = response["Reservations"]
    assert len(reservations) > 0