from ModularOptions import *
import ModularOptions as op




#Stores info about the currently sellected item
blank_item = {
    "ItemName"            : "",
    "MinimumLevel"        : 0,
    "ItemType"            : "",
    "RequiresAttunement"  : False,

    "PrefixAugment"       : "None",
    "PrefixPower"         : 0, 
    "PrefixVariation"     : "None",

    "SuffixAugment"       : "None", 
    "SuffixPower"         : 0, 
    "SuffixVariation"     : "None",

    "TertiaryAugment"     : "None", 
    "TertiaryPower"       : 0, 
    "TertiaryVariation"   : "None",

    "TriggerAugment"      : "None", 
    "TriggerPower"        : 0, 
    "TriggerVariation"    : "None"
}

selected_item = blank_item.copy()
selected_slot = "Prefix"



########## Get Options for Dropdown menues =====================


#ensures that all of the slots in the selected slot are valid. If not it defults them to a value.
def selectedItemSanityCheck():
    for slot in ["Prefix", "Suffix", "Tertiary", "Trigger"]:
        enchant = getAugment(selected_item[slot + "Augment"])

        if selected_item["ItemType"] not in enchant.validItemTypes:
            selected_item[slot + "Augment"] = "None"
            selected_item[slot + "Power"] = 0
            selected_item[slot + "Variation"] = "None"
            continue

        if selected_item[slot + "Power"] not in enchant.power:
            selected_item[slot + "Power"] = list(enchant.power.keys())[0]

        if selected_item[slot + "Variation"] not in enchant.variations:
            selected_item[slot + "Variation"] = list(enchant.variations.keys())[0]


# returns a text list of options for creating dropdown menues.
def getDropdownOptions(dropDownType):
    selectedItemSanityCheck()

    #list the diffrent options of things to loop through
    enchant = getAugment(selected_item[selected_slot + "Augment"])
    options = [] 

    # getting options for item type
    if dropDownType == "ItemType": 
        for item in op.item_types[1:]: options.append(item)

    # getting options for augments
    if dropDownType == "Augment":
        for aug in op.Enhancements:
            if selected_slot in aug.validSlot \
            and selected_item["ItemType"] in aug.validItemTypes:
                options.append(aug.name)

    # getting options for power
    if dropDownType == "Power":
        for pow in enchant.power: options.append("Power Level: " + str(pow))
    
    # getting options for variation
    if dropDownType == "Variation":
        for entry in enchant.variations: options.append(entry)

    return options 

# function that returns an augment based on its name
def getAugment(name):
    for Enh in op.Enhancements:
        if name == Enh.name:
            return Enh
        
#gets the power level as an int from an option string
def getPowerLevel(powerLevel, desiredDataType="int"):
    if desiredDataType == "int": return int(powerLevel.lstrip("Power Level: "))
    if desiredDataType == "str": return f"Minimum level: {powerLevel}"

#check for attunment
def check_if_requires_attunement():
    selected_item["RequiresAttunement"] = False
    for slot in ('PrefixAugment', 
              'SuffixAugment', 
              'TertiaryAugment', 
              'TriggerAugment'):
        if getAugment(selected_item[slot]).attunement == True:
            selected_item["RequiresAttunement"] = True

#determin minimin level
def update_minimum_level():
    selected_item["MinimumLevel"] = 0
    for x in ('Prefix', 'Suffix', 'Tertiary', 'Trigger'):
        selected_item["MinimumLevel"] += selected_item[x + "Power"]


#get the cost to build the entire item
def getItemBuildCost():
    cost = 0
    for x in ('Prefix', 'Suffix', 'Tertiary', 'Trigger'): cost += getAugmentBuildCost(x)
    return cost
#get the cost to build an Augment
def getAugmentBuildCost(slot):
    aug = getAugment(selected_item[slot + "Augment"])
    cost = aug.costToBuild[0] + (selected_item["MinimumLevel"] * aug.costToBuild[1])
    return int(cost)


#Create a description based on the currently sellected item
def update_item_description():
    update_minimum_level()
    check_if_requires_attunement()
    item_description = selected_item['ItemName']
    if selected_item['MinimumLevel'] != 0: item_description += f"Minimum level: {selected_item['MinimumLevel']} "
    item_description += selected_item['ItemType']
    if selected_item['RequiresAttunement'] == True:
        item_description += "\nRequires Attunement"

    for x in ('Prefix', 'Suffix', 'Tertiary', 'Trigger'):
        if selected_item[x + "Augment"] != "None":
            item_description += "\n\n" + create_enhancement_description(x)
            
    return item_description

#create item description
def create_enhancement_description(slot_type):
    augment = getAugment(selected_item[slot_type + "Augment"])
    power = augment.power[selected_item[slot_type + "Power"]]
    variation = selected_item[slot_type + "Variation"]
    base_description = augment.description

    if selected_item[slot_type + "Variation"] != "None":
        flavortext = augment.variations[variation]['flavortext']
        aspect = augment.variations[variation]['aspect']
        
    else:
        flavortext = ""
        aspect = ""
        variation = selected_item[slot_type + "Augment"]

    name = slot_type + ": " + variation

    return name + "\n" + base_description\
        .replace("[flavortext]", flavortext)\
        .replace("[aspect]", aspect)\
        .replace("[power]", power)\
        .replace("[itemType]", selected_item['ItemType'])\
        .replace("  ", " ")\
        .lstrip(" ")

if __name__ == "__main__":
    print()
