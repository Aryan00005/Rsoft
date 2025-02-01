# Rsoft

Rsoft is a Django project built with Python 3.12.

## Setup Guide

### Prerequisites

- Python 3.12
- pip (Python package installer)

### Setting Up Virtual Environment

#### On macOS

1. Open your terminal.
2. Navigate to your project directory:
    ```sh
    cd /path/to/your/project
    ```
3. Create a virtual environment:
    ```sh
    python3.12 -m venv venv
    ```
4. Activate the virtual environment:
    ```sh
    source venv/bin/activate
    ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

#### On Windows

1. Open Command Prompt.
2. Navigate to your project directory:
    ```sh
    cd \path\to\your\project
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    ```sh
    venv\Scripts\activate
    ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Project

1. Ensure your virtual environment is activated.
2. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

### Additional Information

For more details on Django, visit the [official documentation](https://docs.djangoproject.com/en/stable/).
