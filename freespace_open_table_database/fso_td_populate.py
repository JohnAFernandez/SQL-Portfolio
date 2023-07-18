import sqlite3 as sql

database = sql.connect('db/fso_td.db')

db = database.cursor()

db.execute(
    """
    INSERT INTO tables(name, filename, modular_extension) VALUES 
    ("AI","Ai", "aic"),
    ("AI Profiles","Ai_profiles", "aip"),
    ("Animation","Animation", ""),
    ("Armor","Armor", ""),
    ("Asteroid","Asteroid", ""),
    ("Autopilot","Autopilot", ""),
    ("Cheat","Cheats", ""),
    ("Text Colors","Colors", ""),
    ("Math Curves","Curves", " Allows for the defining of arbitrary mathematical functions, mappings from an arbitrary X value to an arbitrary Y value, and what X and Y are in each specific situation."),
    ("Default Keybindings","Controlconfigdefaults", NULL),
    ("Credits","Credits", "crd"),
    ("Cutscenes","Cutscenes", "csn"),
    ("","Decals", "dcl"),
    ("","Fireball", ""),
    ("","Fonts", ""),
    ("","Game_setings", ""),
    ("","Glowpoints", ""),
    ("","Help", ""),
    ("","Hud_gauges", ""),
    ("","Icons", ""),
    ("","Iff_defs", "")
    ("","Lighting_Profiles", "")
    ("","Lightning", "")
    ("","Mainhall", "")
    ("","Medals", "")
    ("","Messages", "")
    ("","Mflash", "")
    ("","Music", "")
    ("","Nebula", "")
    ("","Objecttypes", "")
    ("","Particle_effects", "")
    ("","Post_processing", "")
    ("","Rank", "")
    ("","Scripting", "")
    ("","Ships", "")
    ("","Sexps", "")
    ("","Sounds", "")
    ("","Species_defs", "")
    ("","Species", "")
    ("","Ssm", "")
    ("","Stars", "")
    ("","Strings", "")
    ("","Tips", "")
    ("","Traitor", "")
    ("","Virtual_pofs", "")
    ("","Weapon_expl", "")
    ("","Weapons", "")
    ("","", "")    
    """
)