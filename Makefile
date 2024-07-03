# Makefile

VENV_NAME = .venv

create_venv:
    python -m venv $(VENV_NAME)

activate_venv:
    source $(VENV_NAME)/bin/activate

install_requirements:
    pip install -r requirements.txt

runserver:
    python src/manage.py runserver 0.0.0.0:8000

# migrate:
#     python src/manage.py migrate

setup: create_venv activate_venv install_requirements
