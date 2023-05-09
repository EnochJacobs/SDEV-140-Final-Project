import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import ModularOptions as op
import Functions as fun


#================================== UPDATE STATE FUNCTION =========================================
def updateState():
    resetInvalidDDMSelections()
    fun.update_minimum_level()
    updateimage()
    updateCostBox()    
    updateNameplate()
    updateItemDescription()
  

def copySelectedItem(from_, to_):
    for item in [
        "ItemName", "MinimumLevel", "ItemType", "RequiresAttunement", "PrefixAugment", "PrefixPower",
        "PrefixVariation", "SuffixAugment", "SuffixPower", "SuffixVariation", "TertiaryAugment",
        "TertiaryPower", "TertiaryVariation", "TriggerAugment", "TriggerPower", "TriggerVariation"]:
        to_[item] = from_[item]


#================================== SCREEN BASICS =========================================
# base window 
window = tk.Tk()
window.title("Item Generator Program")
window.geometry("958x562")
window.configure(bg='#555')
window.iconbitmap('images/favicon.ico')

# define / add the header
header = LabelFrame(window, bg="#999", width="1000", height="40")
header.grid(row=0, column=0, columnspan=3) 
# define / add the leftside frame
leftside = LabelFrame(window, bg="#999", width="325", height="560")
leftside.grid(row=1, column=0) 
# define / add the middle frame
middle = LabelFrame(window, bg="#999", width="350", height="560")
middle.grid(row=1, column=1)
# define / add the rightside frame
rightside = LabelFrame(window, bg="#999", width="325", height="560")
rightside.grid(row=1, column=2)

#======================================= HEADER TABS =========================================
#=============================================================================================

# Clear Tabs function to clean the screen whe tabs are clciked
def ClearTab():
    for item in [ CompletedItemsDispaly, ModifyButton, SalvageButton, TotaCostBox, EnchantCostBox, 
        ItemTypeOptionDDM, AugmentOptionDDM, PowerOptionDDM, VariationOptionDDM,
        SelectPrefix, SelectSuffix, SelectTertiary, SelectTrigger, CreateButton ]:
        item.grid_forget()

# Define Completed Items Tab function on click
def LoadTab_Click():
    ClearTab()
    showCompletedItemsList()
    showModifyButton()
    showSalvageButton()
    CreateTab.config(state="normal")
    LoadTab.config(state="disabled")

# Define and add Completed Items Tab 
LoadTab = Button(header, text="Completed Items", padx=25, command=LoadTab_Click)
LoadTab.grid(row=0, column=1, padx=(0,360))

# Define Create New Item Tab function on click
def CreateTab_Click():
    ClearTab()
    showDDMs()
    showCostBoxes()
    showCreateButton()
    showSlotSelection()
    CreateTab.config(state="disabled")
    LoadTab.config(state="normal")

# Define and add Create New Item Tab
CreateTab = Button(header, text="Create New Item", padx=25, command=CreateTab_Click)
CreateTab.grid(row=0, column=0, padx=(295, 1))


#====================================== Cost Boxes ===========================================
#=============================================================================================

# function that updates what is displayed in cost boxes
def updateCostBox():
    EnchantCost = "Enchant Cost: " + str(fun.getAugmentBuildCost(fun.selected_slot)) + " gold"
    TotaCost = "Tota Cost: " + str(fun.getItemBuildCost()) + " gold"
    TotaCostBox.config(text=TotaCost)
    EnchantCostBox.config(text=EnchantCost)

# variable that holds the content for cost boxes
EnchantCost = "Enchant Cost: " + str(fun.getAugmentBuildCost(fun.selected_slot)) + " gold"
TotaCost = "Tota Cost: " + str(fun.getItemBuildCost()) + " gold"

# define cost boxes
TotaCostBox = Label(leftside, text=TotaCost, bg="#fff", width=30, pady=5)
EnchantCostBox = Label(leftside, text=EnchantCost, bg="#fff", width=30, pady=5)

# add cost boxes
def showCostBoxes():
    TotaCostBox.grid(row=8, column=0, pady=(10, 0))
    EnchantCostBox.grid(row=9, column=0, pady=(0, 75))


