from apps import create_app
from apps.config import DebugConfig

import pytest


@pytest.fixture(scope="session")
def test_client():
    flask_app = create_app(DebugConfig)
    flask_app.config.update(
        {
            "TESTING": True,
        }
    )

    return flask_app.test_client()
