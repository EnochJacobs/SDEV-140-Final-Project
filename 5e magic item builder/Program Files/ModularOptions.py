item_types = ("", "Trinket", "Weapon", "Armor", "Shield", "Cape", "Hat", "Shoes") 

Enhancements = []

class Enhancement:
    def __init__(self, 
                name = "None", 
                validSlot = [], 
                attunement = False,
                validItemTypes = [],
                costToBuild = (0, 0), #left side is initial cost, right side is cost per power level
                power = {}, 
                variations = {"None" : {"aspect":"", "flavortext":""}},
                description = ""
                ):
        
        self.name = name
        self.validSlot = validSlot
        self.attunement = attunement
        self.validItemTypes = validItemTypes
        self.costToBuild = costToBuild
        self.power = power
        self.variations = variations
        self.description = description

    def getAttribute(self, atributeName):
        if atributeName == "Name": return self.name
        if atributeName == "validSlot": return self.validSlot
        if atributeName == "Attunement": return self.attunement
        if atributeName == "ValidItemTypes": return self.validItemTypes
        if atributeName == "costToBuild": return self.costToBuild
        if atributeName == "Power": return self.power
        if atributeName == "Variations": return self.variations
        if atributeName == "Description": return self.description


none = Enhancement(
    name = "None", 
    validSlot = ["Prefix", "Suffix", "Tertiary", "Trigger"],
    attunement = False,
    validItemTypes = item_types,
    costToBuild = (0, 0), 
    power = {0 : ""}, 
    variations = {"None" : {"aspect":"", "flavortext":""}},
    description = ""
)
Enhancements.append(none)


skill_boost = Enhancement(
    name = "Skill Boost", 
    validSlot = ["Prefix"], 
    attunement = True,
    validItemTypes = ["Trinket", "Weapon", "Armor", "Shield", "Cape", "Hat", "Shoes"],
    costToBuild = (200, 40), 
    power = {0:"1",  2:"2",  4:"3",  8:"4",  10:"5",  12:"6",  14:"7",  16:"8",  18:"9",  20:"10"}, 
    variations = {
        "Laboror's"       : {"aspect" : "Athletics",          "flavortext" : "r body grows accustomed hard work and physical strain"},
        "Tumbler's"       : {"aspect" : "Acrobatics",         "flavortext" : " are filled with the muscle memory of an acrobat"},
        "Theif's"         : {"aspect" : "Sleight of Hand",    "flavortext" : " gain greater control over your fingers"},
        "Stowaway's"      : {"aspect" : "Stealth",            "flavortext" : " become easier to overlook and draw less attention"},
        "Runecrafter's"   : {"aspect" : "Arcana",             "flavortext" : "r natural awareness of the weave of magical becomes stronger"},
        "Historian's"     : {"aspect" : "History",            "flavortext" : "r memory is improved and you feel a stronger connection to the past"},
        "Researcher's"    : {"aspect" : "Investigation",      "flavortext" : "r drawn towards new information and can systematically seek it out"},
        "Groundskeeper's" : {"aspect" : "Nature",             "flavortext" : " gain a stronger connection to the natural world"},
        "Worshipper's"    : {"aspect" : "Religion",           "flavortext" : " feel the eyes of a powerful entity upon you"},
        "Beastmaster's"   : {"aspect" : "Animal Handling",    "flavortext" : "r intentions bleed into minds of simple creatures"},
        "Detective's"     : {"aspect" : "Insight",            "flavortext" : " become more aware of the subtle mannerisms of others"},
        "Physician's"     : {"aspect" : "Medicine",           "flavortext" : " gain an intuitive sense of when and how something is hurting"},
        "Lookout's"       : {"aspect" : "Perception",         "flavortext" : " seem to have a sixth sense which alerts you to surroundings"},
        "Naturalist's"    : {"aspect" : "Survival",           "flavortext" : " feel a primal drive to reject society and live life on your own terms"},
        "Liar's"          : {"aspect" : "Deception",          "flavortext" : "r natural expressions are more controllable while faked ones seem more natural"},
        "Prosecutor's"    : {"aspect" : "Intimidation",       "flavortext" : " give off a menacing aura that weakens the nerve of those around you"},
        "Performer's"     : {"aspect" : "Performance",        "flavortext" : " move and speak with increased fluidity and grace"},
        "Diplomate's"     : {"aspect" : "Persuasion",         "flavortext" : "r words catch attention and seem more reasonable"},
        },
    description = "While attuned to this [itemType] you[flavortext]. Giving you a +[power] to your [aspect] checks."
    ) 
