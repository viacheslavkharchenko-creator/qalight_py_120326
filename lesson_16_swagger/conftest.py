import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def valid_user():
    username = os.getenv("FL_USERNAME")
    password = os.getenv("PASSWORD")
    return username, password

