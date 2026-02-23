import pytest
from hello import roll

# Provides a single dice roll result to test
@pytest.fixture
def roll_result():
    return roll()