Enhancements.append(skill_boost)


ability_score_improvement = Enhancement(
    name = "Ability Score Improvement", 
    validSlot = ["Suffix"], 
    attunement = True,
    validItemTypes = ["Trinket", "Weapon", "Armor", "Shield", "Cape", "Hat", "Shoes"],
    costToBuild = (500, 250), 
    power = {0:"1",  4:"2",  8:"3",  12:"4",  16:"5",  20:"6"}, 
    variations = {
        "Bull's Might"      : {"aspect" : "Strength",       "flavortext" : "feel as strong as a mighty bull."},
        "Cat's Grace"       : {"aspect" : "Dexterity",      "flavortext" : "feel as limber as a dexterous cat."},
        "Bear's Endurance"  : {"aspect" : "Constitution",   "flavortext" : "feel as tough as an sturdy bear."},
        "Owl's Instincts"   : {"aspect" : "Wisdom",         "flavortext" : "become as wise as an astute owl."},
        "Fox's Cunning"     : {"aspect" : "Intelligence",   "flavortext" : "become as sly as a clever fox."},
        "Snake's Charm"     : {"aspect" : "Charisma",       "flavortext" : "become as alluring as an enchanting snake."},
        },
    description = "While attuned to this [itemType] you [flavortext]. Giving you a +[power] to your [aspect] score. This can increase your [aspect] score above 20, up to 2[power]."
    ) 
Enhancements.append(ability_score_improvement)


indestructibility = Enhancement(
    name = "Indestructibility", 
    validSlot = ["Tertiary"], 
    attunement = False,
    validItemTypes = ["Trinket", "Weapon", "Armor", "Shield", "Cape", "Hat", "Shoes"],
    costToBuild = (1000, 2500), 
    power = {0:"3rd level dispel magic", 1:"6th level dispel magic", 2:"Wish"}, 
    variations = {"None" : {"aspect":"", "flavortext":""}},
    description = "This [itemType] cannot be destroyed unless a [power] spell is cast on it first. At which point it can be destroyed like any other item for 1d8 days."
    ) 
Enhancements.append(indestructibility)


shifting_appearance = Enhancement(
    name = "Shifting Appearance", 
    validSlot = ["Tertiary", "Suffix"], 
    attunement = False,
    validItemTypes = ["Trinket", "Weapon", "Armor", "Shield", "Cape", "Hat", "Shoes"],
    costToBuild = (1000, 0), 
    power = {0:""}, 
    variations = {"None" : {"aspect":"", "flavortext":""}},
    description = "This [itemType] can change its appearence to look like another [itemType]. It can become 1 size category smaller or larger, though its properties remain the same no matter its appearance."
    ) 
Enhancements.append(shifting_appearance)


light = Enhancement(
    name = "Light", 
    validSlot = ["Tertiary", "Trigger"],
    attunement = False,
    validItemTypes = ["Trinket", "Weapon", "Armor", "Shield", "Cape", "Hat", "Shoes"],
    costToBuild = (300, 200), 
    power = {0 : " once per dawn, targeting this [itemType].", 1 : " as a bonus action, targeting this [itemType]", 2 : " as a bonus action."}, 
    variations = {"None" : {"aspect":"", "flavortext":""}},
    description = "You may cast the Light spell[power]"
)
Enhancements.append(light)


