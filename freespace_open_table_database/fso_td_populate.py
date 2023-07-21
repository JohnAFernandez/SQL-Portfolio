import sqlite3 as sql
import fso_td_init as init

init.init_db()

database = sql.connect('db/fso_td.db')

db = database.cursor()

db.execute(
    """
    INSERT INTO restrictions(min_value, max_value) VALUES
    (0.0, 1.0);
    """
)

db.execute(
    """
    INSERT INTO tables(name, filename, modular_extension, description) VALUES 
    ("AI Classes","Ai", "aic", "Defines the AI classes used in the game. This table is used to define each AI class with four abilities for each difficulty level."),
    ("AI Profiles","Ai_profiles", "aip", "Allows the creation and management of different patterns of AI behavior, called profiles. Profiles consist of various statistics and flags that provide some control over AI behavior. All options within a profile are optional; if an option is not specified it will follow the original FreeSpace 2 retail behavior. Different missions can specify different profiles."),
    ("Animations","Animation", "anim", "Specifies subobject animations for models. Animations in this form are only added in modular table files which end with -anim.tbm."),
    ("Armors", "Armor", "amr",  "Lets you define different damage types per armor."),
    ("Asteroids", "Asteroid", "ast", "Used to define all of the asteroids and debris field pieces in-game."),
    ("Autopilot","Autopilot", "aplt", "Used to define the autopilot behavior for a mod."),
    ("Cheats","Cheats", "cht", "Used to define the in-mission cheats for a mod"),
    ("Color Definitions", "Colors", "clr", "Allows editing of the default color values used for text in various game locations, as well as being used for team color declarations, redefining interface colors, and modifying or adding new color tags."),
    ("Math Curves", "Curves", "crv", "Allows for the defining of arbitrary mathematical functions, mappings from an arbitrary X value to an arbitrary Y value, and what X and Y are in each specific situation."),
    ("Default Keybindings","Controlconfigdefaults", NULL, "Can be used to modify the default key bindings in FSO."),
    ("Credits", "Credits", "crd", "Used to create permanent or semi-permanent effects, like impact marks for example."),
    ("Cutscenes","Cutscenes", "csn", "A file for defining the actual video clips and their descriptions displayed in the cutscenes section of the tech room."),
    ("Decals","Decals", "dcl", "Used to create permanent or semi-permanent effects, like impact marks for example."),
    ("Fireball Animations","Fireball", "fbl", "Used to define the usage of animations with certain special effects in game."),
    ("Fonts","Fonts", "fnt", "Allows the definition of unlimited, non-standard fonts."),
    ("Game Settings","Game_setings", "mod", "Defines options that can be changed globally."),
    ("Glowpoints","Glowpoints", "gpo", "Defines glowpoint lights for ships under the deferred lighting renderer."),
    ("Help Texts","Help", "hlp", "A file meant for defining the help texts that can be prompted for example in the mainhall and other such screens by pressing F1."),
    ("Hud Gauges","Hud_gauges", "hdg", "Used for modifying the elements of the HUD. Not all gauges can be modified."),
    ("Icons","Icons", "ico", "Defines icons used in mission briefings."),
    ("IFF Entries","Iff_defs", "iff", "Stores data on FS2's IFF (Identification Friend or Foe) entries."),
    ("Lighting Profiles","Lighting_Profiles", "ltp", "Provides controls for the game's lighting and rendering pipeline."),
    ("Lightning Storms","Lightning", "ltng", "Used to define the different storms seen in game"),
    ("Mainhalls","Mainhall", "hall", "Used to define the various main menu screens in the game"),
    ("Medals","Medals", "mdl", "Used for defining the various medals the player can achieve while playing the game."),
    ("Messages","Messages", "msg", "Used to link actions, animations, and sounds of the messages received during the mission. Personas are used to group messages by the same talker, for example, all the Wingman 1 (Male Terran Pilot) messages go with a Wingman 1 persona."),
    ("Muzzle Flashes","Mflash", "mfl", "Used to define different muzzleflashes that are seen in game."),
    ("Music","Music", "mus", "Defines the in-game soundtracks and menu music."),
    ("Nebulas","Nebula", "neb", "Used to define the various nebula bitmaps and poofs."),
    ("Object Types","Objecttypes", "obt", "Used to set attributes of different object types."),
    ("Particle Effects","Particle_effects", "part","Defines custom particle effects that can be assigned to various engine properties."),
    ("Post Processing", "Post_processing", NULL, "Controls the use of post-processing effects avaiable in FSO."),
    ("Ranks","Rank", "rnk", "Used to define different ranks that can be obtained during the game."),
    ("Scripting","Scripting", "sct", "Used for scripting special features like alternate HUDs or ship viewer into the game."),
    ("Ships","Ships", "shp", "Defines the ship classes used in FSO"),
    ("Sexps","Sexps", "sexp", "Supports adding custom SEXPs to a mod which have a user defined effect."),
    ("Sounds","Sounds", "snd", "Defines the various sounds played ingame."),
    ("Define Species","Species_defs", "sdf", "Allows the addition or replacement of species."),
    ("Tech Room Entries","Species", "intl", "Used to define the various intelligence clips found from tech room."),
    ("Subspace Missiles","Ssm", "ssm", "Defines the flight behavior of subspace missiles."),
    ("Background Graphics","Stars", "str", "Used to define available background graphics, all the stars or suns that create colored light for the game, and used debris animations."),
    ("Localization","Strings", "lcl", "Used for setting the various translations."),
    ("New Pilot Tips","Tips", "", "Used for defining the tips that pop-up in the main hall when a new pilot is created."),
    ("Traitor Text", "Traitor", "trtr", "Used for defining the text displayed when the player ends the mission with the Traitor IFF and the mission does not have the No Traitor flag."),
    ("Table String Translations", "Tstrings", "tlc", "Used for translations quite like the strings.tbl except that it is used for table strings."),
    ("Virtual POFs","Virtual_pofs", "", "Defines POF's that can be used from all other parts of the engine as if they were real, existing POF-files."),
    ("Explosion LODs","Weapon_expl", "wxp", "Defines the effect lods to use for weapon explosion effects."),
    ("Weapons","Weapons", "wep", "Defines the weapon classes used in FSO.");
    """
)

