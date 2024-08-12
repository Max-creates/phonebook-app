from tkinter import *
from tkinter import ttk

#colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

window = Tk()
window.title("")
window.geometry("485x450")
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)

#frames
frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co2)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)

#frame_up widgets

app_name = Label(frame_up, text="Phonebook", height=1, font=('Verdana 17 bold'), bg=co2, fg=co0)
app_name.place(x=5, y=5)

#frame_down widgets
l_name = Label(frame_down, text="Name *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

l_gender = Label(frame_down, text="Gender *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_down, width=27)
c_gender['values'] = ['', 'F', 'M']
c_gender.place(x=80, y=50)

l_telephone = Label(frame_down, text="Telephone*", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_telephone.place(x=10, y=80)
e_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_telephone.place(x=80, y=80)

l_email = Label(frame_down, text="Email *", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_email.place(x=10, y=110)
e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_email.place(x=80, y=110)

window.mainloop()