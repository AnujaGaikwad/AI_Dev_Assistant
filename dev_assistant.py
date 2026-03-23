"""
Assignment 2 - AI-Powered Developer Workflow Assistant
=======================================================
Uses Groq API (free, fast, no quota issues)

Requirements:
    pip install groq rich

Usage:
    python dev_assistant.py --file sample_code.py --task explain
    python dev_assistant.py --file sample_code.py --task debug
    python dev_assistant.py --file sample_code.py --task document
    python dev_assistant.py --file sample_code.py --task test
    python dev_assistant.py --file sample_code.py --task all --save
"""

import os
import sys
import argparse
from groq import Groq
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

# ── Setup ─────────────────────────────────────────────────────────────────────
console = Console()

# ✅ PASTE YOUR GROQ API KEY HERE (get a free key at https://console.groq.com)
API_KEY = "PASTE_YOUR_API_KEY_HERE"
client  = Groq(api_key=API_KEY)

# ── Prompts ───────────────────────────────────────────────────────────────────
PROMPTS = {
    "explain": """You are a senior software engineer.
Analyze the following Python code and provide:
1. A clear, plain-English summary of what the code does
2. A breakdown of each function/class and its purpose
3. The overall architecture or design pattern used
4. Any notable libraries or techniques used
Be beginner-friendly but technically accurate.
""",

    "debug": """You are an expert Python debugger.
Analyze the following code and:
1. List ALL bugs you find (syntax, logic, runtime, edge cases)
2. For each bug, explain WHY it is a bug
3. Provide the FIXED version of each problematic section
4. Rate overall code quality (1-10) with justification

Format each bug as:
  Bug #N: [title]
  Problem: ...
  Fix: ...
""",

    "document": """You are a technical documentation expert.
Add comprehensive docstrings to the following Python code:
1. Module-level docstring explaining the file's purpose
2. Class docstrings with Attributes section
3. Function/method docstrings with Args, Returns, Raises, Example
4. Inline comments for non-obvious logic
Return the COMPLETE file with all docstrings added. Use Google-style docstrings.
""",

    "test": """You are a test engineering expert.
Write a complete pytest test suite for the following Python code:
1. One test per function/method
2. Include happy-path AND edge case tests
3. Test exceptions using pytest.raises
4. Use descriptive names: test_function_when_condition_should_result
Return ONLY the test file content ready to run with: pytest test_sample.py
"""
}

# ── Core Agent ────────────────────────────────────────────────────────────────
def run_task(code: str, task: str, filename: str) -> str:
    """Send code + task prompt to Groq and return the response."""
    full_prompt = PROMPTS[task] + f"\n\nFile: {filename}\n\n```python\n{code}\n```"

    with Progress(
        SpinnerColumn(),
        TextColumn(f"[cyan]Running task: [bold]{task}[/bold]..."),
        transient=True
    ) as progress:
        progress.add_task("", total=None)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPTS[task]},
                {"role": "user",   "content": f"File: {filename}\n\n```python\n{code}\n```"}
            ],
            temperature=0.2,
            max_tokens=2048
        )

    return response.choices[0].message.content


def save_output(result: str, task: str, filename: str):
    """Save task output to a file."""
    base = os.path.splitext(filename)[0]
    out_map = {
        "explain":  f"{base}_explained.md",
        "debug":    f"{base}_debugged.md",
        "document": f"{base}_documented.py",
        "test":     f"test_{base}.py",
    }
    out_file = out_map.get(task, f"{base}_{task}_output.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(result)
    console.print(f"\n[green]Saved to:[/green] [bold]{out_file}[/bold]")
    return out_file


# ── CLI ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="AI Dev Assistant - Powered by Groq + LLaMA 3.3 70B"
    )
    parser.add_argument("--file", "-f", required=True, help="Path to Python file")
    parser.add_argument("--task", "-t", required=True,
                        choices=["explain", "debug", "document", "test", "all"])
    parser.add_argument("--save", "-s", action="store_true",
                        help="Save output to file")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        console.print(f"[red]File not found:[/red] {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        code = f.read()

    if not code.strip():
        console.print("[red]File is empty.[/red]")
        sys.exit(1)

    filename = os.path.basename(args.file)
    console.print(Panel(
        f"[bold cyan]AI Dev Assistant[/bold cyan]\n"
        f"File : [yellow]{filename}[/yellow]\n"
        f"Task : [green]{args.task}[/green]\n"
        f"Model: [magenta]LLaMA 3.3 70B via Groq[/magenta]",
        border_style="cyan"
    ))

    tasks = ["explain", "debug", "document", "test"] if args.task == "all" else [args.task]

    for task in tasks:
        if args.task == "all":
            console.rule(f"[bold magenta]{task.upper()}")
        result = run_task(code, task, filename)
        console.print(Markdown(result))
        if args.save:
            save_output(result, task, filename)


if __name__ == "__main__":
    main()
