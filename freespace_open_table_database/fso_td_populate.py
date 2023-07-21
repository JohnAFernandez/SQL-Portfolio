import sqlite3 as sql

database = sql.connect('db/fso_td.db')

db = database.cursor()

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

test = db.execute("SELECT * FROM tables")

for item in test:
    print(item)