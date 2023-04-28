import tkinter as tk
from tkinter import *
import tkinter.font as font



############################# SCREEN BASICS ################################
#=============== base window #===============
window = tk.Tk()
window.title("Item Generator Program")
window.geometry("958x562")
window.configure(bg='#555')
window.iconbitmap('images/favicon.ico')

#=============== make frames #===============
header = LabelFrame(window, bg="#999", width="1000", height="40")
leftside = LabelFrame(window, bg="#999", width="325", height="560")
middle = LabelFrame(window, bg="#999", width="350", height="560")
rightside = LabelFrame(window, bg="#999", width="325", height="560")



############################ LEFTSIDE ELEMENTS #############################
#=============== item type dropdown menues #===============
options = ["no selection", "option 1", "option 2", "option 3", "option 4", "option 5"]

ItemTypeOption = StringVar()
ItemTypeOption.set(options[0])
ItemTypeOptionDDM = OptionMenu(leftside, ItemTypeOption, *options)

#=============== cost box #===============
EnchantCost = "Enchant Cost: " + "100000"
TotaCost = "Tota Cost: " + "55555"

TotaCostBox = Label(leftside, text=TotaCost, bg="#fff", width=30, pady=5)
EnchantCostBox = Label(leftside, text=EnchantCost, bg="#fff", width=30, pady=5)

#=============== Enchant dropdown menues #===============
EnchantOption = StringVar()
EnchantOption.set(options[0])
EnchantOptionDDM = OptionMenu(leftside, EnchantOption, *options)

PowerOption = StringVar()
PowerOption.set(options[0])
PowerOptionDDM = OptionMenu(leftside, PowerOption, *options)

VariationOption = StringVar()
VariationOption.set(options[0])
VariationOptionDDM = OptionMenu(leftside, VariationOption, *options)

#=============== Enchant slot selection #===============
SelectedEnchant = StringVar()
SelectedEnchant.set("Prefix")

SelectPrefix = Radiobutton(leftside, text="Item Prefix", width=24,
    variable=SelectedEnchant, value="Prefix")
SelectSuffix = Radiobutton(leftside, text="Item Suffix", width=24,
    variable=SelectedEnchant, value="Suffix")
SelectTertiary = Radiobutton(leftside, text="Item Tertiary", width=24,
    variable=SelectedEnchant, value="Tertiary")
SelectTrigger = Radiobutton(leftside, text="Item Trigger", width=24,
    variable=SelectedEnchant, value="Trigger")

#=============== Completed Items List #===============
options = [range(0, 25)]
CompletedItemsList = Listbox(leftside, width=39, height=28)

#=============== Modify Button #===============
ModifyButton = Button(leftside, text="Modify Item", padx=12)



############################### MIDLE ELEMENTS #############################
#=============== Name Plate #===============
ItemName = "Trinket"
ItemNamePlate = Label(middle, text=ItemName, width=42, height=2)


#=============== Item Image #===============
ItemImage = PhotoImage(file='images/trinket.png')
ItemImageBox = Label(middle, image=ItemImage, bg='#222')


#=============== Create Button #===============
bigFont = font.Font(family='Helvetica', size=25)
CreateButton = Button(middle, text="Create", width=9, font=bigFont)


#=============== Salvage Button #===============
bigFont = font.Font(family='Helvetica', size=25)
SalvageButton = Button(middle, text="Salvage", width=9, font=bigFont)



######################### RIGHTSIDE ELEMENTS #############################
#=============== Item Description #===============
descFont = font.Font(size=11)

ItemDescription = ""

ItemDescriptionBox = Label(rightside, 
    text=ItemDescription, 
    width=28, height=25, 
    anchor=NW, wraplength=250,
    padx=15, pady=15, 
    font=descFont)

TextToClipboardButton = Button(rightside, text="Copy to Clipboard", padx=12)



######################### UI FUNCTIONALITY ###############################
def BOOT_UP():
    #================== make frames ==================
    header.grid(row=0, column=0, columnspan=3) 
    leftside.grid(row=1, column=0) 
    middle.grid(row=1, column=1)
    rightside.grid(row=1, column=2)

    #================== make tabs ====================
    CreateTab.grid(row=0, column=0, padx=(295, 1))
    LoadTab.grid(row=0, column=1, padx=(0,360))

    #================== Name Plate ===================
    ItemNamePlate.grid(row=0, column=0, padx=25, pady=25)

    #================== Item Image ===================
    ItemImageBox.grid(row=1, column=0)

    #================== Item Description =============
    ItemDescriptionBox.grid(row=0, column=0, padx=22, pady=(25, 0))
    TextToClipboardButton.grid(row=1, column=0, padx=20, pady=(0, 16))


def ClearTab():
    CompletedItemsList.grid_forget()
    ModifyButton.grid_forget()
    SalvageButton.grid_forget()
    ItemTypeOptionDDM.grid_forget()
    TotaCostBox.grid_forget()
    EnchantCostBox.grid_forget()
    EnchantOptionDDM.grid_forget()
    EnchantOptionDDM.grid_forget()
    PowerOptionDDM.grid_forget()
    VariationOptionDDM.grid_forget()
    SelectPrefix.grid_forget()
    SelectSuffix.grid_forget()
    SelectTertiary.grid_forget()
    SelectTrigger.grid_forget()
    CreateButton.grid_forget()



def LoadTab_Click():
    ClearTab()
    #================== listbox ======================
    CompletedItemsList.grid(row=0, column=0, pady=(25, 0), padx=(14, 13))

    #================== Modify Button ================
    ModifyButton.grid(row=1, column=0, padx=20, pady=(0, 23))

    #================== Create Button ================
    SalvageButton.grid(row=2, column=0, padx=25, pady=24)



def CreateTab_Click():
    ClearTab()
    #================== item type dropdown menues ==================
    ItemTypeOptionDDM.grid(row=0, column=0, pady=(29, 40), padx=20)
    ItemTypeOptionDDM.config(width=30)

    #================== cost box ==================
    TotaCostBox.grid(row=1, column=0, pady=(0, 0))
    EnchantCostBox.grid(row=2, column=0, pady=(0, 40))

    #================== Enchant dropdown menues ==================
    EnchantOptionDDM.grid(row=3, column=0)
    EnchantOptionDDM.config(width=30)

    PowerOptionDDM.grid(row=4, column=0, pady=15)
    PowerOptionDDM.config(width=30)

    VariationOptionDDM.grid(row=5, column=0)
    VariationOptionDDM.config(width=30)

    #================== Enchant slot selection ================== 
    SelectPrefix.grid(row=6, column=0, pady=(40, 6))
    SelectSuffix.grid(row=7, column=0, pady=6)
    SelectTertiary.grid(row=8, column=0, pady=6)
    SelectTrigger.grid(row=9, column=0, pady=(6, 29))

    #================== Create Button ==================
    CreateButton.grid(row=2, column=0, padx=25, pady=24)


CreateTab = Button(header, text="Create New Item", padx=25, command=CreateTab_Click)
LoadTab = Button(header, text="Completed Items", padx=25, command=LoadTab_Click)



BOOT_UP()
CreateTab_Click()
window.mainloop()