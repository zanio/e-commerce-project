import environ
from django.core.management.commands import runserver

from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

env_path = Path('./ecom') / '.env'
load_dotenv(dotenv_path=env_path)
env = environ.Env()


class Command(runserver.Command):
    default_port = env("SERVER_PORT")
