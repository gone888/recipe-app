# recipe-app

- This is recipe app that is built with python using the Django framework. It has an admin panel to allow you to perform CRUD operations on the database, it also allows users to signup and create/view/edit/delete their recipes. Users are able to specify the recipe name, ingredients, and cooking time, the difficulty of the recipe is automatically calculated by a function that takes in the amount of ingredients and cooking time, users additionally can search for recipes by a specific ingredient.

## Technical Requirements

- Python 3.6+ and Django 3 compatibility.
- Exception handling with user-friendly error messages.
- PostgreSQL for production and SQLite for development database connectivity.
- Easy-to-use interface with simple forms and clear instructions.
- Code documentation and automated tests hosted on GitHub.
- Includes a "requirements.txt" for easy project setup.

## Key Features

- User authentication, login, and logout.
- Recipe search by recipe name.
- Automatic difficulty rating for each recipe.
- Error handling on user input.
- Detailed recipe information on demand.
- User recipe submissions with SQLite database integration.
- Django Admin dashboard for database management.
- Statistical analysis and visualization of recipe trends.

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/gone888/recipe-app.git
cd recipe-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Setup Database:

- Adjust the DATABASES configuration in settings.py for PostgreSQL and SQLite as per your development and production environments.

4. Run Migrations:

```bash
python manage.py migrate
```

5. Create Superuser for Admin Access:

```bash
python manage.py createsuperuser
```

6. Run the Development Server:

```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000 in your browser to view the app.
