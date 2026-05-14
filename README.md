 Cloud Infrastructure Auditor & Cost Optimizer

 ##Project Description
This project helps scan cloud resources and optimize AWS costs.

 ##Team Members
- Member 1 – Authentication & CLI
- Member 2 – Scanner Module
- Member 3 – Optimization & Reports
- Member 4 – Testing & Documentation

##Technologies Used
- Python
- AWS Boto3
- Typer CLI

 ##Project Goal

To identify unused AWS resources and suggest cost-saving recommendations.

## installation

pip install-r requirement.txt

## Run the project

pyton main.py
# Features

- Scan AWS EC2 resources
- Generate JSON reports
- Command Line Interface (CLI) support
- Modular project structure
- Basic testing support
- Easy setup and execution

# Project Structure

project/
│
├── scanner/
│   └── ec2_scanner.py
│
├── reports/
│   └── json_report.py
│
├── tests/
│   ├── test_scanner.py
│   ├── test_reports.py
│   └── test_cli.py
│
├── utils/
│   └── logger.py
│
├── README.md
├── requirements.txt
└── main.py

# Example Output

Scanning AWS EC2 resources...

[
    {
        "InstanceId": "i-123456",
        "State": "running"
    }
]

JSON report generated successfully.

