# AWS Terminal Copilot with Mstral LLM

This project is a command-line interface (CLI) tool built using Python and AWS services, designed to interact with AWS resources in a terminal environment. The tool integrates **Mstral LLM** (Large Language Model) to provide intelligent suggestions and help automate common tasks in AWS.

The main objective of this project is to allow users to interact with AWS services via simple commands, without needing to manually run complex AWS CLI commands. It can list EC2 instances, S3 buckets, IAM users, and more. This project can be a powerful tool for AWS developers, system administrators, and anyone looking to quickly interact with AWS resources through an easy-to-use CLI.

---

## Features

- **List EC2 Instances**: View the EC2 instances in your default AWS region.
- **List S3 Buckets**: View all your S3 buckets.
- **List IAM Users**: View the IAM users in your AWS account.
- **Mistral LLM Integration**: Provides command suggestions and smart responses based on the user’s input.

---

## Prerequisites

Before you can use this project, you need to have the following installed:

- **Python** (version 3.6 or higher)
- **AWS CLI**: This is necessary to interact with AWS services. You can install it by following the official guide: [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- **IAM User Credentials**: You will need AWS IAM credentials to interact with AWS services. Follow the instructions below to set this up.

---

## How to Set Up and Use the AWS Terminal Copilot

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/RyanMFurman/aws-terminal-copilot.git
cd aws-terminal-copilot
2. Install Dependencies
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Unix-based systems
venv\Scripts\activate     # For Windows systems
Then, install the necessary Python packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Configure AWS CLI
To interact with AWS services, you need to configure your AWS credentials using IAM (Identity and Access Management).

Steps to Link Your AWS Account:
Sign in to the AWS Management Console:

Go to AWS Console.

Sign in with your AWS account.

Create an IAM User:

In the AWS Console, search for and open IAM.

Click Users and then Add user.

Choose Programmatic access as the access type.

Assign AdministratorAccess (or a custom policy if you prefer more restricted access).

Complete the process and download the Access Key ID and Secret Access Key.

Configure AWS CLI:

Open a terminal window and run the following command:

bash
Copy
Edit
aws configure
Enter the Access Key ID, Secret Access Key, Default region name, and Default output format (usually json).

Example:

bash
Copy
Edit
AWS Access Key ID [None]: YOUR_ACCESS_KEY_ID
AWS Secret Access Key [None]: YOUR_SECRET_ACCESS_KEY
Default region name [None]: us-west-2
Default output format [None]: json
Test the Setup:
After running aws configure, test your AWS CLI setup with the following command:

bash
Copy
Edit
aws sts get-caller-identity
If this returns your IAM user information, your AWS credentials are set up correctly.

Using the Tool
Once the environment is set up, you can interact with the AWS resources using the following commands.

List EC2 Instances
To list all EC2 instances in your default region:

bash
Copy
Edit
python -m aws_terminal_copilot.main copilot
When prompted, you can type: List all EC2 instances in my default region.

List S3 Buckets
To list all S3 buckets:

bash
Copy
Edit
python -m aws_terminal_copilot.main copilot
When prompted, type: List all S3 buckets.

List IAM Users
To list all IAM users:

bash
Copy
Edit
python -m aws_terminal_copilot.main copilot
When prompted, type: List IAM users.

Troubleshooting
If you encounter issues with the AWS CLI not being recognized, make sure you've installed the AWS CLI and configured it properly with your IAM credentials.

If you experience any issues running the commands or if the script doesn’t execute as expected, make sure your environment is set up correctly and dependencies are installed.

Contributing
Feel free to fork this repository and submit pull requests if you'd like to contribute. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Ryan Furman
