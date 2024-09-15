# Flask Starter Projects

This repository contains multiple starter projects demonstrating different approaches to handling user authentication in Flask applications.

All starter projects have:
- **Flask-SQLAlchemy**: Integrates SQLAlchemy ORM for database interactions.
- **Flask-WTF**: Provides form validation on both client and server sides, including CSRF protection.
- **Flask-Injector**: Supports dependency injection within your Flask application.

## Key Differences:
- **Flask-Login**
Used for managing user sessions in stateful applications. It maintains session state on the server.
> Flask-Login has the notion of User as a person in its core model.


- **Flask-JWT**
Used for stateless applications where authentication is managed through tokens. No session state is maintained on the server.
> Flask-jwt has User as a Client (consumer script, another application, an app...).


- **Flask-Bootstrap**: Provides integration with Bootstrap to style and enhance the user interface of your Flask application.


## **Flask-Bootstrap** Integration (`bootstrap` Branch)

In addition to the above setups, the `bootstrap` branch contains the same configurations but with added **Flask-Bootstrap** integration. This branch demonstrates how to use Flask-Bootstrap to enhance the visual appearance of your Flask application with Bootstrap's styling and components.
