# File: aws_terminal_copilot/main.py
# --------------------------------------------------
# Main CLI entry point for the AWS Terminal Copilot.
# Includes both: 
#   - a traditional command to show AWS config,
#   - and an interactive assistant powered by an LLM (like Mistral via Ollama).
# Uses Typer for CLI structure and Rich for styled terminal output.


import subprocess # Used to execute AWS CLI commands from Python
import typer  # Typer helps build simple CLI commands like 'aws config-show'
from rich.console import Console  # Rich helps to print styled terminal output
from rich.panel import Panel  # Panel adds boxes/panels around our output
from aws_terminal_copilot import config  # Import the AWS config that we defined
from aws_terminal_copilot.llm_interface import query_ollama # Sends user input to Ollama and gets back a CLI command

# Create a Typer app instance
app = typer.Typer()

# Create a Rich console for styled printing
console = Console()

# Define a CLI command: 'python -m aws_terminal_copilot.main config-show'
@app.command(name="config-show")
def config_show():
    """Display AWS Credentials pulled from environment variables"""

    # Use triple quotes to define a block of styled text using Rich markup
    aws_info = f"""
[bold orange]AWS Configuration[/bold orange]

[bold]Access Key:[/bold] {config.AWS_ACCESS_KEY_ID or "Not Set"}
[bold]Secret Key:[/bold] {'*' * len(config.AWS_SECRET_ACCESS_KEY) if config.AWS_SECRET_ACCESS_KEY else "Not set"}
[bold]Region:[/bold] {config.AWS_REGION or "Not Set"}
"""
    
    # Print that text inside a panel with a title
    console.print(Panel(aws_info.strip(), title="AWS Terminal Copilot", expand=False))

@app.command()
def copilot():
    """
    Start the LLM assistant loop.
    This assistan takes the natural language input and suggests AWS CLI commands.
    """
    console.print("[bold orange]AWS Terminal Copilot With Mistral LLM")
    
    # This allows continous loop until the user types 'exit'
    while True:
        # Ask user for a natural language query
        prompt = input("\n What do you want to do in AWS? (or 'exit')").strip()

        # Exit the loop if user wants to quit
        if prompt.lower() in ("exit", "quit"):
            break

        # Use the LLM to generate an AWS CLI command from the prompt
        cli_command = query_ollama(prompt)

        # Show the suggested command in a rich panel
        console.print(Panel(f"[bold orange]Suggested command:[bold orange] {cli_command}", title="LLM Output"))

        # Ask the user if they want to run the generated command
        if typer.confirm("Run this command?, default=False"):
            # If yes, execute it with the subprocess and capture the output
            result = subprocess.run(cli_command, shell=True, capture_output=True, text=True)

            # Display command output
            console.print(f"[bold green]Output:[/bold green]\n{result.stdout}")

            # If there's an error, show it
            if result.stderr:
                console.print(f"[bold red]Error:[/bold red]\n{result.stderr}")

        else:
            # Skip execution if the user declines
            console.print(f"[bold grey]Skipping execution...[/bold grey]")

if __name__ == "__main__":
    app() 
