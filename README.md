# Recipe Book API

Django-based RESTful API for managing recipes.

## Prerequisites

- Python 3.6+
- Virtualenv

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Alex-Rabaev/Recipe-book-api.git
    cd Recipe-book-api
    ```

2. **Create and activate a virtual environment**:
    ```bash
    # On Windows
    python -m venv my_venv
    .\my_venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv my_venv
    source my_venv/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    cd recipe-book
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running Tests

To run the tests, use the following command:
    ```bash
    python manage.py test
    ```

## Running the Application

To start the Django development server, run:
    ```bash
    python manage.py runserver
    ```
The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- **Create a Recipe: POST /api/recipes**
- **Get All Recipes: GET /api/recipes**
- **Get a Single Recipe: GET /api/recipes/{id}**
- **Update a Recipe: PUT /api/recipes/{id}**
- **Delete a Recipe: DELETE /api/recipes/{id}**
- **Search Recipes: GET /api/recipes/search?q={query}**