#================================== DROPDOWN MENUES  =========================================
#=============================================================================================

# sanity check that resets selections that are no longer valid
def resetInvalidDDMSelections():
    ItemTypeOptionDDM.set(fun.selected_item["ItemType"])
    AugmentOptionDDM.set(fun.selected_item[fun.selected_slot + "Augment"])
    PowerOptionDDM.set(fun.selected_item[fun.selected_slot + "Power"])
    VariationOptionDDM.set(fun.selected_item[fun.selected_slot + "Variation"])

    augs = fun.getDropdownOptions("Augment")
    pows = fun.getDropdownOptions("Power")
    varis = fun.getDropdownOptions("Variation")
    for DDM, opts in zip([AugmentOptionDDM, PowerOptionDDM, VariationOptionDDM], 
                         [augs, pows, varis]):
        DDM.config(value = opts)
        if DDM.get() not in opts: DDM.current(0)
    
    PowerOptionDDM.set(fun.getPowerLevel(fun.selected_item[fun.selected_slot + "Power"], "str"))

# function on click
def clickDropdown(letter):
    if letter == "T": fun.selected_item["ItemType"] = ItemTypeOptionDDM.get()
    if letter == "A": fun.selected_item[fun.selected_slot + "Augment"] = AugmentOptionDDM.get()
    if letter == "P": fun.selected_item[fun.selected_slot + "Power"] = fun.getPowerLevel(PowerOptionDDM.get())
    if letter == "V": fun.selected_item[fun.selected_slot + "Variation"] = VariationOptionDDM.get()
    updateState()

# Define Dropdowns 
# Item Type Dropdown 
ItemTypeOptionDDM = ttk.Combobox(leftside, state="readonly",
value = fun.getDropdownOptions("ItemType"), width=25, font="Helvetica 11")
ItemTypeOptionDDM.bind("<<ComboboxSelected>>", lambda x: clickDropdown("T"))

# Augment Dropdown 
AugmentOptionDDM = ttk.Combobox(leftside, state="readonly",
value = fun.getDropdownOptions("Augment"), width=25, font="Helvetica 11")
AugmentOptionDDM.bind("<<ComboboxSelected>>", lambda x: clickDropdown("A"))
# Power Dropdown 
PowerOptionDDM = ttk.Combobox(leftside, state="readonly",
value = fun.getDropdownOptions("Power"), width=25, font="Helvetica 11")
PowerOptionDDM.bind("<<ComboboxSelected>>", lambda x: clickDropdown("P"))
# Variation Dropdown 
VariationOptionDDM = ttk.Combobox(leftside, state="readonly",
value = fun.getDropdownOptions("Variation"), width=25, font="Helvetica 11")
VariationOptionDDM.bind("<<ComboboxSelected>>", lambda x: clickDropdown("V"))

# set Dropdowns values
AugmentOptionDDM.current(0)
PowerOptionDDM.current(0)
VariationOptionDDM.current(0)


# Build Dropdowns
def showDDMs():
    ItemTypeOptionDDM.grid(row=0, column=0, pady=(23, 20), padx=20)
    AugmentOptionDDM.grid(row=5, column=0)
    PowerOptionDDM.grid(row=6, column=0, pady=15)
    VariationOptionDDM.grid(row=7, column=0, pady=(0, 40))


#=============================== Enchant Slot Selection Buttons ==============================
#=============================================================================================

# Selection Buttons on clcik function
def clickSlotSelect(slotType):
    fun.selected_slot = slotType
    resetInvalidDDMSelections()
    updateCostBox()

# Selection Buttons Variabe
SelectedEnchant = StringVar()
SelectedEnchant.set("Prefix")

# Define Selection Buttons
SelectPrefix = Radiobutton(leftside, text="Item Prefix", width=24,
    variable=SelectedEnchant, value="Prefix", command=lambda: clickSlotSelect("Prefix"))
SelectSuffix = Radiobutton(leftside, text="Item Suffix", width=24,
    variable=SelectedEnchant, value="Suffix", command=lambda: clickSlotSelect("Suffix"))
