# Q and A Generation Using Llama Index

## Table of Contents
1. [Directory Structure](#directory-structure)
2. [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
3. [Install Necessary Packages](#install-necessary-packages)
4. [Start Ollama](#start-ollama)
5. [Define Settings and Load Documents](#define-settings-and-load-documents)
6. [Create Input File](#create-input-file)
7. [Write the Python Code](#write-the-python-code)
8. [Run the Script](#run-the-script)
9. [Verify Output](#verify-output)
10. [Sample Input and Output](#sample-input-and-output)

## Directory Structure

```
my_project/
│
├── pdfdirectory/
│   └── sample.pdf
├── input.json
├── output.json
├── venv/
│   └── ...
├── main.py
└── README.md
```

## Create and Activate Virtual Environment

1. **Create `my_project` directory and open it in a code editor. Open a terminal.**

2. **Navigate to your project directory:**
    ```sh
    cd my_project
    ```

3. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**
    ```sh
    source venv/bin/activate
    ```

## Install Necessary Packages

1. **Open a terminal within your project directory.**

2. **Install the required packages:**
    ```sh
    pip install llama-index langchain transformers huggingface_hub trafilatura
    pip install llama-index-llms-ollama llama-index-embeddings-huggingface
    pip install --upgrade llama-index langchain transformers huggingface_hub llama-index-llms-ollama llama-index-embeddings-huggingface
    ```

## Start Ollama

1. **Open another terminal tab within the same virtual environment.**

2. **Run:**
    ```sh
    ollama start
    ```

3. **If you encounter a port error, run:**
    ```sh
    killall ollama
    ```

4. **Then run again:**
    ```sh
    ollama start
    ```

5. **Open another terminal tab and run:**
    ```sh
    ollama run llama3
    ```

## Define Settings and Load Documents

## Create Input File

1. **Create a file named `input.json` in your project directory.**

2. **Add sample data to `input.json`:**
    ```json
    {
        "pdf_path": "path/to/your/pdf/directory",
        "query": "query_here"
    }
    ```

## Run the Script

1. **Ensure your virtual environment is activated.**

2. **Run the Python script:**
    ```sh
    python3 main.py
    ```

## Verify Output

1. **Check for the output file `output.json` in your project directory.**

2. **The file should contain the result of the query or any errors encountered.**

## Sample Input and Output

### `input.json`
```json
{
    "pdf_path": "path/to/your/pdf/directory",
    "query": "Who is motmot?"
}
```

### `output.json`
```json
{
    "question": "Who is motmot?",
    "answer": "The response from the LLM will be here."
}
```

### Example `output.json` Generated
```json
{
    "question": "Who is motmot?",
    "answer": "Motmot is a monkey who loves eating bananas!"
}
```

**Note:** This was tested on Python version 3.12.4

**PDF file used is `motmot.pdf` above.**
