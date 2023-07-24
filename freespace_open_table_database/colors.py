import sqlite3 as sql



def init_colors_table():
    database = sql.connect('db/fso_td.db')

    db = database.cursor()

    db.execute(
        """
        INSERT INTO tables(name, filename, modular_extension, description) VALUES 
        ("#Start Colors", "Starts the color define section. ", "NULL", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Blue:, "Defines the color values for overriding Blue in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright Blue:, "Defines the color values for overriding Bright Blue in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Green:, "Defines the color values for overriding Green in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright Green:, "Defines the color values for overriding Bright Green in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Black:, "Defines the color values for overriding Black in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Grey:, "Defines the color values for overriding Grey in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Silver:, "Defines the color values for overriding Silver in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$White:, "Defines the color values for overriding White in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright White:, "Defines the color values for overriding Bright White in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Violet Gray:, "Defines the color values for overriding Violet Gray in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Violet:, "Defines the color values for overriding Violet in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Dim Red:, "Defines the color values for overriding Dim Red in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Red:, "Defines the color values for overriding Red in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright Red:, "Defines the color values for overriding Bright Red in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Pink:, "Defines the color values for overriding Pink in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Light Pink:, "Defines the color values for overriding Light Pink in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Yellow:, "Defines the color values for overriding Yellow in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Bright Yellow:, "Defines the color values for overriding Bright Yellow in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Orange:, "Defines the color values for overriding Orange in the UI.", "COLORALPHA", "3.8", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$UI Light Green:, "Defines the color values for overriding UI Light Green in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$UI Green:, "Defines the color values for overriding UI Green in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$UI Light Pink:, "Defines the color values for overriding UI Light Pink in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$UI Pink:, "Defines the color values for overriding UI Pink in the UI.", "COLORALPHA", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("#End", "Ends each color section.", "NULL", "2.0", (SELECT table_id FROM tables WHERE filename = 'COLORALPHA' LIMIT 1)),
        ("#Team Colors", "Starts the team color section. If used in a build before July 21st 2014, it requires that '#Start Colors' be used.", "NULL", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Team Name:, "Defines a team name to use for a new color scheme.", "STRING", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Team Stripe Color:, "Defines the RGB color for the team 'stripe.' This is applied to sections that go over the base color.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        ("$Team Base Color:, "Defines the RGB color for the team 'stripe.' This is applied to sections that go over the base color.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        (#Interface Colors, "Redefines colors used throughout FSO's interface. Can be defined either with the name of a color.", "COLOR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Colors' LIMIT 1)),
        
        """
        )
