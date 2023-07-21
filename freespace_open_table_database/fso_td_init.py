import sqlite3 as sql

def init_db():
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

    db.execute(
        """
        DROP TABLE IF EXISTS deprecations;
        """
    )

    db.execute(
        """
        DROP TABLE IF EXISTS parse_behaviors;
        """
    )

    db.execute(
        """
        DROP TABLE IF EXISTS restrictions;
        """
    )

    # add deprecations table
    db.execute(
        """
        CREATE TABLE deprecations(
        deprecation_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        date TEXT,
        version TEXT
        );
        """
    )

    # add parse behaviors table
    db.execute(
        """
        CREATE TABLE parse_behaviors(
        behavior_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        behavior TEXT
        );
        """
    )

    # add the restrictions table
    db.execute(
        """
        CREATE TABLE restrictions(
        restriction_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        min_value NUMERIC,
        max_value NUMERIC,
        max_string_length INTEGER,
        illegal_value_int INTEGER,
        illegal_value_float NUMERIC
        )
        """
    )

    # Add table table 
    db.execute(
        """
        CREATE TABLE tables (
        table_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT,
        filename VARCHAR(28) UNIQUE,
        modular_extension VARCHAR(5),
        description TEXT,

        );
        """
    )


    # Add items table, our most complex.  First half is actual info, Second Half is references to other tables
    # parent ID references another entry in the items table
    db.execute(
        """
        CREATE TABLE items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            item_text TEXT NOT NULL,
            documentation TEXT,
            info_type TEXT,
            major_version_added TEXT,
            parent_id INTEGER,
            
            table_id INTEGER,
            parse_behavior_id INTEGER,
            deprecation_id INTEGER,
            restriction_id INTEGR,
            FOREIGN KEY (table_id) REFERENCES tables(table_id),
            FOREIGN KEY (parse_behavior_id) REFERENCES parse_behavior(parse_behavior_id),
            FOREIGN KEY (deprecation_id) REFERENCES deprecations(deprecation_id),
            FOREIGN KEY (restriction_id) REFERENCES restrictions(restriction_id)
        );
        """
    )

    # Add table alias table
    db.execute(
        """
        CREATE TABLE table_aliases(
        alias_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        table_id INTEGER NOT NULL,
        filename VARCHAR(28) UNIQUE,
        FOREIGN KEY (table_id) REFERENCES tables(table_id)
        );
        """
    )

    print('Init Successful')
