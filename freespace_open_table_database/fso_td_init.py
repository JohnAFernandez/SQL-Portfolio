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
    DROP TABLE IF EXISTS table_aliases ;
    """
)

# Add table table 
db.execute(
    """
    CREATE TABLE tables (
    table_id SERIAL PRIMARY KEY,
    name TEXT,
    filename VARCHAR(28) UNIQUE,
    modular_extension VARCHAR(5) UNIQUE,
    description TEXT,    
    );
    """
)

# Add items table
db.execute(
    """
    CREATE TABLE items (
        item_id SERIAL PRIMARY KEY,
        table_id INTEGER,
        item_text TEXT NOT NULL,
        documentation TEXT,
        parent_id INTEGER,
        version_added TEXT,
        deprecation_id INTEGER,
    )
    """
)

# Add Foreign Key to link table and items tables
db.execute(
    """
    ALTER TABLE items 
    ADD CONSTRAINT fk_items_tables
    FOREIGN KEY (table_id)
    REFERENCES tables(table_id)
    """
)

# Add table alias Table
db.execute(
    """
    CREATE TABLE table_aliases(
    alias_id SERIAL PRIMARY KEY,
    table_id INTEGER NOT NULL,
    filename VARCHAR(28) UNIQUE
    )
    """
)


print('Successful')
