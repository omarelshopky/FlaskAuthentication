# Flask Starter Projects

This repository contains multiple starter projects demonstrating different approaches to handling user authentication in Flask applications.

All starter projects have:
- **Flask-SQLAlchemy**: Integrates SQLAlchemy ORM for database interactions.
- **Flask-Injector**: Supports dependency injection within your Flask application.

## Key Differences:

- **FlaskLogin**

Used for managing user sessions in stateful applications. It maintains session state on the server.

> Flask-Login has the notion of User as a person in its core model.
> This version also integrates Flask-WTF for form validation on both client and server sides, including CSRF protection.


- **FlaskJWT**

Used for stateless applications where authentication is managed through tokens. No session state is maintained on the server.

> Flask-JWT has User as a Client (consumer script, another application, an app...).
> This version includes Flask-Limiter to add rate-limiting capabilities, helping to control the API usage and protect against abuse.


## **Flask-Bootstrap** Integration

the `FlaskLoginBootstrap` subfolder contains all the functionality of **FlaskLogin**, but with added **Flask-Bootstrap** integration. This subfolder demonstrates how to use Flask-Bootstrap to enhance the visual appearance of your Flask application using Bootstrap's styling and components.