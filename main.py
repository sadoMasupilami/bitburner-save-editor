import base64
import json

# file paths for reading and writing
IN_FILE = "../../Downloads/bitburnerSave.json"
OUT_FILE = "hack.json"

# What to edit
EDIT_MONEY = True
EDIT_HACKING = False
EDIT_COMBAT_SKILLS = False
EDIT_INTELLIGENCE = False
EDIT_KARMA = False
EDIT_FACTIONS = False

# values for editing
MONEY = 1000000000000
HACKING_SKILL = 15000
COMBAT_SKILL = 1500
INTELLIGENCE = 500
KARMA = -60000
FACTION_FAVOR = 4000

if __name__ == '__main__':

    with open(IN_FILE, "r") as f:
        content = f.read()
        content = base64.b64decode(content)
        json_content = json.loads(content)

        # Load data
        player_save = json.loads(json_content["data"]["PlayerSave"])
        factions_save = json.loads(json_content["data"]["FactionsSave"])
        all_servers_save = json.loads(json_content["data"]["AllServersSave"])
        companies_save = json.loads(json_content["data"]["CompaniesSave"])

        # edit data
        if EDIT_MONEY:
            player_save["data"]["money"] = MONEY
        if EDIT_HACKING:
            player_save["data"]["hacking"] = HACKING_SKILL
        if EDIT_COMBAT_SKILLS:
            player_save["data"]["strength"] = COMBAT_SKILL
            player_save["data"]["defense"] = COMBAT_SKILL
            player_save["data"]["dexterity"] = COMBAT_SKILL
            player_save["data"]["agility"] = COMBAT_SKILL
        if EDIT_INTELLIGENCE:
            player_save["data"]["intelligence"] = INTELLIGENCE
        if EDIT_KARMA:
            player_save["data"]["karma"] = KARMA
        if EDIT_FACTIONS:
            for k, v in factions_save.items():
                v["data"]["favor"] = FACTION_FAVOR

        # print some info
        world_daemon_hack_needed = all_servers_save["w0r1d_d43m0n"]["data"]["requiredHackingSkill"]
        print(f'Hacking needed for world daemon: {world_daemon_hack_needed}')

        # save data
        json_content["data"]["PlayerSave"] = json.dumps(player_save)
        json_content["data"]["FactionsSave"] = json.dumps(factions_save)
        json_content["data"]["AllServersSave"] = json.dumps(all_servers_save)
        json_content["data"]["CompaniesSave"] = json.dumps(companies_save)

    # for debugging inner json
    with open("out.json", "wb") as of:
        of.write(str.encode(json.dumps(player_save)))

    with open(OUT_FILE, "wb") as of:
        data = json.dumps(json_content)
        b64_data = base64.b64encode(data.encode('utf-8'))
        of.write(b64_data)
