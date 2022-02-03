# Imports
from tkinter import * 
  
# Constants
TITLE = "Prisions and Lizards"

class Creature:

	def __init__(self, _name, _health):

		self.name = _name
		self.health = _health

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d: "%s"' % (index, value))

def CreateRootWindow():
	# Creates the root window.
	global root
	root = Tk()   
	root.title(TITLE)


	#root.state("zoomed")

	creature1 = Creature("Skeleton", 100)
	creature2 = Creature("Townsfolk", 100)

	############ Encounter List ################
	encounter_Listbox= Listbox(root, width="20")
	encounter_Listbox.grid(row=1, column=0, rowspan=6, sticky="nsew")
	encounter_Listbox.bind('<<ListboxSelect>>', onselect)

	############ Health ################
	health_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	health_label.insert("1.0", "HP")
	health_label.grid(row=1, column=1)
	health_label.tag_configure("cntr", justify='center')
	health_label.tag_add("cntr", "1.0", "end")
	health_label.config(state=DISABLED)

	health_entry = Entry(root, width="3", font=("Arial, 20"))
	health_entry.grid(row=1, column=2)
	health_entry.insert(0, "100")
	

	############ Initative ################
	init_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	init_label.insert("1.0", "INIT")
	init_label.grid(row=1, column=3)
	init_label.tag_configure("cntr", justify='center')
	init_label.tag_add("cntr", "1.0", "end")
	init_label.config(state=DISABLED)

	init_entry = Entry(root, width="3", font=("Arial, 20"))
	init_entry.grid(row=1, column=4)
	init_entry.insert(0, "2")


	############ Armor Class ################
	ac_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	ac_label.insert("1.0", "AC")
	ac_label.grid(row=1, column=5)
	ac_label.tag_configure("cntr", justify='center')
	ac_label.tag_add("cntr", "1.0", "end")
	ac_label.config(state=DISABLED)

	ac_entry = Entry(root, width="3", font=("Arial, 20"))
	ac_entry.grid(row=1, column=6)
	ac_entry.insert(0, "13")


	############ Strength ################
	str_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	str_label.insert("1.0", "STR")
	str_label.grid(row=2, column=1)
	str_label.tag_configure("cntr", justify='center')
	str_label.tag_add("cntr", "1.0", "end")
	str_label.config(state=DISABLED)

	str_entry = Entry(root, width="3", font=("Arial, 20"))
	str_entry.grid(row=2, column=2)
	str_entry.insert(0, "+2")
	

	############ Dexterity ################
	dex_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	dex_label.insert("1.0", "DEX")
	dex_label.grid(row=2, column=3)
	dex_label.tag_configure("cntr", justify='center')
	dex_label.tag_add("cntr", "1.0", "end")
	dex_label.config(state=DISABLED)

	dex_entry = Entry(root, width="3", font=("Arial, 20"))
	dex_entry.grid(row=2, column=4)
	dex_entry.insert(0, "+2")


	############ Constitution ################
	con_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	con_label.insert("1.0", "CON")
	con_label.grid(row=2, column=5)
	con_label.tag_configure("cntr", justify='center')
	con_label.tag_add("cntr", "1.0", "end")
	con_label.config(state=DISABLED)

	con_entry = Entry(root, width="3", font=("Arial, 20"))
	con_entry.grid(row=2, column=6)
	con_entry.insert(0, "+2")


	############ Intelegance ################
	int_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	int_label.insert("1.0", "INT")
	int_label.grid(row=3, column=1)
	int_label.tag_configure("cntr", justify='center')
	int_label.tag_add("cntr", "1.0", "end")
	int_label.config(state=DISABLED)

	int_entry = Entry(root, width="3", font=("Arial, 20"))
	int_entry.grid(row=3, column=2)
	int_entry.insert(0, "+2")
	

	############ Wisdom ################
	wis_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	wis_label.insert("1.0", "WIS")
	wis_label.grid(row=3, column=3)
	wis_label.tag_configure("cntr", justify='center')
	wis_label.tag_add("cntr", "1.0", "end")
	wis_label.config(state=DISABLED)

	wis_entry = Entry(root, width="3", font=("Arial, 20"))
	wis_entry.grid(row=3, column=4)
	wis_entry.insert(0, "+2")


	############ Charisma ################
	cha_label = Text(root, width="4", height="1", borderwidth="2", font=("Arial", 20), bg="grey")
	cha_label.insert("1.0", "CHA")
	cha_label.grid(row=3, column=5)
	cha_label.tag_configure("cntr", justify='center')
	cha_label.tag_add("cntr", "1.0", "end")
	cha_label.config(state=DISABLED)

	cha_entry = Entry(root, width="3", font=("Arial, 20"))
	cha_entry.grid(row=3, column=6)
	cha_entry.insert(0, "+2")


	############ Vunerablilities ################
	vuln_lable = Label(root, text="Vulnerabilities", font=("Arial, 20"), bg="grey")
	vuln_lable.grid(row=4, column=1)

	vuln_entry = Entry(root, font=("Arial, 20"))
	vuln_entry.grid(row=4, column=2, columnspan=5)
	vuln_entry.insert(0, "Bludgeoning")


	############ Damgae Imunities ################
	dmgImm_lable = Label(root, text="Dmg Immune", font=("Arial, 20"), bg="grey")
	dmgImm_lable.grid(row=5, column=1)

	dmgImm_entry = Entry(root, font=("Arial, 20"))
	dmgImm_entry.grid(row=5, column=2, columnspan=5)
	dmgImm_entry.insert(0, "Poison")

	#int_label = Label(root, width="10", text="INT")
	#int_label.grid(row=2, column=1, sticky="nsew")


def Main():
	

	CreateRootWindow()
	root.mainloop() 

if __name__ == "__main__":
	Main()