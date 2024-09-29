# Flask Starter Project | Flask-Login, Flask-SQLAlchemy, FLASK-WTF, Flask-Injector, and Flask-Bootstrap

A Flask starter project with server-side setup, including:
- **Flask-Login**: For user authentication management.
- **Flask-SQLAlchemy**: For database ORM integration.
- **Flask-WTF**: For form validation on both client and server sides, with CSRF protection.
- **Flask-Injector**: For dependency injection
- **Flask-Bootstrap**: For serving bootstrap features


## Establish the app

- Create a virtual environment with all required dependencies by running those commands

```bash
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

- Set the environment variables based on your configuration in the `.env` file
```env
FLASK_DEBUG=True    # Enable hot reload and debug messages
CREATE_DATABASE_IF_NOT_FOUND=True   # Create new database file in case of there is no a database file already
DATABASE_TYPE=sqlalchemy    # The database type you want to use ["sqlalchemy", "mongodb"]
SQLALCHEMY_DATABASE_URI=sqlite:///DATABASE_FILE.db  # The sqlalchemy database connection string
MONGODB_DATABASE_URI=mongodb+srv://DATABASE_USER:DATABASE_PASSWORD@<DATABASE_HOST>/?retryWrites=true&w=majority&appName=Cluster0    # The mongodb database connection string from Atlas
MONGODB_DATABASE_NAME=test_db   # The mongodb database name
SECRET_KEY=     # The secret key used to encrypt the session content
LOGIN_MANAGER_LOGIN_VIEW=auth.login     # The login view based on the defined routes
```

- Run the flask app

```bash
python main.py
```