damage_on_hit = Enhancement(
    name = "Damage on Hit", 
    validSlot = ["Prefix"], 
    attunement = True,
    validItemTypes = ["Weapon", "Shield"],
    costToBuild = (100, 250), 
    power = {0 : "1",  2 : "1d6",  6 : "2d6",  10 : "3d6",  14 : "4d6",  18 : "5d6"}, 
    variations = {
        "Flame Touched"     : {"aspect" : "Fire", 
            "flavortext"    : f"This [itemType] is sheethed in magical flames."},
        "Snow Touched"      : {"aspect" : "Cold", 
            "flavortext"    : f"This [itemType] is sheethed in a layer of frost."},
        "Spark Touched"     : {"aspect" : "Lightning", 
            "flavortext"    : f"This [itemType] sheds sparks of electricity as it moves."},
        "Echo Touched"      : {"aspect" : "Thunder", 
            "flavortext"    : f"This [itemType] produces unusually loud sounds that reverberate in a musical fashion."},
        "Chemical Touched"  : {"aspect" : "Acid", 
            "flavortext"    : f"This [itemType] drips with a corosive but sweet smelling acid."},
        "Venom Touched"     : {"aspect" : "Poison", 
            "flavortext"    : f"This [itemType] causes a stinging pain when touched."},
        "Earth Touched"     : {"aspect" : "Bludgeoning", 
            "flavortext"    : f"This [itemType] has an unusual amount of inertial weight to it."},
        "Sky Touched"       : {"aspect" : "Piercing", 
            "flavortext"    : f"This [itemType] is followed by a trail of glimmering stars when moved at high speeds."},
        "Sea Touched"       : {"aspect" : "Slashing", 
            "flavortext"    : f"This [itemType] is covered in a thin film of water that rapidly flows across its surface."},
        "Void Touched"      : {"aspect" : "Force", 
            "flavortext"    : f"This [itemType] is seems to draw in upon itself, as if space itself is collapsing into it."},
        "Greif Touched"     : {"aspect" : "Psychic", 
            "flavortext"    : f"This [itemType] seems to whisper into your mind when you look at it for too long."},                    
        "Death Touched"     : {"aspect" : "Necrotic", 
            "flavortext"    : f"This [itemType] has a haunting aura about it."},
        "Sun Touched"       : {"aspect" : "Radiant", 
            "flavortext"    : f"This [itemType] has a righteous aura about it."},
    },
    description = "[flavortext] When you make an attack roll using this [itemType] it deals [power] extra [aspect] damage on hit."
)
Enhancements.append(damage_on_hit)


damage_on_crit = Enhancement(
    name = "Damage on Crit", 
    validSlot = ["Prefix", "Suffix"],
    attunement = False,
    validItemTypes = ["Weapon"],
    costToBuild = (500, 200), 
    power = {2 : "10",  6 : "20",  10 : "30",  14 : "40",  18 : "50"}, 
    variations = {
        "Burning"           : {"aspect" : "Fire", 
            "flavortext"    : f"conjures an eruption of molten lava"},
        "Blizzarding"       : {"aspect" : "Cold", 
            "flavortext"    : f"suddenly draws out all heat from its target"},
        "Storming"          : {"aspect" : "Lightning", 
            "flavortext"    : f"conjures a bolt of lightning from the sky or ceiling"},
        "Screaming"         : {"aspect" : "Thunder", 
            "flavortext"    : f"releases a sudden earsplitting scream"},
        "Scathing"          : {"aspect" : "Acid", 
            "flavortext"    : f"sprays its target with a shower of noxious chemicals"},
        "Contaminating"     : {"aspect" : "Poison", 
            "flavortext"    : f"injects its target with a highly potent fast action venom"},
        "Mauling"           : {"aspect" : "Bludgeoning", 
            "flavortext"    : f"crushes its target with several times its normal weight"},
        "Stabbing "         : {"aspect" : "Piercing", 
            "flavortext"    : f"conjures a cloud of spectral daggers which stab into its target"},
        "Lacerating"        : {"aspect" : "Slashing", 
            "flavortext"    : f"splits open thousands of tiny cuts all over the target's body"},
        "Calling"           : {"aspect" : "Force", 
            "flavortext"    : f"summons an atrial being for just a moment to join in the attack"},
        "Unsettling"        : {"aspect" : "Psychic", 
            "flavortext"    : f"wracks its target's psyche with horrible visions that tear at its mind"},                    
        "Rotting"           : {"aspect" : "Necrotic", 
            "flavortext"    : f"suddenly floods its target with dark energy"},
        "Smiting"           : {"aspect" : "Radiant", 
            "flavortext"    : f"suddenly floods its target with holy energy"},
    },
    description = "This [itemType] seems dormant, but there is a terrible power waiting just below the surface. \
When you crittically hit with this [itemType] it [flavortext] dealing [power] extra [aspect] damage."
)
Enhancements.append(damage_on_crit)


plus_x_weapon = Enhancement(
    name = "Enhanced Weapon", 
    validSlot = ["Tertiary"],
    attunement = False,
    validItemTypes = ["Weapon"],
    costToBuild = (500, 250), 
    power = {1 : "1", 5 : "2", 10 : "3"}, 
    variations = {"None" : {"aspect":"", "flavortext":""}},
    description = "This [itemType] has a +[power] to attack and damage rolls."
)
Enhancements.append(plus_x_weapon)