SelectTertiary = Radiobutton(leftside, text="Item Tertiary", width=24,
    variable=SelectedEnchant, value="Tertiary", command=lambda: clickSlotSelect("Tertiary"))
SelectTrigger = Radiobutton(leftside, text="Item Trigger", width=24,
    variable=SelectedEnchant, value="Trigger", command=lambda: clickSlotSelect("Trigger"))

# Build Selection Buttons
def showSlotSelection():
    SelectPrefix.grid(row=1, column=0, pady=(20, 3), padx=(34, 35))
    SelectSuffix.grid(row=2, column=0, pady=3)
    SelectTertiary.grid(row=3, column=0, pady=3)
    SelectTrigger.grid(row=4, column=0, pady=(3, 40))



#================================= Completed Items Dispaly ===================================
#=============================================================================================

# update the Completed Items Dispaly
def updateCompletedItemsDispaly():
    CompletedItemsDispaly.delete(0, "end")
    for item in Completed_Items:
        CompletedItemsDispaly.insert("end", generateName(item))


def clickCompletedItemsDispaly(args):
    if CompletedItemsDispaly.curselection() != ():
        selected = CompletedItemsDispaly.curselection()[0]
        selected = Completed_Items[selected]
        copySelectedItem(selected, fun.selected_item)  
        updateState()

# create an array to hold completed items
Completed_Items = []
# define completed items Dispaly
CompletedItemsDispaly = Listbox(leftside, width=39, height=28)
CompletedItemsDispaly.bind("<<ListboxSelect>>", clickCompletedItemsDispaly)
# add completed items Dispaly
def showCompletedItemsList(): CompletedItemsDispaly.grid(row=0, column=0, pady=(25, 0), padx=(14, 13))


#====================================== Create Button ========================================
#=============================================================================================

bigFont = font.Font(family='Helvetica', size=25)

def ConfirmCreate():
    new_item = {}
    copySelectedItem(fun.selected_item, new_item)  
    Completed_Items.append(new_item)
    copySelectedItem(fun.blank_item, fun.selected_item)
    updateCompletedItemsDispaly()
    updateState()
    
def clickCreateButton():
    if fun.selected_item["ItemType"] != "":
        PopupWindow("Create")

CreateButton = Button(middle, text="Create", width=9, font=bigFont, command=clickCreateButton)
def showCreateButton(): CreateButton.grid(row=3, column=0, padx=25, pady=24)



#================== Salvage Button ================
def ConfirmSalvage():
    selected = CompletedItemsDispaly.curselection()[0]
    Completed_Items.pop(selected)
    copySelectedItem(fun.blank_item, fun.selected_item)
    updateCompletedItemsDispaly()
    updateState()

def clickSalvageButton():
    if CompletedItemsDispaly.curselection() != ():
        PopupWindow("Salvage")

SalvageButton = Button(middle, text="Salvage", width=9, font=bigFont, command=clickSalvageButton)
def showSalvageButton(): SalvageButton.grid(row=3, column=0, padx=25, pady=24)

   
#================== Popup Window ================



def PopupWindow(popupType):
    submitName()
    def popupConfirm(choice):
        Popup.destroy()
        if choice == "Y" and popupType == "Salvage": ConfirmSalvage()
        if choice == "Y" and popupType == "Create": ConfirmCreate()


    Popup = Toplevel(window)
    Popup.title("Confirm " + popupType)


    if popupType == "Salvage":
        try: salvageAmount = int(fun.getItemBuildCost() / 2.50)
        except: salvageAmount = 0
        message = f"Are you sure want to salvage {generateName()} for {salvageAmount} gold?"
    if popupType == "Create": message = f"Are you sure want to build {generateName()} for {fun.getItemBuildCost()} gold?"


    PopupMessage = Label(Popup, text=message, wraplength=300, justify="center", padx=30, pady=20) 
    PopupMessage.grid(row=0, column=0, columnspan=2)

 

    yesButton = Button(Popup, text="Yes", width=6, command=lambda: popupConfirm("Y"))
    yesButton.grid(row=1, column=0, pady=(0, 20))

    noButton = Button(Popup, text="No", width=6, command=lambda: popupConfirm("N"))
    noButton.grid(row=1, column=1, pady=(0, 20))


    





