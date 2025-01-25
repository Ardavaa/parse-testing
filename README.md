## Installation

### Prerequisites

- Python >= 3.9
- pip

### Steps

1. **Install `virtualenv`** (if not already installed):
   ```bash
   pip install virtualenv
2. **Create** a new virtual enviroment called `env`
    ```bash
    py -m venv env
    ```
    or
    ```
    python -m venv env
    ```
3. **Activate** the vitual environments
    ```bash
    source env/Scripts/active
    ```
    
    or
    ```bash
    source/bin/activate
    ```
    
    depending on your env folder
4. **Install** dependencies
    Once the virtual environment is activated, install the required dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
5. Obtain API Key
You need to get an API key from [LlamaIndex Cloud](https://cloud.llamaindex.ai/). Sign up and obtain your key to use the services.

6. **Run** the application
    After installing dependencies, you can start the application by running:
    ```bash
    python app.py
    ```
