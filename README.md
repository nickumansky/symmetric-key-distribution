# Symmetric Key Distribution Tool

## Overview
This project implements a tool to assign unique symmetric keys to networks. Given a network plan (a list of sets of names), the tool assigns a unique key to each network while ensuring that each device (person) holds no more than 4 keys. The project includes a FastAPI API for key distribution, unit tests, and a CI pipeline with GitHub Actions.

## Project Structure
- **key_distribution.py**: Core logic for deduplicating networks and assigning keys.
- **main.py**: FastAPI API exposing the key assignment functionality.
- **test_key_distribution.py**: Unit tests using Python's `unittest`.
- **requirements.txt**: Lists project dependencies.
- **.github/workflows/ci.yml**: GitHub Actions configuration for continuous integration.

## Features
- **Key Assignment**: Deduplicates network definitions and assigns keys ensuring no device exceeds 4 keys.
- **Web API**: FastAPI endpoint accepts a JSON network plan and returns key assignments.
- **Automated Testing & CI**: Unit tests with GitHub Actions for linting, type checking, and test execution.

## Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/nickumansky/symmetric-key-distribution.git
2. **Navigate to the Project Directory:**

    ```bash
    cd symmetric-key-distribution
3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
### Running the Application
#### As an API Service

Start the FastAPI server:

    uvicorn main:app --reload
    
**Access the interactive API docs at http://localhost:8000/docs.**

### Running Tests
Run unit tests locally:

    python -m unittest discover

## Continuous Integration
GitHub Actions is configured to automatically run linting (flake8), static type checking (mypy), and unit tests on every push or pull request to the main branch. View the CI status under the Actions tab in the GitHub repository.

## Additional Enhancements
**Automated Testing:** Unit tests to verify key assignment logic.

**API Deployment:** A FastAPI endpoint for key distribution.

**CI Pipeline:** Automated quality checks via GitHub Actions.


## Contact
For questions or further information, please contact:

Email: umanskynicholas@gmail.com