# aws_terminal_copilot/__intit__.py

import os #Allows access to enviorment variables seurely

# Get AWS access key from enviorment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

# Get AWS Secret Key from enviorment variables
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Get AWS Region or default to us-east-1 if not set
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
                    