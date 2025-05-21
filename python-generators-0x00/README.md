# Python Generators: Streaming SQL Data

This project sets up a MySQL database named `ALX_prodev`, seeds it with data from a CSV file, and prepares it for use with Python generators that stream SQL data row by row.

## 📁 Project Files

- `0-main.py`: Main script that runs the database setup and inserts sample data.
- `seed.py`: Contains functions for database connection, table creation, and data insertion.
- `user_data.csv`: CSV file with sample user data.
- `README.md`: Project documentation (this file).

## ✅ Objectives

- Connect to a MySQL server.
- Create a database `ALX_prodev` if it doesn’t already exist.
- Create a table `user_data` with the following fields:
  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Insert data from `user_data.csv` into the table.
- Prepare the database for generator-based row streaming.

## 🔧 Function Prototypes

Defined in `seed.py`:

```python
def connect_db():
    """Connects to the MySQL database server."""
