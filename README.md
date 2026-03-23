#  AI Developer Workflow Assistant

**LegalSeva.org | AI Agent Developer Internship Assignment**

An AI-powered CLI tool that automates essential software development tasks such as code explanation, debugging, documentation, and test generation using LLM APIs.

---

## 🔍 Overview

This project is designed to assist developers by reducing manual effort in understanding and improving code.
It takes a Python file as input and performs multiple intelligent operations using AI models.

---

## ⚙️ Features

* 🧠 **Explain Code**
  Generates a clear, beginner-friendly explanation of the code, including structure and logic.

* 🐞 **Debug Code**
  Identifies bugs (syntax, logic, edge cases) and provides fixes with explanations.

* 📝 **Generate Documentation**
  Adds Google-style docstrings and inline comments across the code.

* 🧪 **Generate Test Cases**
  Creates a complete pytest suite with both normal and edge case testing.

* 🔄 **All-in-One Mode**
  Runs all tasks together and optionally saves outputs.

---

## 🏗️ Architecture

```
User Input (CLI)
        ↓
Read Python File
        ↓
Select Task Prompt
        ↓
Send to LLM API (Groq / Gemini)
        ↓
Receive AI Response
        ↓
Display / Save Output
```

---

## 🛠️ Tech Stack

* Python
* Groq API / Google Gemini API
* Rich (for terminal UI formatting)
* argparse (CLI handling)

---

## 📦 Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-dev-workflow-assistant.git
cd ai-dev-workflow-assistant
```

### 2. Install dependencies

```
pip install groq rich
```

or (for Gemini version):

```
pip install google-genai rich
```

---

## 🔑 Setup API Key

Open `dev_assistant.py` and replace:

```
API_KEY = "YOUR_API_KEY"
```

with your actual API key from:

* https://console.groq.com
  or
* https://aistudio.google.com/apikey

---

## ▶️ Usage

Run commands from terminal:

```
python dev_assistant.py --file sample_code.py --task explain
python dev_assistant.py --file sample_code.py --task debug
python dev_assistant.py --file sample_code.py --task document
python dev_assistant.py --file sample_code.py --task test
python dev_assistant.py --file sample_code.py --task all --save
```

---

## 💡 Example

**Input:** Python file with logical errors

**Output:**

* Detected division by zero
* Identified edge case failures
* Generated fixes and improved code structure

---

## 🎯 Key Highlights

* Uses task-specific prompts for structured AI output
* Automates real developer workflows
* Beginner-friendly yet practical implementation
* Clean CLI-based interface

---

## 📌 Future Improvements

* Web-based UI version
* Multi-language code support
* Integration with GitHub repositories
* Real-time code analysis

---

## 👩‍💻 Author

**Anuja Ramesh Gaikwad**
B.Tech Electronics & Computer Engineering

---

This project was developed as part of an AI Agent Developer internship assignment to demonstrate practical use of AI in software development workflows.
