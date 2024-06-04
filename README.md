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
    cd recipe_book
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running Tests

To run the tests, use the following command:
    `python manage.py test`

## Running the Application

To start the Django development server, run:
    `python manage.py runserver`
The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- **Create a Recipe: POST /api/recipes**
- **Get All Recipes: GET /api/recipes**
- **Get a Single Recipe: GET /api/recipes/{id}**
- **Update a Recipe: PUT /api/recipes/{id}**
- **Delete a Recipe: DELETE /api/recipes/{id}**
- **Search Recipes: GET /api/recipes/search?q={query}**

## Example Request and Response

### Create a Recipe

**Request**:
```json
POST /api/recipes
{
    "title": "Spaghetti Carbonara",
    "description": "A classic Italian pasta dish with a creamy egg sauce.",
    "ingredients": [
        "200g spaghetti",
        "100g pancetta",
        "2 large eggs",
        "50g grated Parmesan cheese",
        "Salt",
        "Black pepper"
    ],
    "instructions": "...",
    "category": "Pasta"
}
```
**Response**:
```json
{
    "id": 1,
    "title": "Spaghetti Carbonara",
    "description": "A classic Italian pasta dish with a creamy egg sauce.",
    "ingredients": [
        "200g spaghetti",
        "100g pancetta",
        "2 large eggs",
        "50g grated Parmesan cheese",
        "Salt",
        "Black pepper"
    ],
    "instructions": "...",
    "category": "Pasta"
}
```

### Update a Recipe

**Request**:
```json
PUT /api/recipes/1
{
    "title": "Updated Spaghetti Carbonara",
    "instructions": "Updated instructions...",
    "category": "Pasta Carbonara"
}
```
**Response**:
```json
{
    "id": 1,
    "title": "Updated Spaghetti Carbonara",
    "description": "An updated description.",
    "ingredients": [
        "250g spaghetti",
        "150g pancetta",
        "3 large eggs",
        "70g grated Parmesan cheese",
        "Salt",
        "Black pepper"
    ],
    "instructions": "Updated instructions...",
    "category": "Pasta Carbonara"
}
```

### Delete a Recipe

**Request**:
```http
DELETE /api/recipes/1
```
**Response**:
```json
{
    "message": "The recipe has been deleted",
    "title": "Spaghetti Carbonara"
}
```

### Search Recipes

**Request**:
```http
GET /api/recipes/search?q=Spaghetti
```
**Response**:
```json
[
    {
        "id": 1,
        "title": "Spaghetti Carbonara",
        "description": "A classic Italian pasta dish with a creamy egg sauce.",
        "ingredients": [
            "200g spaghetti",
            "100g pancetta",
            "2 large eggs",
            "50g grated Parmesan cheese",
            "Salt",
            "Black pepper"
        ],
        "instructions": "...",
        "category": "Pasta"
    }
]
```
