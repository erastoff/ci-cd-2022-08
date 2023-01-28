"""
Test configuration
"""

import pytest
from flask.testing import FlaskClient
from app import app

@pytest.fixture
def client() -> FlaskClient:
    """
    client creation
    :return:
    """
    app.config.update(WTF_CSRF_ENABLED=False)
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
