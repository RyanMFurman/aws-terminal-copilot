#AWS Terminal Copilot Project

A CLI tool that interacts with AWS services using an LLM (Mistral) to generate AWS CLI commands from natural language queries.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RyanMFurman/aws-terminal-copilot.git
   ```

2. Install dependencies in a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m aws_terminal_copilot.main copilot
   ```

## Usage

You can ask questions like "List all EC2 instances" and the program will suggest and execute the corresponding AWS CLI commands.
