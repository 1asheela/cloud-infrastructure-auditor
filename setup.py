from setuptools import setup, find_packages

setup(
    name="cloud-infrastructure-auditor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "click",
        "pytest",
        "moto"
    ],
)