### Uncomment to test table population.
#test = db.execute("SELECT * FROM tables")
#
#for item in test:
#    print(item)


# quick hint
#            item_text TEXT NOT NULL,
#            documentation TEXT,
#            info_type TEXT,
#            major_version_added TEXT,

# Add AI table items
db.execute(
    """
    INSERT INTO items(item_text, documentation, info_type, major_version_added, table_id) VALUES
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("+nocreate", "Allows editing of the ai class entry without creating a new entry","NULL","23.2", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Accuracy:", "Allows editing of the ai class entry without creating a new entry","FLOAT_LIST5","23.2", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Evasion:", "How good the ship is at evading. Value defines the frequency of AI course changes while it is evading.", "FLOAT_LIST5", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Courage:", "How likely the ship is to chance danger to accomplish goals. Basically the lower the value sooner the AI will start evading when attacked and its less likely to target turrets.", "FLOAT_LIST5", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Patience:", "How willing the ship is to wait for an advantage before pursuing goals. Implemented in 3.6.12 in conjunction with the $Stalemate Time Threshold and $Stalemate Distance Threshold options, otherwise does nothing.", "FLOAT_LIST5", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Afterburner Use Factor:", "Affects how probably it is that the AI will use afterburners in "maybe" situations. A value of 1 means always, 2 means half the time, 3 a third of the time, etc.", "INT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Shockwave Evade Chances Per Second:", "Controls how likely it is for a ship to try to start evading a shockwave. The higher the number, the more "chances per second" the ship has to evade.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Get Away Chance:", "How likely the AI is to use a "get away" maneuver instead of simply making evasive turns. "Get away" usually involves the AI flying straight away, usually on afterburner, and making small jinking motions (instead of large evasive turns). Higher values result in more "jousting" fights. 0.0 is never, 1.0 is always.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Secondary Range Multiplier:", "Multiplier which affects from how far away the AI will begin firing secondary weapons. Capped by the actual maximum range of the weapon. Penalty for firing in nebula still applies above and beyond this. 0.0 never, 1.0 from max distance.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Autoscale by AI Class Index:", "If set to YES (default), a number of miscellaneous AI probabilities are affected by the order of the AI class in the file (for example, the chance to fire countermeasures). Classes near the beginning of the file are generally weaker than classes at the end. If set to NO, this flag will turn off that auto scaling behavior (so that the order of the AI class does not affect AI behavior).\n\n\tNote that even if this is set to NO, the other options above will still be controlled by AI class index (so if you want complete independence, you need to set all of the options listed in the "Other AI Class Attributes" category).", "BOOL_YESNO", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Name:", "Defines a name for the AI class that can be used with ships.tbl and also with FRED", "TEXT", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    
        
    """
)

#    ((SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1), "+nocreate", "Allows editing of the ai class entry without creating a new entry", "NULL", "", ,"23.2"),
#    ((SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1), "$Accuracy:", "How accurately the ship fires its weapons. Value is used to scale the error in the AI aim. With repeated shots, AI aim will improve. Note that the AI is always 100% accurate when aiming for subsystems, according to Retail code.", "FLOAT_LIST5", "", ,""),
#    ((SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1), "", "", "", "", ,""),


test = db.execute("SELECT * FROM items")

for item in test:
    print(item)
