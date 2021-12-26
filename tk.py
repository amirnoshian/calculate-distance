from tkinter import *
from tkinter.font import *
from tkinter import messagebox
from unitconverter import *
def calculate_unit():
   unit_from = list_box_from.get(ACTIVE)
   unit_to = list_box_to.get(ACTIVE)
   value_from = int(entry_from.get())
   entry_to.delete(0,END)
   entry_to.insert(END,unit_converter(value=value_from,unit_from=unit_from,unit_to=unit_to)) 
 
window = Tk()
my_font= Font(family='consoals', size=12)
to_font= Font(family='consoals', size=15)
other_font= Font(family='consoals', size=10)
pad_x = 10
pad_y =10
# wared kardan esm soton ha
Label_from = Label(window, text = "first", font = to_font)
Label_to = Label(window, text = "second ",font = to_font)
# jagozari soton ha ke dar kodam bakhsh bashand
Label_from.grid(row=0, column=0,sticky=W,padx = pad_x,pady= pad_y)
Label_to.grid(row=0, column=1,sticky=W)
# entry
entry_from = Entry(window,font= my_font,fg='brown')
entry_to = Entry(window,font= my_font,fg = 'brown')
entry_from.grid(row=1, column=0)
entry_to.grid(row=1, column=1)
#list box 
list_box_from = Listbox(window,exportselection=False,font = other_font) 

list_box_to = Listbox(window,exportselection=False,font = other_font)
list_box_from.grid(row=2, column=0)
list_box_to.grid(row=2, column=1)
list_box_from.insert(END, 'cm')
list_box_from.insert(END, 'm')
list_box_from.insert(END, 'km')
list_box_from.insert(END, 'mile')
list_box_from.insert(END, 'yard')

list_box_to.insert(END, 'cm')
list_box_to.insert(END, 'm')
list_box_to.insert(END, 'km')
list_box_to.insert(END, 'mile')
list_box_to.insert(END, 'yard')
# calculate key
button = Button(window,text='calculate',font= my_font,command= calculate_unit)
button.grid(row=3 ,column=0,columnspan=2,sticky=W+E)
window.mainloop()

