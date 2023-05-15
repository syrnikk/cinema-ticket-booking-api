# Cinema Ticket Booking API

## Installation
1. Checkout the project
```bash
$ git clone https://github.com/syrnikk/cinema-ticket-booking-api.git
```
2. Create a virtual environment with virtualenv module:
```bash
$ cd cinema-ticket-booking-api
$ python3 -m venv venv
```
3. After, active the virtual environment and install the requirements of project:
```bash
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```
4. Create .env file (example below):
```bash
$ touch .env
```
```dotenv
# project
PROJECT_NAME="Cinema Ticket Booking API"
VERSION=0.0.1
DEBUG=false
TESTING=false
# database
DATABASE_URL=sqlite:///./app.db?check_same_thread=False
# authentication
SECRET_KEY=83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
# mail
MAIL_USERNAME=cinema.ticket.booking.system@gmail.com
MAIL_PASSWORD=xymheszucdaukhxt
MAIL_FROM=cinema.ticket.booking.system@gmail.com
MAIL_PORT=465
MAIL_SERVER=smtp.gmail.com
MAIL_STARTTLS=false
MAIL_SSL_TLS=true
USE_CREDENTIALS=true
VALIDATE_CERTS=true
```
5. Run alembic to create database changes
```bash
$ alembic upgrade head
```

6. Run the application (port is optional):
```bash
$ uvicorn app.main:app --reload --port <port>
```

## OpenAPI Documentation

The API documentation is available at the following endpoint:

- **URL**: `/docs`
- **Method**: GET
- **Description**: This endpoint serves the OpenAPI documentation for the API. It provides detailed information about the available endpoints, request/response models, and authentication requirements.

To explore and interact with the API documentation, navigate to [http://your-api-url/docs](http://your-api-url/docs) in your web browser.

Please refer to the documentation for more information on how to use the API and the available endpoints.


## Alembic Database Migrations

Alembic is a database migration tool that helps manage changes to your database schema over time. It provides a way to create, apply, and revert database migrations.

### 1. Creating a Migration

To create a new migration, use the following command:
```sh
alembic revision --autogenerate -m "Your migration message"
```

This will automatically generate a new migration script based on the changes detected in your models or schema. You can then customize the migration script as needed.

### 2. Applying a Migration

To apply a migration and update the database schema, use the following command:

```sh
alembic upgrade head
```

This will apply all pending migrations up to the latest version. Alternatively, you can specify a specific version to upgrade to.

### 3. Reverting a Migration

If you need to revert a migration and roll back the database schema changes, use the following command:

```sh
alembic downgrade <target_version>
```

Replace `<target_version>` with the version you want to roll back to. This will revert all migrations applied after the specified version.

### 4. Viewing Migration History

To view the migration history and check the current version of the database schema, use the following command:

```sh
alembic history
```

This will display a list of migrations with their versions and revision IDs.