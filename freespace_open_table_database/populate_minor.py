import sqlite3 as sql

def init_minor_tables():
    database = sql.connect('db/fso_td.db')

    db = database.cursor()

    # populate tips table
    db.execute(
        """
        INSERT INTO items(item_text, documentation, info_type, major_version_added, table_id) VALUES
        ("+Tip", "Defines the text for the tip as an XSTR (provides translation index).", "XSTR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Tips' LIMIT 1)),
        ("#End", "Ends the table.", "NULL", 2.0, (SELECT table_id FROM tables WHERE filename = 'Tips' LIMIT 1))
        """
    )

    ### Uncomment to test tips table population.
    #test = db.execute("SELECT * FROM items WHERE table_id = (SELECT table_id FROM tables WHERE filename = 'Tips' LIMIT 1)")
    #
    #for item in test:
    #    print(item)


    # populate the traitors table
    db.execute(
        """
        INSERT INTO items(item_text, documentation, info_type, major_version_added, table_id) VALUES
        ("#Debriefing_info", "Required formatting to start traitor.tbl.", "NULL", "2.0", (SELECT table_id FROM tables WHERE filename = 'Traitor' LIMIT 1)),
        ("$Num stages:", "Field to mark how many debrief stages are in the traior debriefing. Must be 1. There is no support for a multi stage traitor debrief. Optional as of 23.0.", "INTEGER", "2.0", (SELECT table_id FROM tables WHERE filename = 'Traitor' LIMIT 1)),
        ("$Formula:", "Sets the trigger for the traior debriefing.  Should be '( true )', as optional traitor stages are not supported. Optional as of 23.0.", "INTEGER", "2.0", (SELECT table_id FROM tables WHERE filename = 'Traitor' LIMIT 1)),
        ("$Multi text", "The text for the debriefing in XSTR format.\n\nStarting with 21.0, multiple $Multi text fields may exist, each (except for the default) followed by its own Persona. The mission's Debriefing Persona Index controls which one is used.", "XSTR", "2.0", (SELECT table_id FROM tables WHERE filename = 'Traitor' LIMIT 1)),
        ("+Persona:", "Optional. Defines the persona associated with the muti text before it. If specified, this particular text will be chosen when the Debriefing Persona Index matches. The Debriefing Persona is a number set for a given mission using the campaign editor.", "INTEGER", "21.0", (SELECT table_id FROM tables WHERE filename = 'Traitor' LIMIT 1)),
        ("$Voice:", "Defines the base voice file that is played during the traitor debriefing.\n\nAs of 21.0: if the value of Debriefing Persona for the mission has been set, that value plus an underscore plus the base filename becomes the filename FSO will search for. For example, if this value is set to traitor_debrief.ogg and the Debriefing Persona value is 10, FSO will look for and play the file 10_traitor_debrief.ogg. If this persona-specific file cannot be found, the base filename on its own - for example traitor_debrief.ogg - will be played instead. Note that the value of $Voice: is only defined once in the table, regardless of however many personas are present in the campaign, just as is the case with rank.tbl voice files.", "STRING", "2.0", (SELECT table_id FROM tables WHERE filename = 'Traitor' LIMIT 1))

        """
    )

    ### Uncomment to test tips table population.
    #test = db.execute("SELECT * FROM items WHERE table_id = (SELECT table_id FROM tables WHERE filename = 'Traitor' LIMIT 1)")
    #
    #for item in test:
    #    print(item)