cantrip_SwordBurst = Enhancement(
    name = "Sword Burst", 
    validSlot = ["Trigger"],
    attunement = False,
    validItemTypes = ["Weapon"],
    costToBuild = (100, 500), 
    power = {0 : "3 times per dawn", 1 : "", 5 : "as a bonus action"}, 
    variations = {"None" : {"Intelligence"  : "", "flavortext":""},
                  "None" : {"Wisdom"        : "", "flavortext":""},
                  "None" : {"Charisma"      : "", "flavortext":""},
                  "None" : {"Strength"      : "", "flavortext":""},
                  "None" : {"Dexterity"     : "", "flavortext":""},
                  "None" : {"Constitution"  : "", "flavortext":""}},
    description = "While holding this [itemType] you may cast the Sword Burst spell [power]. \
[aspect] is your spellcasting ability for this spell.")
Enhancements.append(cantrip_SwordBurst)


plus_x_armor = Enhancement(
    name = "Enhanced Armor", 
    validSlot = ["Tertiary"],
    attunement = False,
    validItemTypes = ["Armor", "Shield"],
    costToBuild = (1000, 750), 
    power = {1 : "1", 5 : "2", 10 : "3"}, 
    variations = {"None" : {"aspect":"", "flavortext":""}},
    description = "While wearng this [itemType] you have +[power] armor class."
)
Enhancements.append(plus_x_armor)


energy_resistance = Enhancement(
    name = "Enhancement Bonus", 
    validSlot = ["Suffix"],
    attunement = True,
    validItemTypes = ["Armor", "Cape"],
    costToBuild = (1000, 750), 
    power = {4 : "have resistance",     12 : "are immune"}, 
    variations = {        
        "Fire Resistance"           : {"aspect" : "Fire", 
            "flavortext"            : f" feels comfortably cool to the touch"},
        "Cold Resistance"           : {"aspect" : "Cold", 
            "flavortext"            : f" feels comfortably warm to the touch"},
        "Lightning Resistance"      : {"aspect" : "Lightning", 
            "flavortext"            : f" gathers static and redirects it around the wearer"},
        "Thunder Resistance"        : {"aspect" : "Thunder", 
            "flavortext"            : f" absorbs noise incredibly well"},
        "Acid Resistance"           : {"aspect" : "Acid", 
            "flavortext"            : f" seems to repel grime and filth like water rolling off a ducks back"},
        "Poison Resistance"         : {"aspect" : "Poison", 
            "flavortext"            : f" draws toxins out of the skin and wicks them into itself like a sponge"},
        "Bludgeoning Resistance"    : {"aspect" : "Bludgeoning", 
            "flavortext"            : f" has shock absorbing properties"},
        "Piercing Resistance"       : {"aspect" : "Piercing", 
            "flavortext"            : f" seems to catch sharp pointed objects"},
        "Slashing Resistance"       : {"aspect" : "Slashing", 
            "flavortext"            : f" has lines running through it that are extra difficult to cut"},
        "Force Resistance"          : {"aspect" : "Force", 
            "flavortext"            : f" is surrounded by a thin barrier of arcane energy"},
        "Psychic Resistance"        : {"aspect" : "Psychic", 
            "flavortext"            : f" does not feel like anything and calms the mind"},                    
        "Necrotic Resistance"       : {"aspect" : "Necrotic", 
            "flavortext"            : f" is overflowing with life energy"},
        "Radiant Resistance"        : {"aspect" : "Radiant", 
            "flavortext"            : f" seems to always be cast in shadow, even when in direct sunlight"},},
    description = "This [itemType][flavortext]. While wearng it you [power] to [aspect] damage."
)
Enhancements.append(energy_resistance)


