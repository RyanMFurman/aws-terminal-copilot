# aws_terminal_copilot/llm_interface.py

import subprocess

def query_ollama(prompt: str, model: str = "mistral") -> str:
    """
    Sends a natural language prompt to Ollama and extracts the CLI command only.
    """
    full_prompt = f"""
You are a helpful assistant. The user will ask a question about AWS. 
Respond ONLY with a single, executable AWS CLI command on one line. 
Do NOT include explanations, markdown, or extra text. 
Only return something that can be run in the terminal.
User: {prompt}
"""

    result = subprocess.run(
        ["ollama", "run", model],
        input=full_prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()

         