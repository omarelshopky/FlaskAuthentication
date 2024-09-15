# Flask Starter Project | Flask-JWT-Extended, Flask-SQLAlchemy, and Flask-Injector

A Flask starter project with client-side setup, including:
- **Flask-JWT-Extended**: For authentication management.
- **Flask-SQLAlchemy**: For database ORM integration.
- **Flask-Injector**: For dependency injection
- **Flask-Limiter**: For rate limiting


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
CREATE_DATABASE_IF_NOT_FOUND=True    # Create new database file in case of there is no a database file already
SQLALCHEMY_DATABASE_URI=sqlite:///DATABASE_FILE.db    # The database connection string
SECRET_KEY=         # The secret key used to encrypt the session content
JWT_SECRET_KEY=     # The secret key used for JWT signature
JWT_ACCESS_TOKEN_EXPIRES=30
```

- Run the flask app

```bash
python main.py
```


## Endpoints Usage

### Auth Route

## /auth/signup

- Signup a new user in the database
  
**Request Body**
```json
{
    "username" : "YOUR_USERNAME",
    "password" : "YOUR_PASSWORD"
}
```

**Response**
- Registered Successfully
```json
{
    "msg": "User registered successfully"
}
```

- User Exist in the Database
```json
{
    "msg": "User already exists"
}
```

- Password less than 8 characters
```json
{
    "msg": "Weak password"
}
```

- Exceed Rate limit
```json
{
    "error": "rate limit exceeded"
}
```


### /auth/login
- Login with a specific user already in the database

**Request Body**
```json
{
    "username" : "YOUR_USERNAME",
    "password" : "YOUR_PASSWORD"
}
```

**Response**
- Login Successfully
```json
{
    "access_token": "YOUR_JWT_TOKEN"
}
```

- Wrong Credentials
```json
{
    "msg": "Invalid username or password"
}
```

- Exceed Rate limit
```json
{
    "error": "rate limit exceeded"
}
```


## /user/profile
- Just a test for an endpoint need users authentication to access

**Request Header**
```json
headers = {
  "Authorization": "Bearer <JWT_TOKEN>"
}
```

**Response**
- Authorized User
```
Hello to the protected area, your public id is <YOUR_ID>
```

- Exceed Rate limit
```json
{
    "error": "rate limit exceeded"
}
```