#================================== Modify Button  =========================================
#=============================================================================================

def clickshowModifyButton():
    if CompletedItemsDispaly.curselection() != ():
        selected = CompletedItemsDispaly.curselection()[0]
        Completed_Items.pop(selected)
        updateCompletedItemsDispaly()
        CreateTab_Click()


ModifyButton = Button(leftside, text="Modify Item", padx=12, command=clickshowModifyButton)

def showModifyButton(): ModifyButton.grid(row=1, column=0, padx=20, pady=(0, 23))

#================================== ITEM NAME PLATE  =========================================
#=============================================================================================

# gets the name of an item or generates a name based on the items properties  
# uses the current item selection unless specified  
def generateName(item=fun.selected_item):
    Name = item["ItemName"]
    
    if Name == "":
        PrefixA = item["PrefixAugment"]  
        PrefixV = item["PrefixVariation"]
        SuffixA = item["SuffixAugment"]
        SuffixV = item["SuffixVariation"]

        if PrefixV == "None":
            if PrefixA != "None": Name += PrefixA + " "
        else: Name += PrefixV + " " 

        Name += item["ItemType"]

        if SuffixV == "None": 
            if SuffixA != "None": Name += " of " + SuffixA
        else: Name += " of " + SuffixV

    return Name

# function that updates the name plate
def updateNameplate(): ItemNamePlate.config(text=generateName())

# function that runs when the name plate is clicked
def clickNameplate(): 
    ItemNamePlate.grid_forget()
    ItemEntryPrompt.grid(   row=0, column=0, padx=(116, 117), pady=(18, 0))
    ItemEntry.grid(         row=1, column=0, pady=(0, 28))

# function that runs when the name entry is submited
def submitName(args=""):
    ItemEntryPrompt.grid_forget()
    ItemEntry.grid_forget()
    ItemNamePlate.grid(row=1, column=0, padx=23, pady=(23, 22))
    fun.selected_item["ItemName"] = ItemEntry.get()
    updateNameplate()

# define and add the name plate
ItemNamePlate = Button(middle, text="", width=42, height=2, command=clickNameplate)
ItemNamePlate.grid(row=1, column=0, padx=23, pady=(23, 22))

# define the name entry prompt
ItemEntryPrompt = Label(middle, text="Press Enter to submit", bg="#999")
ItemEntry = Entry(middle, width=42, validate="focusout", validatecommand=submitName)
ItemEntry.bind("<Return>", submitName)



#================================== Image Box ================================

# function that changes the image in response to events
def updateimage():
    ImageName = fun.selected_item["ItemType"]
    if ImageName == "": ImageName = "Blank"
    ItemImage = PhotoImage(file="images/" + ImageName + ".png")
    ItemImageBox.config(image=ItemImage)
    ItemImageBox.image=ItemImage

# create and addd the image box 
ItemImage = PhotoImage(file="images/Blank.png")
ItemImageBox = Label(middle, image=ItemImage, bg='#222')
ItemImageBox.grid(row=2, column=0)





#=============================== Item Description Box ================================

# updates the item description
def updateItemDescription():
    ItemDescription = fun.update_item_description()
    ItemDescriptionBox.config(text=ItemDescription)    
    ItemDescriptionBox.text=ItemDescription

# define / add the Item Description Box
ItemDescriptionBox = Label(rightside, 
text="", width=35, height=29, justify="left", anchor=NW, wraplength=250, padx=16, pady=10)
ItemDescriptionBox.grid(row=0, column=0, padx=(25, 24), pady=(25, 0))


#================== Export to Text Document Button =============

def clickExportTextButton():
    if "\n" in fun.update_item_description():
        name = generateName() + ".txt"
        with open(str(name), 'w') as f:
            f.write(fun.update_item_description())

exportTextButton = Button(rightside, text="Export to Text Document", padx=10, command=clickExportTextButton)
exportTextButton.grid(row=1, column=0, padx=20, pady=(0, 16))


CreateTab_Click()
window.mainloop()