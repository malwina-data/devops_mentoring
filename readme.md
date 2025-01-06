# Project Overview

This project contains an Ansible playbook that creates an AWS Virtual Private Cloud (VPC), subnets, security groups, and launches EC2 instances for a PostgreSQL database and a web application. It also configures the instances, deploys a Flask web application, and sets up Nginx as a reverse proxy.

## Prerequisites

Before you run this playbook, ensure you have the following installed and configured:

1. **Ansible**: Installed on your local machine. You can install it via pip:

    ```bash
    pip install ansible
    ```

2. **AWS CLI**: Installed and configured with your AWS credentials. You can install it via pip:

    ```bash
    pip install awscli
    aws configure
    ```

3. **AWS Access and Secret Keys**: You should have your AWS credentials saved in `../vars/aws_credentials.yaml`.

    The structure of `aws_credentials.yaml` should look like this:

    ```yaml
    aws_access_key: 'your_aws_access_key'
    aws_secret_key: 'your_aws_secret_key'
    region: 'your_aws_region'
    ```

## Ansible Playbook Structure

Ensure your project directory structure is correct:

```bash
.
├── playbook.yaml           # The main playbook file
├── ../vars/                # Directory containing variables and supporting files
│   ├── aws_credentials.yaml
│   ├── key.pem
│   ├── netflix_titles.csv
│   ├── pg_hba.conf
│   ├── templates/
│   │   └── index.html
│   ├── main.py
│   ├── myproject.service
│   └── wsgi.py
├── README.md               # This README file
└── inventory.ini           # Auto-generated during playbook execution

