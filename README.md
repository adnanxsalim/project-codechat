# codechat: Have a chat with any codebase

**codechat** is a command-line AI tool that lets you analyze and interact with any codebase by asking questions about the code. Powered by OpenAI's GPT models, it helps you understand, review, and refactor codebases quickly and efficiently.

## Features

- Load and parse multiple source code files from a directory
- Ask natural language questions about the entire codebase
- Interactive chat mode for continuous Q&A
- Supports many common programming languages and file types
- Lightweight and easy to install via pip

## Project Structure

```bash
.
├── setup.py                # setup file containing installation information for pip
└── codechat                # parent directory containing all source files
    ├── __init__.py         # file to let pip know that this is a package
    ├── cli.py              # main script
    ├── code_loader.py      # script to load files from the specified codebase
    └── llm_client.py       # script for chat model configuration
```

## Installation

Make sure you have Python 3.8 or higher installed.

```bash
pip install git+https://github.com/adnanxsalim/project-codechat.git
```

Alternatively, clone the repo and install with:

```bash
git clone https://github.com/adnanxsalim/project-codechat.git
cd codechat
pip install .
```

## Setup

You need an OpenAI API key to use **codechat**. Set it as an environment variable:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

## Usage

```bash
codechat /path/to/codebase -q "Your question about the codebase"
```

Example:

```bash
codechat ./my_project -q "What does this codebase do?"
```

### Interactive Mode

Run without the `-q` flag to enter an interactive chat mode:

```bash
codechat ./my_project
```

Type your questions and get answers. Type `exit` or `quit` to leave.

## Supported File Types

By default, **codechat** loads files with these extensions:

`.py`, `.js`, `.ts`, `.jsx`, `.tsx`, `.wasp`, `.c`, `.mjs`, `.java`, `.html`, `.css`, `.json`

To add more extensions, go to `codechat/code_loader.py` and add the file extensions you want.

Files larger than 100 KB are skipped to keep responses manageable.

## How it Works

- **Code Loading:** Recursively scans the given directory for supported files, reading their contents.
- **Prompt Construction:** Combines all code files into a single prompt (truncated if too large).
- **AI Analysis:** Sends the prompt and user question to OpenAI's GPT API to generate an answer.
- **CLI Interface:** Provides both single-question and interactive chat modes.

## Development

To contribute or modify:

1. Clone the repo
2. Create a virtual environment and install dependencies
3. Modify the code in the `codechat` package
4. Test using the CLI

## License

MIT License © Adnan Salim

## Contact

For questions or feedback, reach out to Adnan Salim at [hello@adnansal.im](mailto:hello@adnansal.im)
