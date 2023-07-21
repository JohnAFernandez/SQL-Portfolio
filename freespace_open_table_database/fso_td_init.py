import sqlite3 as sql

database = sql.connect('db/fso_td.db')

db = database.cursor()

# star from a blank state
db.execute(
    """
    DROP TABLE IF EXISTS tables;
    """
)

db.execute(
    """
    DROP TABLE IF EXISTS items;
    """
)

db.execute(
    """
    DROP TABLE IF EXISTS table_aliases;
    """
)

# Add table table 
db.execute(
    """
    CREATE TABLE tables (
    table_id INTEGER RIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    filename VARCHAR(28) UNIQUE,
    modular_extension VARCHAR(5),
    description TEXT    
    );
    """
)

# Add items table
db.execute(
    """
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        table_id INTEGER,
        item_text TEXT NOT NULL,
        documentation TEXT,
        parent_id INTEGER,
        version_added TEXT,
        deprecation_id INTEGER,
        FOREIGN KEY (table_id) REFERENCES tables(table_id)
    );
    """
)

# Add table alias Table
db.execute(
    """
    CREATE TABLE table_aliases(
    alias_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    table_id INTEGER NOT NULL,
    filename VARCHAR(28) UNIQUE
    );
    """
)


print('Successful')
