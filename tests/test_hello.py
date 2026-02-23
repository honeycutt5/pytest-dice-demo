import pytest
from unittest.mock import patch
from hello import roll, msg

# --- Smoke Tests ---
@pytest.mark.smoke
def test_msg_content():
    """This message string should match expected value."""
    assert msg == "Roll the Dice!"

@pytest.mark.smoke
def test_roll_returns_integer(roll_result):
    """roll() should return an integer."""
    assert isinstance(roll_result, int)
    
# --- Boundary Tests ---
@pytest.mark.boundary
def test_roll_within_valid_range(roll_result):
    # roll() should return an integer between 1 and 6 inclusive.
    assert 1 <= roll_result <= 6
    
@pytest.mark.boundary
@pytest.mark.parametrize("mocked_value", [1, 2, 3, 4, 5, 6])
def test_roll_returns_each_face(mocked_value):
    # Verifies that roll() returns each value between 1 and 6 inclusive.
    with patch("hello.np.random.randint", return_value=mocked_value):
        assert roll() == mocked_value
        
# --- Exception/Edge Case Tests ---

@pytest.mark.parametrize("mocked_value", [0, 7])
def test_roll_returns_out_of_bounds_mock(mocked_value):
    # Mocks response value to out of bounds values (0 and 7) for the sake of identifying a gap
    with patch("hello.np.random.randint", return_value=mocked_value):
        result = roll()
        assert 1 > result > 6  # mocked values pass through, exposing need for validation

def test_roll_returns_consistent_type():
    # Checks to ensure numpy is returning strictly int values
    for _ in range(10):
        result = roll()
        assert type(result) is int, f"Expected int, got {type(result).__name__}"

        
