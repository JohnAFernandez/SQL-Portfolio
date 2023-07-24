import sqlite3 as sql



def init_colors_table():
    database = sql.connect('db/fso_td.db')

    db = database.cursor()

    db.execute(
        """
        INSERT INTO tables(name, filename, modular_extension, description) VALUES 
        ("#Start Colors", "Starts the color define section", "NULL", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Blue:, "Defines the color values for overriding Blue in the UI.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright Blue:, "Defines the color values for overriding Bright Blue.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Green:, "Defines the color values for overriding Green.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright Green:, "Defines the color values for overriding Bright Green.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Black:, "Defines the color values for overriding Black.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Grey:, "Defines the color values for overriding Grey.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$White:, "Defines the color values for overriding White.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright White:, "Defines the color values for overriding Bright White.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Violet Gray:, "Defines the color values for overriding Violet Gray.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Violet:, "Defines the color values for overriding Violet.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Dim Red:, "Defines the color values for overriding Dim Red.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Red:, "Defines the color values for overriding Red.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright Red:, "Defines the color values for overriding Bright Red.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("#End", "Ends the color section.", "NULL", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),

        """
        )
