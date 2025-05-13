# User Authentication System

This project implements a user authentication system with registration, login, and protected routes. It uses Flask for the backend, JWT for token-based authentication, and MySQL for the database.

## Features

* **Registration:** Users can register with a username and password.  Optionally, a user role can be assigned (default: "user").
* **Login:** Users can log in with their username and password to receive a JWT token.
* **Authentication:** JWT token-based authentication for securing routes.
* **Protected Routes:** Only authenticated users with a valid token can access protected routes.
* **User Roles:** Supports user roles (e.g., "user", "admin") for authorization.
* **Database:** MySQL database to store user information.

## Dependencies

The project uses the following Python libraries:

* Flask: A web framework for building the API.
* PyJWT: For generating and verifying JSON Web Tokens.
* mysql-connector-python:  For connecting to the MySQL database.
* Werkzeug: For password hashing.

To install the dependencies, create a virtual environment and run:

```bash
pip install -r requirements.txt

Setup
Clone the repository:

git clone <repository_url>
cd <repository_name>

Set up the MySQL database:

Create a database named auth_db (or change the name in config.py).

Run the SQL script in database.sql to create the users table.

Configure the database connection settings in config.py.  You'll need to provide the host, user, password, and database name.

Configure the application:

Set the SECRET_KEY in config.py.  This key is used to sign the JWT tokens.  Important: Use a strong, random, and secret key.

Run the application:

python app.py

The server will start at http://localhost:5000 (or the configured port).

API Endpoints
The following API endpoints are available:

POST /api/auth/register:  Registers a new user.  Requires username, password, and optionally role in the request body.

Returns a 201 status code on success with a message.

Returns a 409 status code if the username already exists.

POST /api/auth/login:  Logs in a user.  Requires username and password in the request body.

Returns a 200 status code on success with a JWT token.

Returns a 401 status code for invalid credentials.

GET /api/auth/protected:  A protected route that requires a valid JWT token in the Authorization header.

Returns a 200 status code with a welcome message and the username of the authenticated user.

Returns a 403 status code if the token is missing, invalid, or expired.

The Authorization header should be in the format Bearer <token>.

Postman Collection
The Postman_Collection.json file provides a Postman collection with pre-defined requests for testing the API endpoints.  Import this collection into Postman to easily test the registration, login, and protected routes.

File Structure
app.py:  The main Flask application file.

config.py:  Configuration settings for the application (database connection, secret key).

database.sql:  SQL script to create the database table.

Postman_Collection.json:  Postman collection for testing the API.

requirements.txt:  List of Python dependencies.

auth.py:  Blueprint for authentication-related routes (register, login, protected).

user.py:  Contains the  create_user and get_user_by_username functions to interact with the database.

token.py: Contains the  generate_token and token_required functions for generating and validating JWTs.

Important Notes
Security: The SECRET_KEY in config.py is crucial for the security of your application.  Do not use the default key in a production environment. Generate a strong, random key and keep it secret.

Password Hashing: Passwords are stored in the database as hashed values using Werkzeug's generate_password_hash function.  Never store plain-text passwords.

Error Handling: The application includes basic error handling for registration, login, and token authentication.  You may want to add more robust error handling for a production environment.

Database Connection: The application uses a simple helper# Secured-User-Authentication-System-Project
