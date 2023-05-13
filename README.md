# Cinema Ticket Booking API

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