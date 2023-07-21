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
    ("+nocreate", "Allows editing of the AI class entry without creating a new entry","NULL","23.2", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Accuracy:", "Allows editing of the AI class entry without creating a new entry","FLOAT_LIST5","23.2", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Evasion:", "How good the ship is at evading. Value defines the frequency of AI course changes while it is evading.", "FLOAT_LIST5", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Courage:", "How likely the ship is to chance danger to accomplish goals. Basically the lower the value sooner the AI will start evading when attacked and its less likely to target turrets.", "FLOAT_LIST5", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Patience:", "How willing the ship is to wait for an advantage before pursuing goals. Implemented in 3.6.12 in conjunction with the $Stalemate Time Threshold and $Stalemate Distance Threshold options, otherwise does nothing.", "FLOAT_LIST5", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Afterburner Use Factor:", "Affects how probably it is that the AI will use afterburners in 'maybe' situations. A value of 1 means always, 2 means half the time, 3 a third of the time, etc.", "INT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Shockwave Evade Chances Per Second:", "Controls how likely it is for a ship to try to start evading a shockwave. The higher the number, the more 'chances per second' the ship has to evade.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Get Away Chance:", "How likely the AI is to use a 'get away' maneuver instead of simply making evasive turns. 'Get away' usually involves the AI flying straight away, usually on afterburner, and making small jinking motions (instead of large evasive turns). Higher values result in more 'jousting' fights. 0.0 is never, 1.0 is always.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Secondary Range Multiplier:", "Multiplier which affects from how far away the AI will begin firing secondary weapons. Capped by the actual maximum range of the weapon. Penalty for firing in nebula still applies above and beyond this. 0.0 never, 1.0 from max distance.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Autoscale by AI Class Index:", "If set to YES (default), a number of miscellaneous AI probabilities are affected by the order of the AI class in the file (for example, the chance to fire countermeasures). Classes near the beginning of the file are generally weaker than classes at the end. If set to NO, this flag will turn off that auto scaling behavior (so that the order of the AI class does not affect AI behavior).\n\nNote that even if this is set to NO, the other options above will still be controlled by AI class index (so if you want complete independence, you need to set all of the options listed in the 'Other AI Class Attributes' category).", "BOOL_YESNO", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$AI Countermeasure Firing Chance:", "Overrides the AI_Profiles value for this AI class. Defines the chance a countermeasure will be fired by an AI-controlled ship (scaled by $Autoscale by AI Class Index:). ", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$AI In Range Time:", "Overrides the AI_Profiles value for this AI class. The delay (in seconds) for the AI to fire its weapons after getting in range.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$AI Always Links Ammo Weapons:", "Overrides the AI_Profiles value for this AI class. AI ships will link ballistic primaries if ammo levels are greater than these percents.", "FLOST_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$AI Maybe Links Ammo Weapons:", "Overrides the AI_Profiles value for this AI class. Defines the same as $AI Always Links Ammo Weapons: but in situations when its hull is below 33 % of maximum hitpoints. Overrides ai_profiles entry.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Predict Position Delay:", "Overrides the AI_Profiles value for this AI class. Sets the time after which the AI will recalculate the position of its target.\n\nIt does not apply to the AI's aim, it only applies to things like avoiding collisions and maneuvering at close range. Generally, anything other than a 0 just allows the AI to do monumentally stupid things like try to turn to avoid ramming where it thought you were 2 seconds ago.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$AI Shield Manage Delay:", "Overrides the AI_Profiles value for this AI class. Sets the time in seconds between each instance of an AI ship managing its shields", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Friendly AI Fire Delay Scale:", "Overrides the AI_Profiles value for this AI class. Sets the factor applied to 'fire wait' for friendly ships.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Hostile AI Fire Delay Scale:", "Overrides the AI_Profiles value for this AI class. Sets the factor applied to 'fire wait' for hostile ships", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$AI Turn Time Scale:", "Overrides the AI_Profiles value for this AI class. Defines the factor applied to time it takes for enemy ships to turn. A value of 1.0 means the ship turns at normal speed, 2.0 means half speed (takes twice as long), etc. Note that this value ONLY affects ships hostile to the player (always 1.0 for friendly ships).", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Glide Attack Percent:", "Overrides the AI_Profiles value for this AI class. How often the AI will use the 'glide attack' move when it has the opportunity. Glide attack means using glide to maintain course while aiming and firing at the current target. Only affects ships capable of glide.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Circle Strafe Percent:", "Overrides the AI_Profiles value for this AI class. How often the AI will use the 'circle strafe' move when it has the opportunity. Circle strafe means that the ship will attempt 'Descent-like' combat, trying to maintain distance while circling around the target using sidethrusters. Ships will only attempt this when sidethrust top speed is at least 2/3 of target's current velocity.", "FLOAT_LIST5", "2.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Glide Strafe Percent:", "Overrides the AI_Profiles value for this AI class. How often the AI will use the 'glide strafe' move when it has the opportunity. Glide strafe means using glide to attack capships by flying past and shooting at them. Only affects ships capable of glide.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Stalemate Time Threshold:", "Overrides the AI_Profiles value for this AI class. The minimum amount of time required for the AI to detect a 'stalemate' situation. If a ship and its target have been within a certain distance of each other (defined by $Stalemate Distance Threshold) for this amount of time without either of them scoring a hit on the other, the AI will do something to break the stalemate. Only applies to small ships. If this value is 0 or less, no stalemate detection is performed.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Stalemate Distance Threshold:", "Overrides the AI_Profiles value for this AI class. The maximum distance that an AI ship must remain from its target for a 'stalemate' to occur (see $Stalemate Time Threshold).", "FLOAT_LIST5", "3,6,12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Chance AI Has to Fire Missiles at Player:", "Overrides the AI_Profiles value for this AI class. Chance for an AI to hesitate about firing a secondary or homing turret weapon at the player. Values range from 0-6, at 0 they will frequently hesitate, at 6 they will never hesitate.\n\nMechanic details: AIs are only allowed to fire homing secondaries or turrets with homing weapons at the player in a limited window of time. The window starts every ten seconds, and lasts (value + 1) 7ths of that ten second cycle. Each ship has it's own cycle, so their windows are not all synchronized.", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Max Aim Update Delay:", "Overrides the AI_Profiles value for this AI class. Maximum amount of delay allowed before the AI will update its aim. Until the next update, the AI will project the target forward based on last checked position and velocity. Applies to small ships vs small ships (dogfights). The actual delay is randomly selected between 0 and the maximum (so setting a value of 2 will result in an average of 1 second delay).", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$Turret Max Aim Update Delay:", "Overrides the AI_Profiles value for this AI class. As $Max Aim Update Delay, but affecting turrets instead", "FLOAT_LIST5", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$big ships can attack beam turrets on untargeted ships:", "Overrides the AI_Profiles value for this AI class. If set, big ships can attack a beam turret that's firing on them from a ship that they don't currently have targeted.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$smart primary weapon selection:", "Overrides the AI_Profiles value for this AI class. If set, enables the new primary weapon selection method", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$smart secondary weapon selection:", "Overrides the AI_Profiles value for this AI class. If set, enables the new secondary weapon selection method (including proper use of bomber+ missiles)", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$smart shield management:", "Overrides the AI_Profiles value for this AI class. If set, shields will devote all their charging energy to the weakest quadrant(s) and not waste energy on fully-charged quadrants (previously was -smart_shields on the command line)", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$smart afterburner management:", "Overrides the AI_Profiles value for this AI class. If set, the AI will properly use brief pulses of afterburner power instead of afterburning until fuel is exhausted.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$allow rapid secondary dumbfire:", "Overrides the AI_Profiles value for this AI class. If set, allows an AI ship to switch to rapid fire for dumbfire missiles.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$huge turret weapons ignore bombs:", "Overrides the AI_Profiles value for this AI class. If set, causes huge turret weapons (including anti-capship beams) to not target bombs.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$don't insert random turret fire delay:", "Overrides the AI_Profiles value for this AI class. If set, removes the random turret fire delay (from .1 to .9 seconds) inserted in addition to AI Fire Delay Scale.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$prevent turrets targeting too distant bombs:", "Overrides the AI_Profiles value for this AI class. If set, prevents turrets from targeting bombs beyond maximum range of the weapons of the turret..", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$smart subsystem targeting for turrets:", "Overrides the AI_Profiles value for this AI class. If set, prevents turrets from trying to target subsystems beyond their fov limits, also keeps the turret subsystem targeting preference order intact regardless of the angle to the target.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$allow turrets target weapons freely:", "Overrides the AI_Profiles value for this AI class. If set, allows turrets to target any weapons instead of just targeting bombs, to be used in conjunction with target priorities setup.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$allow vertical dodge:", "Overrides the AI_Profiles value for this AI class. If set, allows ships to dodge weapons fire vertically as well as horizontally.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$No extra collision avoidance vs player:", "Overrides the AI_Profiles value for this AI class. If set, allows ships to dodge weapons fire vertically as well as horizontally.", "BOOL_FLEX", "3.6.12", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$all ships manage shields:", "Overrides the AI_Profiles value for this AI class. Allows AI to manage shields on big ships", "BOOL_FLEX", "3.6.14", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$ai can slow down when attacking big ships:", "Overrides the AI_Profiles value for this AI class. When set, fighters attacking big ships will slow down depending on how long they've been attacking (80% speed after 5 seconds, 60% after 8 seconds, 40% after 10 seconds, and 20% after 15 seconds), how long it's been since they were last shot (full throttle if it was within the past 6 seconds), and how close they are (full throttle if the target is more than 1200 meters away).", "BOOL_FLEX", "3.8.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)),
    ("$use actual primary range:", "Overrides the AI_Profiles value for this AI class. When set, fighters will no longer fire primary weapons at targets outside their range just because weapon travel time would be sufficiently short.", "BOOL_FLEX", "19.0", (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1))        
    """
)

### Uncomment to test ai table population.
#test = db.execute("SELECT * FROM items WHERE table_id = (SELECT table_id FROM tables WHERE filename = 'Ai' LIMIT 1)")
#
#for item in test:
#    print(item)

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