saves_boost = Enhancement(
    name = "Saving Throws", 
    validSlot = ["Prefix"],
    attunement = False,
    validItemTypes = ["Armor"],
    costToBuild = (1000, 750), 
    power = {0:"1",  3:"2",  6:"3",  9:"4",  12:"5",  15:"6"}, 
    variations = {
        "Steadfast"     : {"aspect" : "Strength",       "flavortext" : ""},
        "Evasive"       : {"aspect" : "Dexterity",      "flavortext" : ""},
        "Healthy"       : {"aspect" : "Constitution",   "flavortext" : ""},
        "Enlightened"   : {"aspect" : "Wisdom",         "flavortext" : ""},
        "Rational"      : {"aspect" : "Intelligence",   "flavortext" : ""},
        "Confident"     : {"aspect" : "Charisma",       "flavortext" : ""},},
    description = "While wearng this [itemType] you have +[power] to [aspect] saves."
)
Enhancements.append(saves_boost)



cantrip_Blade_Ward = Enhancement(
    name = "Blade Ward", 
    validSlot = ["Trigger"],
    attunement = False,
    validItemTypes = ["Armor"],
    costToBuild = (200, 400), 
    power = {0 : "3 times per dawn.", 1 : ".", 4 : "as a bonus action."}, 
    variations = {"None" : {"aspect":"", "flavortext":""}},
    description = "You may cast the Blade Ward spell [power]"
)
Enhancements.append(cantrip_Blade_Ward)


damage_when_hit = Enhancement(
    name = "Damage when Hit", 
    validSlot = ["Prefix"], 
    attunement = True,
    validItemTypes = ["Armor"],
    costToBuild = (100, 250), 
    power = {2 : "2",  5 : "5",  10 : "10",  14 : "15", 18 : "20"}, 
    variations = {
        "Flame Guard"     : {"aspect" : "Fire", 
            "flavortext"    : f"This [itemType] is sheethed in magical flames."},
        "Snow Guard"      : {"aspect" : "Cold", 
            "flavortext"    : f"This [itemType] is sheethed in a layer of frost."},
        "Spark Guard"     : {"aspect" : "Lightning", 
            "flavortext"    : f"This [itemType] sheds sparks of electricity as it moves."},
        "Echo Guard"      : {"aspect" : "Thunder", 
            "flavortext"    : f"This [itemType] produces unusually loud sounds that reverberate in a musical fashion."},
        "Chemical Guard"  : {"aspect" : "Acid", 
            "flavortext"    : f"This [itemType] drips with a corosive but sweet smelling acid."},
        "Venom Guard"     : {"aspect" : "Poison", 
            "flavortext"    : f"This [itemType] causes a stinging pain when touched."},
        "Earth Guard"     : {"aspect" : "Bludgeoning", 
            "flavortext"    : f"This [itemType] has an unusual amount of inertial weight to it."},
        "Sky Guard"       : {"aspect" : "Piercing", 
            "flavortext"    : f"This [itemType] is followed by a trail of glimmering stars when moved at high speeds."},
        "Sea Guard"       : {"aspect" : "Slashing", 
            "flavortext"    : f"This [itemType] is covered in a thin film of water that rapidly flows across its surface."},
        "Void Guard"      : {"aspect" : "Force", 
            "flavortext"    : f"This [itemType] is seems to draw in upon itself, as if space itself is collapsing into it."},
        "Greif Guard"     : {"aspect" : "Psychic", 
            "flavortext"    : f"This [itemType] seems to whisper into your mind when you look at it for too long."},                    
        "Death Guard"     : {"aspect" : "Necrotic", 
            "flavortext"    : f"This [itemType] has a haunting aura about it."},
        "Sun Guard"       : {"aspect" : "Radiant", 
            "flavortext"    : f"This [itemType] has a righteous aura about it."},
    },
    description = "[flavortext] When you are hit by an attack [itemType] your attacker takes [power] [aspect] damage."
)
Enhancements.append(damage_when_hit)





"""
"", "Trinket", "Weapon", "Armor", "Shield", "Cape", "Hat", "Shoes"
["Prefix", "Suffix", "Tertiary", "Trigger"]
[itemType] [flavortext] [power] [aspect]
Strength Dexterity Constitution Intelligence Wisdom  Charisma
While attuned to this [itemType]


"Shield"
Pre: Danceing Shield
Suf: Reflection
Ter: Shield Bashing
Tri: Toll the Dead

"Cape"
Pre: Heroic
Suf: Shadows
Ter: Billowing
Tri: Gust

"Hat"
Pre:
Suf: Nightvision
Ter: Waterbreathing 
Tri: Message

"Shoes"
Pre: Sheer footed
Suf: Striding 
Ter: False Tracks
Tri: Mold Earth
    

Of holding
Beast Senses
Returning
"""