# Basic Dice Rolling App & Pytest Suite

A Python test automation project demonstrating pytest best practices. Utilizes fixtures, parametrize, mocking, markers, and CI/CD integration.

## Project Structure
dice_project/
 - src/
     - dice.py        # Dice rolling application
 - tests/
     - conftest.py     # Initialization & fixtures
     - test_dice.py    # Test suite
 - pytest.ini          # pytest configuration
 - requirements.txt    # Dependencies

## Running Tests

Install dependencies:
pip install -r requirements.txt

Run all tests:
pytest

Run by marker:
pytest -m smoke
pytest -m boundary

## CI/CD
Tests run automatically on every push via GitHub Actions.
