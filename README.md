# Cloud Book Writer

This is a cloud book writer platform.

## Requirements

- pre-commit (`pip install pre-commit`)

## Setup

1. Clone the Repo

    ```bash
    git pull origin https://github.com/MuhammadHassan1998/coding_task.git
    cd coding_task
    ```
2. Setup Virtual Environment `python3 -m venv myvenv`

3. Activate the Environment `source venv/bin/activate`

4. Install the project: `pip install -r requirements.txt`

5. Set up pre-commit: `pre-commit install`

6. populate `.env`:

    Add a `.env` file in the repo root.
    important values to run the project

    ```sh
    SECRET_KEY: asdasdasdasd
    ```
7. Run `python manage.py makekigrations`

8. Run `python manage.py migrate`

9. Run `Python manage.py runserver`

    _**Note:**
    Run `pre-commit run --all-files` before committing to run black and isort on all files
