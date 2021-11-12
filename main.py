from tkinter import *
from tkinter import ttk
# Main Window
root= Tk()
root.geometry('600x500')
root.title('Unit Convertor')
root.resizable(False, False)
# GUI
def km_milesCommand(event):
	commands= Commands()
	commands.km_miles()
def unit_combo_command(event):
	commands= Commands()
	commands.unit_combo()
class Commands:
	def km_miles(self):
		self.answer= float(int(label1_entry.get())) * 0.621371 
		label1_entry.delete(0, 'end')
		label2_answer.config(text= self.answer)
	def unit_combo(self):
		if unit_combo.current() == 0:
			label1.config(text= 'km:')
			label2.config(text= 'miles:')
		elif unit_combo.current() == 1:
			label1.config(text= 'm:')
			label2.config(text= 'yard:')
			label1_entry.destroy()
			label1_entry2= ttk.Entry(root)
			label1_entry2.place(x= 100, y= 285)
		elif unit_combo.current() == 2:
			label1.config(text= 'm:')
			label2.config(text= 'foot:')
		elif unit_combo.current() == 3:
			label1.config(text= 'cm:')
			label2.config(text= 'inch:')
		elif unit_combo.current() == 0:
			label1.config(text= 'km:')
			label2.config(text= 'miles:')

title= ttk.Label(root, text= 'Unit Convertor', font= ('tkfixedfont 15', 20, 'bold'))
title.place(x= 200, y= 10)

type_label= ttk.Label(root, text= 'Type:', font= ('tkfixedfont 15', 15, 'bold'))
type_label.place(x= 10, y= 100)

type_List= [
'Length',
'Width'
]
type_combo= ttk.Combobox(root, value= type_List)
type_combo.current(0)
type_combo.place(x= 100, y= 105)

unit_label= Label(root, text= 'Units:', font= ('tkfixedfont 15', 15, 'bold'))
unit_label.place(x= 10, y= 200)

unit_list= [
'km - miles',
'm - yard',
'm - foot',
'cm - inch'
]
unit_combo= ttk.Combobox(root, value= unit_list)
unit_combo.current(0)
unit_combo.bind('<<ComboboxSelected>>', unit_combo_command)
unit_combo.place(x= 100, y= 205)

label1= Label(root, text= 'km:', font= ('tkfixedfont 15', 15, 'bold'))
label1.place(x= 10, y= 280)

label1_entry= ttk.Entry(root)
label1_entry.bind('<Return>', km_milesCommand)
label1_entry.place(x= 100, y= 285)


label2= Label(root, text= 'miles:', font= ('tkfixedfont 15', 15, 'bold'))
label2.place(x= 10, y= 330)

label2_answer= Label(root, text= '', font= ('tkfixedfont 15', 18, 'bold'))
label2_answer.place(x= 100, y= 330)


root.mainloop()